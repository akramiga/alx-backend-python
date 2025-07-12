import time
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
            return func(conn, *args, **kwargs) # Pass connection as first argument and execute
        finally:
            conn.close() # Ensure connection is closed
    return wrapper


# Decorator for transaction management
def retry_on_failure(retries: int=3, delay: int=2):
    """
    A decorator factory that retries the decorated function a specified number of times
    if a sqlite3.Error occurs.

    Args:
        retries (int): The maximum number of times to retry the function (default: 3).
        delay (int): The delay in seconds between retries (default: 2).

    Returns:
        callable: A decorator that can be applied to a function.
    """
    def decorator_retry_on_failure(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs) # Attempt to execute the function
                except sqlite3.Error as e:
                    print(f"Attempt {attempt + 1}/{retries} failed with error: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay) # Wait before the next retry
            raise # Re-raise the last exception if all retries fail
        return wrapper
    return decorator_retry_on_failure


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# attempt to fetch users with automatic retry on failure
if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(users)