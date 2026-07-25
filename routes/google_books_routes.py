
import os
import requests

from flask import request, jsonify

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"

RETRYABLE_GOOGLE_STATUSES = (
    429,
    500,
    502,
    503,
    504,
)


def create_google_session():
    retry_policy = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=0.5,
        status_forcelist=RETRYABLE_GOOGLE_STATUSES,
        allowed_methods={"GET"},
        respect_retry_after_header=True,
        raise_on_status=False,
    )

    session = requests.Session()

    session.mount(
        "https://",
        HTTPAdapter(max_retries=retry_policy),
    )

    return session

def register_google_books_routes(app):
    @app.route("/google-books", methods=["GET"])
    def search_google_books():
        query = request.args.get("q", "").strip()

        if not query:
            return jsonify({
                "status": "error",
                "message": "El  texto de busqueda es obligatorio"
            }), 400

        api_key = os.getenv("GOOGLE_BOOKS_API_KEY")


        if not api_key:
            return jsonify({
                "status": "error",
                "message": "Falta la clave de google books"
            }),500

        try:
           with create_google_session() as google_session:
                response = google_session.get(
                    GOOGLE_BOOKS_URL,
                    params={
                        "q": query,
                        "maxResults": 12,
                        "printType": "books",
                        "key": api_key,
                    },
                    timeout=10,
                )


                response.raise_for_status()

                data =response.json()
                books = data.get("items", [])
                return jsonify({
                    "status": "ok",
                    "books" : books
                }),200

        except requests.exceptions.Timeout:
            return jsonify({
                "status": "error",
                "message": (
                    "Google Books tardó demasiado "
                    "en responder"
                ),
            }), 504

        except requests.exceptions.HTTPError as error:
            google_status = error.response.status_code

            print(
                f"Google Books respondió con HTTP "
                f"{google_status}: {error.response.text}"
            )

            if google_status in RETRYABLE_GOOGLE_STATUSES:
                message = (
                    "Google Books no está disponible temporalmente. "
                    "Inténtalo de nuevo en unos segundos."
                )
            else:
                message = (
                    "Google Books rechazó la petición. "
                    "Revisa que la API esté activada y "
                    "las restricciones de la clave."
                )

            return jsonify({
                "status": "error",
                "message": message,
                "google_status": google_status,
            }), 502

        except requests.exceptions.RequestException as error:
            print(
                f"Error de conexión con Google Books: {error}"
            )

            return jsonify({
                "status": "error",
                "message": (
                    "No se pudo establecer conexión "
                    "con Google Books"
                ),
            }), 503

       

    