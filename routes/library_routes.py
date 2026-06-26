from flask import jsonify, request

from helpers.auth_helpers import get_current_user_from_token
from queries.library_queries import get_library_by_user_id, add_book_to_library, get_library_item_by_id_and_user_id, update_library
from queries.books_queries import get_book_by_id


def register_library_routes(app):
    @app.route("/library", methods=["GET"])
    def get_library_route():
        current_user, error_response, status_code = get_current_user_from_token()

        if error_response:
            return jsonify(error_response), status_code

        library_items = get_library_by_user_id(current_user["user_id"])

        return jsonify(library_items)

    @app.route("/library", methods=["POST"])
    def add_book_to_library_route():
        current_user, error_response, status_code = get_current_user_from_token()

        if error_response:
            return jsonify(error_response), status_code

        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No se recibieron datos"
            }), 400

        if not data.get("library_book_id"):
            return jsonify({
                "status": "error",
                "message": "El ID del libro es necesrio"
            }), 400

        book = get_book_by_id(data.get("library_book_id"))

        if book is None:
            return jsonify({
                "status": "error",
                "message": "El libro no existe"
            }), 404

        library_id = add_book_to_library(current_user["user_id"], data)

        if library_id is None:
            return jsonify({
                "status": "error",
                "message": "No se pudo añadir el libro a la biblioteca"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Libro añadido a la biblioteca correctamente",
            "library_id": library_id
        }), 201
    
    @app.route("/library/<library_id>", methods = ["PUT"])
    def update_library_route(library_id):
        current_user, error_response, status_code = get_current_user_from_token()

        if error_response:
            return jsonify(error_response, status_code)
        
        data = request.get_json()
        if not data:
            return({
                "status": "error",
                "message": "No se recibieror datos"
            }), 400
        
        library_item = get_library_item_by_id_and_user_id(library_id, current_user["user_id"])
        if library_item is None:
            return jsonify({
                "status": "error",
                "message": "No se puedo acutalizar"
            }), 500
        
        return jsonify({
            "status": "ok",
            "message": "Elemento de biblioteca actualizado correctamente",
            "library_id": library_id
        })