# db.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",  
        database="gymdb"
    )

def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def insert_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, password, create_time) VALUES (%s, %s, NOW())", (username, password))
    conn.commit()
    conn.close()
