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