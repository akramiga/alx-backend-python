import sqlite3

class DatabaseConnection:
    """
    This class-based context manager automates reliable SQLite database connection management, 
    ensuring connections open and close properly within a with block, 
    even if errors occur.
    """
    def __init__(self, db_name: str):
        """
        Initializes the DatabaseConnection context manager.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None # Initialize connection to None

    def __enter__(self):
        """
        Establishes and returns a database connection when entering the 'with' block.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn # The connection object is returned and assigned to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the database connection when exiting the 'with' block.
        Handles any exceptions that occurred within the block.

        Args:
            exc_type (type): The type of exception (e.g., ValueError), or None if no exception.
            exc_val (Exception): The exception instance, or None.
            exc_tb (traceback): The traceback object, or None.
        """
        if self.conn:
            self.conn.close() # Ensure the connection is closed
            # print(f"Database connection to {self.db_name} closed.") # Optional: for debugging


