import mysql.connector
from mysql.connector import Error


def create_database():
    """ Connects to MySQL Server and creates the alx_book_store database """
    connection = None
    cursor = None  # <-- Add this line to initialize cursor
    try:
        # --- IMPORTANT: REPLACE WITH YOUR REAL MYSQL PASSWORD ---
        my_password = "gaTeCare@#$12"

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=my_password
        )
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Now, we check if the cursor was actually created before trying to close it
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == '__main__':
    create_database()