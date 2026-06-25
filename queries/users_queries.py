from database.connection import get_db_connection
from werkzeug.security import generate_password_hash


def get_users():
    con = get_db_connection()

    if con is None:
        return []

    cursor = con.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            user_id,
            user_name,
            user_email,
            user_created_at
        FROM users
        ORDER BY user_created_at DESC
    """)

    users = cursor.fetchall()

    cursor.close()
    con.close()

    return users


def create_user(data):
    con = get_db_connection()

    if con is None:
        return None

    cursor = con.cursor()

    password_hash = generate_password_hash(data.get("user_password"))

    sql = """
        INSERT INTO users (
            user_name,
            user_email,
            user_password_hash
        )
        VALUES (%s, %s, %s)
    """

    values = (
        data.get("user_name"),
        data.get("user_email"),
        password_hash
    )

    cursor.execute(sql, values)

    con.commit()

    user_id = cursor.lastrowid

    cursor.close()
    con.close()

    return user_id


def get_user_by_email(user_email):
    con = get_db_connection()

    if con is None:
        return None
    cursor = con.cursor(dictionary=True)

    sql = """
        SELECT
           user_id,
           user_name,
           user_email,
           user_password_hash
        FROM users
        WHERE user_email = %s

    """
    cursor.execute(sql, (user_email,))

    user = cursor.fetchone()

    cursor.close()
    con.close()

    return user