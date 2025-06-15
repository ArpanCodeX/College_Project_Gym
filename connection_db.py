import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
import datetime 

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
            cursor.execute("SELECT password FROM users WHERE name = %s", (username,)) 
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

def insert_user(username, password):
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
            cursor.execute("SELECT id FROM users WHERE name = %s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Registration Error", "Username already exists. Please choose a different username.")
                return False
            create_time = datetime.datetime.now()
            cursor.execute("INSERT INTO users (name, password, create_time) VALUES (%s, %s, %s)", (username, password, create_time))
            conn.commit()
            return True
    except mysql.connector.Error as e:
        messagebox.showerror(
            "Database Error",
            "Failed to register user.\n\n"
            f"Error: {str(e)}"
        )
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()