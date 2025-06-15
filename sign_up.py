from tkinter import *
from tkinter import messagebox
from connection_db import insert_user
from login import open_login

def open_signup():
    signup_window = Toplevel()
    signup_window.title("Sign Up Page")
    signup_window.state('zoomed')
    signup_window.configure(bg="#fff")

    def register():
        username = user.get()
        password_data = password.get()
        if username == "Username" or password_data == "Password":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if insert_user(username, password_data):
                messagebox.showinfo("Success", "Registration Successful!")
                signup_window.destroy()
                open_login()
            else:
                messagebox.showerror("Error", "Something went wrong. Try again.")

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

    def switch_to_login():
        signup_window.destroy()
        from login import open_login
        open_login()

    main_content_frame = Frame(signup_window, bg="white")
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

    heading = Label(form_frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 28, "bold"))
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

    Button(form_frame, width=45, pady=10, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=register).grid(row=5, column=0, pady=30, padx=50, sticky="ew")

    bottom_links_frame = Frame(form_frame, bg="white")
    bottom_links_frame.grid(row=6, column=0, pady=10, sticky="n")

    Label(bottom_links_frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10)).pack(side="left")

    Button(bottom_links_frame, width=8, text="Login", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=switch_to_login).pack(side="left", padx=5)

    signup_window.mainloop()