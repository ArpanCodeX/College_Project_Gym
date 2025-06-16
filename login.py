from tkinter import *
from tkinter import messagebox
from connection_db import check_user
from dashboard import create_exercise_section
from admin import show_admin_dashboard

def open_login():
    login_window = Toplevel()
    login_window.title("Login Page")
    login_window.state('zoomed')
    login_window.configure(bg="#fff")

    def call():
        username = user.get()
        password_data = password.get()

        if username == "admin" and password_data == "0000":
            login_window.destroy()
            show_admin_dashboard()
        elif username == "Username" or password_data == "Password":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            result = check_user(username, password_data)
            if result == "success":
                messagebox.showinfo("Success", f"Welcome {username}!")
                login_window.destroy()
                open_dashboard()
            elif result == "wrong_password":
                messagebox.showerror("Error", "Incorrect password.")
            elif result == "not_found":
                messagebox.showerror("Error", "User does not exist.")
            else:
                messagebox.showerror("Error", "Unknown login error occurred.")

    def enter(event):
        if user.get() == "Username":
            user.delete(0, END)

    def leave(event):
        if user.get() == "":
            user.insert(0, "Username")

    def enterP(event):
        if password.get() == "Password":
            password.delete(0, END)
            password.config(show="*")

    def leaveP(event):
        if password.get() == "":
            password.insert(0, "Password")
            password.config(show="")

    def switch_to_signup():
        login_window.destroy()
        from sign_up import open_signup
        open_signup()

    main_content_frame = Frame(login_window, bg="white")
    main_content_frame.pack(expand=True, fill="both")

    img = PhotoImage(file="login.png")
    img_label = Label(main_content_frame, image=img, bg="white")
    img_label.pack(side="left", padx=20, pady=20)

    form_frame = Frame(main_content_frame, width=380, height=380, bg="white")
    form_frame.pack(side="left", expand=True, fill="both", padx=200, pady=120)

    form_frame.grid_rowconfigure(0, weight=1)
    form_frame.grid_rowconfigure(1, weight=1)
    form_frame.grid_rowconfigure(2, weight=0)
    form_frame.grid_rowconfigure(3, weight=1)
    form_frame.grid_rowconfigure(4, weight=0)
    form_frame.grid_rowconfigure(5, weight=1)
    form_frame.grid_rowconfigure(6, weight=1)
    form_frame.grid_columnconfigure(0, weight=1)

    heading = Label(form_frame, text="GYM", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 28, "bold"))
    heading.grid(row=0, column=0, pady=(20, 0), sticky="n")

    user = Entry(form_frame, width=40, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 14))
    user.grid(row=1, column=0, pady=(30, 0), padx=50, sticky="ew")
    user.insert(0, "Username")
    user.bind("<FocusIn>", enter)
    user.bind("<FocusOut>", leave)

    Frame(form_frame, width=350, height=2, bg="black").grid(row=2, column=0, padx=45, sticky="ew")

    password = Entry(form_frame, width=40, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 14))
    password.grid(row=3, column=0, pady=(30, 0), padx=50, sticky="ew")
    password.insert(0, "Password")
    password.bind("<FocusIn>", enterP)
    password.bind("<FocusOut>", leaveP)

    Frame(form_frame, width=350, height=2, bg="black").grid(row=4, column=0, padx=45, sticky="ew")

    Button(form_frame, width=45, pady=10, text="Sign In", bg="#57a1f8", fg="white", border=0, command=call).grid(row=5, column=0, pady=30, padx=50, sticky="ew")

    bottom_links_frame = Frame(form_frame, bg="white")
    bottom_links_frame.grid(row=6, column=0, pady=10, sticky="n")

    Label(bottom_links_frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10)).pack(side="left")
    Button(bottom_links_frame, width=8, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=switch_to_signup).pack(side="left", padx=5)

    login_window.mainloop()

def open_dashboard():
    dash = Toplevel()
    dash.state('zoomed')
    dash.title("Gym Management Dashboard")
    dash.configure(bg="green")

    title = Label(dash, text="🏋️‍♂️ Welcome to Gym Dashboard 🏋️‍♀️", font=("Helvetica", 24, "bold"), bg="#f0f4f7", fg="#333")
    title.pack(pady=20)

    exercise_section_frame = Frame(dash, bg="white", bd=2, relief="ridge")
    exercise_section_frame.pack(expand=True, fill="both", padx=50, pady=20)

    create_exercise_section(exercise_section_frame)

    exit_btn = Button(
        dash,
        text="Exit",
        command=dash.destroy,
        font=("Arial", 16, "bold"),
        bg="#dc3545",
        fg="white",
        padx=25,
        pady=12,
        relief="raised"
    )
    exit_btn.pack(pady=30)

    dash.mainloop()
