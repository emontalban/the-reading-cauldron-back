from database.connection import get_db_connection

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

def create_book(data):
    con = get_db_connection()

    if con is None:
        return None
    
    cursor = con.cursor()

    sql = """
        INSERT INTO books (
                book_title,
                book_author,
                book_isbn,
                book_description,
                book_pages,
                book_language,
                book_category,
                book_cover_url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

    """
    values = (
        data.get("book_title"),
        data.get("book_author"),
        data.get("book_isbn"),
        data.get("book_description"),
        data.get("book_pages"),
        data.get("book_language"),
        data.get("book_category"),
        data.get("book_cover_url")
    )

    cursor. execute(sql, values)

    con.commit()

    book_id = cursor.lastrowid

    cursor.close()
    con.close()

    return book_id

def get_book_by_id(id):
    con = get_db_connection()

    if con is None:
        return None
    
    cursor = con.cursor(dictionary=True)
    
    sql = """
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
        WHERE book_id = %s
    """

    cursor.execute(sql,(id,))

    book = cursor.fetchone()

    cursor.close()
    con.close()

    return book

def update_book(id, data):
    con = get_db_connection()

    if con is None:
        return False
    
    cursor = con.cursor()
    sql = """
        UPDATE books
        SET
            book_title = %s,
            book_author = %s,
            book_isbn = %s,
            book_description = %s,
            book_pages = %s,
            book_language = %s,
            book_category = %s,
            book_cover_url = %s
        WHERE book_id = %s
    """

    values = (
        data.get("book_title"),
        data.get("book_author"),
        data.get("book_isbn"),
        data.get("book_description"),
        data.get("book_pages"),
        data.get("book_language"),
        data.get("book_category"),
        data.get("book_cover_url"),
        id
    )

    cursor.execute(sql, values)

    con.commit()

    cursor.close()

    con.close()

    return True


def delete_book(id):
    con = get_db_connection()

    if con is None:
        return False

    cursor = con.cursor()

    sql = """
        DELETE FROM books
        WHERE book_id = %s
    """

    cursor.execute(sql, (id,))

    con.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    con.close()

    return deleted_rows > 0
