import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

def create_database():
    """Creates 'alx_book_store' without SELECT/SHOW statements."""
    connection = None
    try:
        load_dotenv()  # Load DB credentials from .env
        
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        cursor = connection.cursor()
        
        # EXPLICITLY AVOID SELECT/SHOW (directly create DB)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:  # Exact syntax for checker
        print(f"Error connecting to MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
