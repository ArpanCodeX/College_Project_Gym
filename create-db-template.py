import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="system"
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE gymDB_1")
print("Database 'gymDB_1' created successfully.")

cursor.close()
conn.close()