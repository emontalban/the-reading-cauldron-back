import os
import jwt

from datetime import datetime, timedelta, timezone
from flask import jsonify, request
from werkzeug.security import check_password_hash

from queries.users_queries import get_user_by_email
from helpers.auth_helpers import get_current_user_from_token

def register_auth_routes(app):
    @app.route("/login", methods=["POST"])
    def login_route():
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No se recibieron datos"
            }), 400
        
        if not data.get("user_email") or not data.get("user_password"):
            return jsonify({
                "status": "error",
                "message": "El email y la contraseña no pueden estar vacios"
            }), 400

        user = get_user_by_email(data.get("user_email"))

        if user is None:
            return jsonify({
                "status": "error",
                "message": "Email o contraseña incorrectos"
            }), 401

        password_is_valid = check_password_hash(
            user["user_password_hash"],
            data.get("user_password")
        )

        if not password_is_valid:
            return jsonify({
                "status": "error",
                "message": "Email o contraseña incorrectos"
            }), 401
        
        #Este token sera valido durante dos horas
        payload = {
            "user_id": user["user_id"],
            "user_name": user["user_name"],
            "user_email": user["user_email"],
            "exp": datetime.now(timezone.utc) + timedelta(hours=2)
        }

        token = jwt.encode(
            payload,
            os.getenv("JWT_SECRET_KEY"),
            algorithm="HS256"
        )

        return jsonify({
            "status": "ok",
            "message": "Login correcto",
            "token": token,
            "user": {
                "user_id": user["user_id"],
                "user_name": user["user_name"],
                "user_email": user["user_email"]
            }
        })
    


    @app.route("/profile", methods=["GET"])
    def profile_route():
        current_user, error_response, status_code = get_current_user_from_token()

        if error_response:
            return jsonify(error_response), status_code

        return jsonify({
            "status": "ok",
            "message": "Token válido",
            "user": {
                "user_id": current_user["user_id"],
                "user_name": current_user["user_name"],
                "user_email": current_user["user_email"]
            }
        })