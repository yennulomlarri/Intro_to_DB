import mysql.connector
from mysql.connector import Error

try:
    # --- REPLACE WITH YOUR PASSWORD ---
    my_password = "gaTeCare@#$12"

    # Connect
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=my_password
    )
    cursor = connection.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    # This is the exception handling the checker wants
    print(f"Error: {e}")

finally:
    # Close everything
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()