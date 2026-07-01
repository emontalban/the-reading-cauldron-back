from flask import jsonify, request

from queries.users_queries import get_users, create_user, get_existing_user


def register_user_routes(app):
    @app.route("/users", methods=["GET"])
    def get_users_route():
        users = get_users()

        return jsonify(users)

    @app.route("/users", methods=["POST"])
    def create_user_route():
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No se recibieron datos"
            }), 400

        if not data.get("user_name") or not data.get("user_email") or not data.get("user_password"):
            return jsonify({
                "status": "error",
                "message": "El nombre, email y password son obligatorios"
            }), 400
        
        existing_user = get_existing_user(data)

        if existing_user["user_email"] == data.get("user_email"):
            return jsonify({
                "status": "error",
                "message" : "Este email ya esta registrado"
            }),409
        if existing_user["user_name"] == data.get("user_name"):
            return jsonify({
                "status" : "error",
                "message" : "Este nombre ya existe"
            }), 409
        



        user_id = create_user(data)
        if user_id == "duplicate":
            return jsonify({
                "status": "error",
                "message": "Este usuario ya existe"
            }), 409

        if user_id is None:
            return jsonify({
                "status": "error",
                "message": "No se pudo crear el usuario"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Usuario creado correctamente",
            "user_id": user_id
        }), 201