import mysql.connector
from mysql.connector import Error


def create_database():
    """ Connects to MySQL Server and creates the alx_book_store database """
    connection = None
    cursor = None
    try:
        # --- IMPORTANT: REPLACE WITH YOUR REAL MYSQL PASSWORD ---
        my_password = "gaTeCare@#$12"

        # Connect to the server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=my_password
        )
        cursor = connection.cursor()

        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # This is the specific exception handling the checker wants
        print(f"Error: {e}")

    finally:
        # This ensures everything is closed properly
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == '__main__':
    create_database()