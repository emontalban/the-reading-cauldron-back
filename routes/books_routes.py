from flask import jsonify, request

from queries.books_queries import get_books, create_book, get_book_by_id, update_book, delete_book, get_existing_book

def register_book_routes(app):
    @app.route("/books", methods=["GET"])
    def get_books_routes():
        books = get_books()
        return jsonify(books)
    
    @app.route("/books", methods=["POST"])
    def create_book_route():
        data = request.get_json()

        if not data:
            return jsonify({
                "status" : "error",
                "message" : "No se recibieron datos"
            }), 400
        
        if not data.get("book_title") or not data.get("book_author"):
            return jsonify({
                "status": "error",
                "message": "El título y el autor son obligatorios"
            }), 400
        
        existing_book = get_existing_book(data)

        if existing_book is not None:
            return jsonify({
                "status": "error",
                "message": "Este libro ya existe en la base de datos",
                "book": existing_book
            }), 409

        book_id = create_book(data)

        if book_id is None:
            return jsonify({
                "status": "error",
                "message": "No se pudo crear el libro"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Libro creado correctamente",
            "book_id": book_id
        }), 201
    
    @app.route("/books/<int:id>", methods=["GET"])
    def get_book_by_id_route(id):
        book = get_book_by_id(id)

        if book is None:
            return jsonify({
                "status": "error",
                "message": "Libro no encontrado"
            }),404
        
        return jsonify(book)
    

    @app.route("/books/<int:id>", methods=["PUT"])
    def update_book_route(id):
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "message": "No se recibieron datos"
            }), 400

        if not data.get("book_title") or not data.get("book_author"):
            return jsonify({
                "status": "error",
                "message": "El título y el autor son obligatorios"
            }), 400

        book = get_book_by_id(id)

        if book is None:
            return jsonify({
                "status": "error",
                "message": "Libro no encontrado"
            }), 404

        updated = update_book(id, data)

        if not updated:
            return jsonify({
                "status": "error",
                "message": "No se pudo actualizar el libro"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Libro actualizado correctamente",
            "book_id": id
        })
    
    @app.route("/books/<int:id>",  methods=["DELETE"])
    def  delete_book_route(id):
        book = get_book_by_id(id)

        if book is None:
            return jsonify({
                "status": "error",
                "message" : "Libro no encontrado"
            }), 404
        
        deleted = delete_book(id)

        if not deleted:
            return jsonify({
                "status": "error",
                "message": "No se pudo eliminar el libro"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Libro eliminado correctamente",
            "book_id": id
        }) 
