import time
import sqlite3 
import functools


# Empty cached query
query_cache = {}

# Leverage the Task 1 connection management.
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


# Global dictionary to store cached query results.
query_cache = {}

def cache_query(func):
    """
    A decorator that caches the results of a function based on a query string.
    It uses a global dictionary `query_cache` to store and retrieve results,
    preventing redundant database calls for the same query.

    The cache key is derived from:
    1. The 'query' keyword argument.
    2. The second positional argument (args[1]) if available.

    Args:
        func (callable): The function whose results are to be cached.
                        It's assumed this function takes a query string
                        either as a 'query' kwarg or its second arg.

    Returns:
        callable: The wrapped function with caching capabilities.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        # Determine the cache key from 'query' keyword arg or the second positional arg.
        cache_key = kwargs.get('query') or (args[1] if len(args) > 1 else None)

        # If the cache key is not valid (e.g., no query found), execute without caching.
        # Otherwise, check cache and store result if not found.
        if cache_key is None:
            return func(*args, **kwargs) # Execute directly if no valid cache key
        elif cache_key not in query_cache:
            query_cache[cache_key] = func(*args, **kwargs) # Cache result if not present
        return query_cache[cache_key] # Return cached result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


