from tkinter import *
from tkinter import messagebox
from connection_db import insert_user

def open_signup():
    signup_window = Tk()
    signup_window.title("Sign Up Page")
    signup_window.geometry("925x500+300+200")
    signup_window.configure(bg="#fff")
    signup_window.resizable(False, False)

    def register():
        username = user.get()
        password_data = password.get()
        if username == "Username" or password_data == "Password":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if insert_user(username, password_data):
                messagebox.showinfo("Success", "Registration Successful!")
                signup_window.destroy()
                from login import open_login
                open_login()
            else:
                messagebox.showerror("Error", "Username already exists.")

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

    img = PhotoImage(file="login.png")
    Label(signup_window, image=img, bg="white").place(x=50, y=50)

    frame = Frame(signup_window, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", enter)
    user.bind("<FocusOut>", leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    password = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    password.place(x=30, y=150)
    password.insert(0, "Password")
    password.bind("<FocusIn>", enterP)
    password.bind("<FocusOut>", leaveP)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    Button(frame, width=39, pady=7, text="Sign Up", bg="#57a1f8", fg="white", border=0, command=register).place(x=35, y=204)

    Label(frame, text="Already have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=65, y=270)

    Button(frame, width=6, text="Login", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=switch_to_login).place(x=215, y=270)

    signup_window.mainloop()
