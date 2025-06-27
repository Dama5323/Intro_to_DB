#!/usr/bin/env python3
"""
MySQLServer.py - Script to create alx_book_store database securely
"""

import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    try:
        # Load environment variables
        load_dotenv()
        
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if not exists (without using SHOW or SELECT)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        # Close the connection if it was established
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
