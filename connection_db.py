from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="gymDB_1"
    )

def check_user(username, password):
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="system",
            database="gymDB_1"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result:
                if result[0] == password:
                    return "success"
                else:
                    return "wrong_password"
            else:
                return "not_found"
    except mysql.connector.Error as e:
        messagebox.showerror(
            "Database Connection Error",
            "⚠️ Unable to connect to the MySQL database.\n\n"
            "Please make sure MySQL server is running.\n\n"
            f"Error: {str(e)}"
        )
        return "error"
    finally:
        if conn and conn.is_connected():
            conn.close()