from flask import jsonify

from queries.db_queries import get_database_name

def register_db_routes(app):
    @app.route("/db-test", methods=["GET"])
    def db_test():
        result = get_database_name()

        if result is None:
            return jsonify({
                "status": "error",
                "message": "No se pudo conectar con la base de datos"
            }), 500

        return jsonify({
            "status": "ok",
            "message": "Conexión con MySQL funcionando correctamente",
            "database": result["database_name"]
        })