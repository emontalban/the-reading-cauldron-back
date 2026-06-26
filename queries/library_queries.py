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

def get_library_item_by_id_and_user_id(library_id, user_id):
    con = get_db_connection()

    if con is None:
        return None

    cursor = con.cursor(dictionary=True)

    sql = """
        SELECT
            library_id,
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
            library_ownership,
            library_created_at,
            library_updated_at
        FROM library
        WHERE library_id = %s
        AND library_user_id = %s
    """

    cursor.execute(sql, (library_id, user_id))

    library_item = cursor.fetchone()

    cursor.close()
    con.close()

    return library_item

def update_library(library_id,user_id, data):
    con = get_db_connection()

    if con is None:
        return False
    
    cursor = con.cursor()
    sql = """
        UPDATE library
        SET
            library_status = %s,
            library_format = %s,
            library_rating = %s,
            library_current_page = %s,
            library_start_date = %s,
            library_finish_date = %s,
            library_notes = %s,
            library_favorite = %s,
            library_ownership = %s
        WHERE library_id = %s
        AND library_user_id = %s
    """
    values=(
        data.get("library_status"),
        data.get("library_format"),
        data.get("library_rating"),
        data.get("library_current_page"),
        data.get("library_start_date"),
        data.get("library_finish_date"),
        data.get("library_notes"),
        data.get("library_favorite"),
        data.get("library_ownership"),
        library_id,
        user_id
    )
    cursor.execute(sql, values)
    con.commit()
    update_rows = cursor.rowcount

    cursor.close()
    con.close()
    return update_rows > 0

def delete_library(library_id, user_id):
    con = get_db_connection()

    if con is None:
        return False
    
    cursor = con.cursor()
    sql = "DELETE FROM library WHERE library_id = %s AND library_user_id = %s"

    cursor.execute(sql, (library_id, user_id))
    con.commit()

    delete_rows = cursor.rowcount

    cursor.close()
    con.close()

    return delete_rows >0
