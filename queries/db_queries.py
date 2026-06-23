from database.connection import get_db_connection

def get_database_name():
    con = get_db_connection()

    if con is None:
        return None

    cursor = con.cursor(dictionary=True)

    cursor.execute("SELECT DATABASE() AS database_name")

    result = cursor.fetchone()

    cursor.close()
    con.close()

    return result

def get_books():
    con = get_db_connection()

    if con is None:
        return []

    cursor = con.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            book_id,
            book_title,
            book_author,
            book_isbn,
            book_description,
            book_pages,
            book_language,
            book_category,
            book_cover_url,
            book_created_at
        FROM books
        ORDER BY book_created_at DESC
    """)

    books = cursor.fetchall()

    cursor.close()
    con.close()

    return books