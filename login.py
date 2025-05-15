from tkinter import *
from tkinter import messagebox
from connection_db import check_user
from dashboard import create_exercise_section

def open_login():
    login_window = Toplevel()
    login_window.title("Login Page")
    login_window.geometry("925x500+300+200")
    login_window.configure(bg="#fff")
    login_window.resizable(False, False)

    def call():
        username = user.get()
        password_data = password.get()
        if username == "Username" or password_data == "Password":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            if check_user(username, password_data):
                messagebox.showinfo("Success", f"Welcome {username}!")
                login_window.destroy()
                open_dashboard()
            else:
                messagebox.showerror("Error", "Incorrect Username or Password")

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

    img = PhotoImage(file="login.png")
    Label(login_window, image=img, bg="white").place(x=50, y=50)

    frame = Frame(login_window, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="GYM", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
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

    Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=call).place(x=35, y=204)

    Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)

    Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=switch_to_signup).place(x=215, y=270)

    login_window.mainloop()


def open_dashboard():
    dash = Toplevel()
    dash.geometry("900x600")
    dash.title("Gym Management Dashboard")
    dash.configure(bg="light green") 
 
 
    title = Label(dash, text="🏋️‍♂️ Welcome to Gym Dashboard 🏋️‍♀️", font=("Helvetica", 24, "bold"), bg="#f0f4f7", fg="#333")
    title.pack(pady=30)

     
    content_frame = Frame(dash, bg="white", bd=2, relief="ridge")
    content_frame.pack(fill="both", expand=True, padx=30, pady=20)

    
    create_exercise_section(content_frame)
