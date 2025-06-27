#!/usr/bin/env python3
"""
MySQLServer.py - Secure database creation script with proper error handling
"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def create_database():
    """Create the alx_book_store database with proper error handling"""
    connection = None
    try:
        # Load environment variables
        load_dotenv()
        
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:  # This catches mysql.connector.Error specifically
        print(f"\n[!] MySQL Error: {e}")
        print("Database creation failed. Check:")
        print("- MySQL service status")
        print("- Connection credentials in .env")
        print("- Network connectivity\n")
        
    except Exception as e:  # Catches other unexpected errors
        print(f"\n[!] Unexpected error: {e}")
        
    finally:
        # Proper resource cleanup
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()
