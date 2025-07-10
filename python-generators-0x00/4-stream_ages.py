import mysql.connector
from mysql.connector import Error

def stream_user_ages():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='akram12345',
            database='ALX_prodev'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row[0]  # row is a tuple like (age,), so row[0] gives the actual age

        cursor.close()
        connection.close()

    except Error as e:
        print(f" Error: {e}")


def compute_average_age():
    total = 0
    count = 0

    for age in stream_user_ages():  
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No user data found.")

