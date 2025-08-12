

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (update credentials accordingly)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',       # Replace with your MySQL username
        password='Clyde@2025'  # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close connection properly
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
