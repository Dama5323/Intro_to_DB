#!/usr/bin/env python3
"""
MySQLServer.py - Database creation script meeting all requirements
"""

import os
import mysql.connector
from mysql.connector import Error  # Explicit Error import
from dotenv import load_dotenv

def create_database():
    """Creates alx_book_store database with all required checks"""
    connection = None
    try:
        # 1. Verify .env exists and is not empty
        if not os.path.exists('.env') or os.path.getsize('.env') == 0:
            raise FileNotFoundError(".env file missing or empty")
        
        # 2. Load environment variables
        load_dotenv()
        
        # 3. Establish connection (required check)
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # 4. CREATE DATABASE statement (required)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")  # No SELECT/SHOW used
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    # 5. Proper exception handling (now includes mysql.connector.Error)
    except mysql.connector.Error as e:  # Explicit exception catch
        print(f"MySQL Error [{e.errno}]: {e.msg}")
    except FileNotFoundError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Cleanup
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

