from datetime import datetime


VALID_LIBRARY_STATUSES = [
    "quiero_leer",
    "pendiente",
    "leyendo",
    "terminado",
    "abandonado"
]

VALID_LIBRARY_FORMATS = [
    "papel",
    "digital",
    "audiolibro"
]

VALID_LIBRARY_OWNERSHIPS = [
    "propio",
    "prestado",
    "biblioteca",
    "no_lo_tengo"
]

def is_valid_date(date_value):
    if date_value is None or date_value =="":
        return True
    
    try:
        datetime.strptime(date_value, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    

def validate_library_data(data, require_book_id=False):
    if require_book_id:
        library_book_id = data.get("library_book_id")

        if type(library_book_id) is not int or library_book_id <=0:
            return {
                "status": "error",
                "message": "El ID debe ser mayor que 0"
            }
        
    library_status = data.get("library_status")
    if library_status is not None and library_status not in VALID_LIBRARY_STATUSES:
        return{
            "status": "error",
            "message" : "Estado no valido"
        }
    
    library_format = data.get("library_format")
    if library_format is not None and library_format not in VALID_LIBRARY_FORMATS:
        return{
            "status":"error",
            "message": "Formato no valido"
        }
    
    library_rating = data.get("library_rating")
    if library_rating is not None:
        if type(library_rating) is not int or library_rating < 0 or library_rating > 5:
            return{
                "status" : "error",
                "message" : "Debe de ser un numero entre 0 y 5"
            }
    library_current_page = data.get("library_currente_page")   
    if library_current_page is not None:
        if type(library_current_page)is not int or library_current_page < 0:
            return{
                "status" : "error",
                "message" : "La pagina actual debe de ser mayor que cero"
            }
        
    library_start_date = data.get("library_start_date")
    if not is_valid_date(library_start_date):
        return{
            "status": "error",
            "message": "la fecha de inicio debe tener formato DD-MM-YY"
        }
    
    library_favorite = data.get("library_favorite")
    if library_favorite is not None and type(library_favorite) is not bool:
        return {
            "status": "error",
            "message": "El campo favorito debe ser true o false"
        }

    library_ownership = data.get("library_ownership")
    if library_ownership is not None and library_ownership not in VALID_LIBRARY_OWNERSHIPS:
        return {
            "status": "error",
            "message": "Tipo de propiedad no válido"
        }

    return None