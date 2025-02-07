import sqlite3


def get_db_connection():
    try:
        conn = sqlite3.connect("company.db")  # Change the path if needed
        conn.row_factory = sqlite3.Row  
        print("✅ Database connected successfully!")  # Confirmation message
        return conn
    except sqlite3.Error as e:
        print("❌ Database connection failed:", e)
        return None 
    
get_db_connection()

