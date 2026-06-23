from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "mensaje": "Backend funcionando"
    })

@app.route("/api/book")
def health():
    return jsonify({
        "status" : "ok",
        "book" : "Harry potter"
    })

if __name__ == "__main__":
    app.run(debug= True)