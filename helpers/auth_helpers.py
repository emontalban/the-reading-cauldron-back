import os
import jwt

from flask import request


def get_current_user_from_token():
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None, {
            "status": "error",
            "message": "Token no enviado"
        }, 401

    if not auth_header.startswith("Bearer "):
        return None, {
            "status": "error",
            "message": "Formato de token incorrecto"
        }, 401

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(
            token,
            os.getenv("JWT_SECRET_KEY"),
            algorithms=["HS256"]
        )

        return payload, None, None

    except jwt.ExpiredSignatureError:
        return None, {
            "status": "error",
            "message": "Token caducado"
        }, 401

    except jwt.InvalidTokenError:
        return None, {
            "status": "error",
            "message": "Token inválido"
        }, 401