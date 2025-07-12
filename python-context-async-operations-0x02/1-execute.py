import sqlite3

class ExecuteQuery:
    """
    This class-based context manager offers a reusable solution for executing SQL queries. 
    It automates SQLite database connection management, handles optional parameters, 
    and returns query results, all within a convenient with block.
    """
    def __init__(self, db_name: str, query: str, params: tuple=None):
        """
        Initializes the ExecuteQuery context manager.

        Args:
            query (str): The SQL query string to be executed.
            params (tuple, optional): A tuple of parameters to bind to the query. Defaults to None.
            db_name (str): The name of the SQLite database file. Defaults to 'users.db'.
        """
        self.query = query
        self.params = params if params is not None else ()
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Establishes a database connection, creates a cursor, executes the query,
        fetches all results, and returns them.
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall() # Return all fetched results

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the database cursor and connection upon exiting the 'with' block,
        regardless of whether an exception occurred.
        """
        if exc_type and exc_tb:
            print("Error Occurred:\n", exc_val)
            self.conn.close()
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            

