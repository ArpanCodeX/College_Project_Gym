import tkinter as tk
from tkinter import messagebox
import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="gymDB_1"
    )

def show_table_columns():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SHOW COLUMNS FROM users")
    print("Columns in 'users' table:")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE name != 'admin'")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

def delete_user_from_db(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", (name,))
    conn.commit()
    conn.close()


def show_admin_dashboard():
    def delete_user(name):
        delete_user_from_db(name)
        messagebox.showinfo("Deleted", f"User '{name}' deleted.")
        dashboard.destroy()
        show_admin_dashboard()

    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("400x400")
    dashboard.configure(bg="white")

    tk.Label(dashboard, text="Admin - All Users", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    users = get_all_users()

    if not users:
        tk.Label(dashboard, text="No users available.", bg="white", fg="red", font=("Arial", 12)).pack(pady=20)

    for name in users:
        frame = tk.Frame(dashboard, bg="white")
        frame.pack(pady=5, padx=10, anchor="w")

        tk.Label(frame, text=name, font=("Arial", 12), bg="white").pack(side="left")
        tk.Button(frame, text="Delete", bg="#d9534f", fg="white",
                    command=lambda n=name: delete_user(n)).pack(side="left", padx=10)

    tk.Button(dashboard, text="Exit", command=dashboard.destroy, bg="gray", fg="white", font=("Arial", 12)).pack(pady=20)

    dashboard.mainloop()
