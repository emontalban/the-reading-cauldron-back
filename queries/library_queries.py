from database.connection import get_db_connection

def get_library_by_user_id(user_id):
    con = get_db_connection()

    if con is None:
        return []
    
    cursor = con.cursor(dictionary=True)

    sql = """
        SELECT
            library.library_id,
            library.library_user_id,
            library.library_book_id,
            library.library_status,
            library.library_format,
            library.library_rating,
            library.library_current_page,
            library.library_start_date,
            library.library_finish_date,
            library.library_notes,
            library.library_favorite,
            library.library_ownership,
            library.library_created_at,
            library.library_updated_at,

            books.book_id,
            books.book_title,
            books.book_author,
            books.book_isbn,
            books.book_description,
            books.book_pages,
            books.book_language,
            books.book_category,
            books.book_cover_url
        FROM library
        INNER JOIN books
            ON library.library_book_id = books.book_id
        WHERE library.library_user_id = %s
        ORDER BY library.library_created_at DESC
    """

    cursor.execute(sql, (user_id,))
    

    library_items = cursor.fetchall()

    cursor.close()
    con.close()

    return library_items

def add_book_to_library(user_id, data):
    con = get_db_connection()

    if con is None:
        return None

    cursor = con.cursor()

    sql = """
        INSERT INTO library (
            library_user_id,
            library_book_id,
            library_status,
            library_format,
            library_rating,
            library_current_page,
            library_start_date,
            library_finish_date,
            library_notes,
            library_favorite,
            library_ownership
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        user_id,
        data.get("library_book_id"),
        data.get("library_status", "pendiente"),
        data.get("library_format", "papel"),
        data.get("library_rating"),
        data.get("library_current_page", 0),
        data.get("library_start_date"),
        data.get("library_finish_date"),
        data.get("library_notes"),
        data.get("library_favorite", False),
        data.get("library_ownership", "propio")
    )

    cursor.execute(sql, values)

    con.commit()

    library_id = cursor.lastrowid

    cursor.close()
    con.close()

    return library_id