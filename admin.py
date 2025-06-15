import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="gymDB_1"
    )

def get_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, create_time FROM users WHERE name != 'admin'")
    users_data = cursor.fetchall()
    conn.close()
    return users_data

def delete_user_from_db(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", (name,))
    conn.commit()
    conn.close()

def show_admin_dashboard():
    def delete_user_action(name):
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user '{name}'? This action cannot be undone."):
            delete_user_from_db(name)
            messagebox.showinfo("Deleted", f"User '{name}' deleted successfully.")
            dashboard.destroy()
            show_admin_dashboard()

    dashboard = tk.Tk()
    dashboard.title("Admin Dashboard")
    dashboard.state('zoomed')
    dashboard.configure(bg="#f0f4f7")

    main_frame = tk.Frame(dashboard, bg="#f0f4f7")
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)

    main_frame.grid_rowconfigure(0, weight=0)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure(2, weight=0)
    main_frame.grid_columnconfigure(0, weight=1)

    tk.Label(main_frame, text="Admin Panel - Manage Users", font=("Arial", 28, "bold"), bg="#f0f4f7", fg="#333").grid(row=0, column=0, pady=20, sticky="n")

    users_list_container = tk.Frame(main_frame, bg="white", bd=2, relief="ridge")
    users_list_container.grid(row=1, column=0, sticky="nsew", padx=50, pady=20)

    canvas = tk.Canvas(users_list_container, bg="white")
    scrollbar = tk.Scrollbar(users_list_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=1)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_canvas_configure(event):
        canvas.itemconfig(canvas.find_withtag("all")[0], width=event.width)
    canvas.bind('<Configure>', _on_canvas_configure)

    users = get_all_users()

    if not users:
        tk.Label(scrollable_frame, text="No users available (excluding admin).", bg="white", fg="#555", font=("Arial", 16)).pack(pady=50, padx=20)
    else:
        header_frame = tk.Frame(scrollable_frame, bg="#e0e0e0", bd=1, relief="solid")
        header_frame.pack(fill="x", padx=10, pady=(10, 0))
        header_frame.grid_columnconfigure(0, weight=3)
        header_frame.grid_columnconfigure(1, weight=2)
        header_frame.grid_columnconfigure(2, weight=1)

        tk.Label(header_frame, text="Username", font=("Arial", 14, "bold"), bg="#e0e0e0", padx=10, pady=5).grid(row=0, column=0, sticky="w")
        tk.Label(header_frame, text="Creation Time", font=("Arial", 14, "bold"), bg="#e0e0e0", padx=10, pady=5).grid(row=0, column=1, sticky="w")
        tk.Label(header_frame, text="Actions", font=("Arial", 14, "bold"), bg="#e0e0e0", padx=10, pady=5).grid(row=0, column=2, sticky="w")

        for name, create_time in users:
            user_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="groove")
            user_frame.pack(fill="x", padx=10, pady=5)
            user_frame.grid_columnconfigure(0, weight=3)
            user_frame.grid_columnconfigure(1, weight=2)
            user_frame.grid_columnconfigure(2, weight=1)

            tk.Label(user_frame, text=name, font=("Arial", 14), bg="white", padx=10, pady=8).grid(row=0, column=0, sticky="w")

            formatted_time = create_time.strftime("%Y-%m-%d %H:%M:%S") if isinstance(create_time, datetime) else str(create_time)
            tk.Label(user_frame, text=formatted_time, font=("Arial", 12), bg="white", fg="#666", padx=10, pady=8).grid(row=0, column=1, sticky="w")

            tk.Button(user_frame, text="Delete", bg="#dc3545", fg="white", font=("Arial", 12, "bold"),
                      command=lambda n=name: delete_user_action(n)).grid(row=0, column=2, padx=10, pady=5, sticky="e")

    tk.Button(main_frame, text="Exit Dashboard", command=dashboard.destroy, bg="#007bff", fg="white",
              font=("Arial", 16, "bold"), padx=25, pady=12, relief="raised").grid(row=2, column=0, pady=30)

    dashboard.mainloop()
