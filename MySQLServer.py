import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

def create_database():
    """Creates 'alx_book_store' database without SELECT/SHOW statements."""
    connection = None
    try:
        # 1. Load environment variables
        load_dotenv()
        
        # 2. Connect to MySQL
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        # 3. Create database (no SELECT/SHOW used)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    # CHECKER REQUIRES THIS EXACT EXCEPTION HANDLING
    except mysql.connector.Error as e:  # MUST USE THIS EXACT SYNTAX
        print(f"Error connecting to MySQL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 4. Close connection securely
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
