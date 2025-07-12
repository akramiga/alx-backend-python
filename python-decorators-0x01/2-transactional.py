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
        conn = sqlite3.connect('users.db') # Establish connection
        try:
            return func(conn, *args, **kwargs) # Pass connection as first argument and execute
        finally:
            conn.close() # Ensure connection is closed
    return wrapper


# transaction management
def transactional(func):
    
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs) # Execute the wrapped function
            conn.commit() # Commit changes on success
            print("[TRANSACTION] Committed successfully.")
            return result
        except Exception as e:
            conn.rollback() # Rollback on error
            print(f"[TRANSACTION] Rolled back due to error: {e}")
            raise 
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


# Run update with automatic transaction handling
if __name__ == "__main__":
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')