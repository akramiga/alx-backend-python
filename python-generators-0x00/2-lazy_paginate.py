import mysql.connector
from mysql.connector import Error

def paginate_users(page_size, offset):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='akram12345',  # Use your own password
            database='ALX_prodev'
        )

        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results  # A list of user dictionaries

    except Error as e:
        print(f"Error: {e}")
        return []  # Return empty list on failure

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page  
        offset += page_size
