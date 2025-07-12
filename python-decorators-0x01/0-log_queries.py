import sqlite3
import functools
from datetime import datetime

def log_queries(func):
    """
    A decorator that logs SQL queries with a timestamp before they are executed.

    It attempts to identify the SQL query string from either:
    1. A keyword argument named 'query'.
    2. The first positional argument of the decorated function.

    If a query is found, it prints the current timestamp and the query string.
    """
   
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # trying to extract the query from keyword arguments or the first positional argument.
        
        query = kwargs.get('query') or (args[0] if args else None)

        if query: 
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] Executing SQL Query: {query}")

        
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#fetch users while logging the query
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)