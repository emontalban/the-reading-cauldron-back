from flask import jsonify

def register_book_routes(app):
    @app.route("/book")
    def book_test():
        return jsonify({
            "status": "ok",
            "book": "Harry Potter"
        })