import mysql.connector
from mysql.connector import errorcode


def create_database():
    """Connects to MySQL server and creates the alx_book_store database."""
    conn = None  # Initialize conn to None
    cursor = None  # Initialize cursor to None
    try:
        # Replace with your MySQL connection details
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gaTeCare@#$12"
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Failed to connect to the database: {err}")
    finally:
        # Now, we check if the objects were successfully created before closing
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    create_database()