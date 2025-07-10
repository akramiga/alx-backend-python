"""
Database seeding script for ALX_prodev MySQL database.
Creates database, table, and populates with CSV data.
"""

import mysql.connector
from mysql.connector import Error
import csv
import uuid
import os


def connect_db():
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='',  
            
        )
        return connection
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
        
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='',  
            database='ALX_prodev',
            
        )
        return connection
            
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    
    try:
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX idx_user_id (user_id));
        """)
        connection.commit()
        
        print("Table user_data created successfully")
        cursor.close()
        
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()

        # Open the CSV file in read mode
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)  # Reads each row as a dictionary: {'user_id': ..., 'name': ..., etc.}

            for row in reader:
                # Check if user_id already exists in the table
                cursor.execute("SELECT * FROM user_data WHERE user_id = %s", (row['user_id'],))
                if cursor.fetchone():  # If any result is returned, skip this row
                    continue

                # Insert data into the table
                cursor.execute('''
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                ''', (
                    row['user_id'],   # UUID string
                    row['name'],      # Full name
                    row['email'],     # Email address
                    row['age']        # Age as decimal
                ))

        connection.commit()  # Save changes to database
        print(" Data inserted successfully")
        cursor.close()

    except Error as e:
        print(f" Error inserting data: {e}")



def stream_user_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_data")  # Get all rows

        while True:
            row = cursor.fetchone()  # fetch one row at a time
            if row is None:
                break               # if no more rows, exit loop
            yield row               # yield row to the caller
        cursor.close()
    except Error as e:
        print(f" Error streaming data: {e}")
