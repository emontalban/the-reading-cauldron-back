from flask import Flask, jsonify
from flask_cors import CORS
from database.connection import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "mensaje": "Backend funcionando"
    })

@app.route("/book")
def health():
    return jsonify({
        "status" : "ok",
        "book" : "Harry potter"
    })


@app.route("/db-test")
def db_test():
    connection = get_db_connection()

    if connection is None:
        return jsonify({
            "status": "error",
            "message": "No se pudo conectar con la base de datos"
        }), 500

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT DATABASE() AS database_name")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify({
        "status": "ok",
        "message": "Conexión con MySQL funcionando correctamente",
        "database": result["database_name"]
    })

if __name__ == "__main__":
    app.run(debug= True)