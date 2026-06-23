from flask import jsonify

def register_home_routes(app):
    @app.route("/")
    def home():
        return jsonify({
            "mensaje": "Backend funcionando"
        })