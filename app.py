from flask import Flask
from flask_cors import CORS

from routes.home_routes import register_home_routes
from routes.db_routes import register_db_routes
from routes.books_routes import register_book_routes
from routes.user_routes import register_user_routes
from routes.auth_routes import register_auth_routes
from routes.library_routes import register_library_routes

app = Flask(__name__)
CORS(app)

register_home_routes(app)
register_db_routes(app)
register_book_routes(app)
register_user_routes(app)
register_auth_routes(app)
register_library_routes(app)

if __name__ == "__main__":
    app.run(debug=True)