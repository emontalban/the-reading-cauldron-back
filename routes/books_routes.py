from flask import jsonify

from queries.db_queries import get_books

def register_book_routes(app):
    @app.route("/books", methods=["GET"])
    def get_books_routes():
        books = get_books()
        return jsonify(books)
    
