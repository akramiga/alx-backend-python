import sqlite3
import functools


def with_db_connection(func):
    """
    A decorator that automatically manages a SQLite database connection for the decorated function.

    It establishes a connection to 'users.db', passes this connection object
    as the first argument to the decorated function, and ensures the connection
    is closed upon the function's completion, regardless of success or failure.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db') 
        try:
            return func(conn, *args, **kwargs) 
        finally:
            conn.close() 
    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling 
if __name__ == "__main__":
    user = get_user_by_id(user_id=1)
    print(user)