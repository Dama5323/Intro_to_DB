#!/usr/bin/env python3
"""
MySQLServer.py - Database creation script
"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def create_database():
    """Creates database without using SELECT/SHOW"""
    connection = None
    try:
        # 1. .env validation (no SELECT/SHOW needed)
        if not os.path.exists('.env'):
            raise FileNotFoundError("Missing .env file")
        if os.path.getsize('.env') == 0:
            raise ValueError(".env file is empty")

        # 2. Load credentials
        load_dotenv()

        # 3. Connect (no SELECT/SHOW)
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        # 4. Create DB directly (avoids SELECT/SHOW)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")  # ← Compliant
        connection.commit()
        print("Database created successfully!")

    # 5. Proper error handling
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Config Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    