# signup.py
from tkinter import *
from tkinter import messagebox
from connection_db import insert_user  # Import the function to insert user data into the database

def open_signup(root):
    root.quit()
    # Create the Sign Up window
    signup = Toplevel(root)
    signup.title("Sign Up")
    signup.geometry("925x500+300+200")  # Set window size to match login window
    signup.config(bg="#ffffff")
    signup.resizable(False, False)  # Disable resizing

    img = PhotoImage(file="login.png")  # Ensure this image exists for consistency
    lbl = Label(signup, image=img, bg="#ffffff")
    lbl.place(x=50, y=50)

    frame = Frame(signup, width=350, height=350, bg="#ffffff")
    frame.place(x=480, y=60)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="#ffffff", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=100, y=5)

    # Username field
    user = Entry(frame, width=25, fg="#000000", bg="#ffffff", border=0, font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", lambda event: enter(event, user))
    user.bind("<FocusOut>", lambda event: leave(event, user))

    Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=107)

    # Password field
    password = Entry(frame, width=25, fg="#000000", bg="#ffffff", border=0, font=("Microsoft YaHei UI Light", 11))
    password.place(x=30, y=150)
    password.insert(0, "Password")
    password.bind("<FocusIn>", lambda event: enterP(event, password))
    password.bind("<FocusOut>", lambda event: leaveP(event, password))

    Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=177)

    # Submit Button to Register User
    def register():
        uname = user.get()
        pwd = password.get()

        if uname == "" or pwd == "":
            messagebox.showwarning("Empty Fields", "All fields are required.")
        else:
            # Insert user into the database
            insert_user(uname, pwd)
            messagebox.showinfo("Success", "User registered successfully!")
            signup.destroy()  # Close sign-up window after successful registration

    Button(frame, text="Register", width=42, pady=7, bg="#57a2f8", fg="#fff",
           activeforeground="#fff", border=0, font=("Microsoft YaHei UI Light", 9), command=register).place(x=25, y=215)

    # Link to go back to the login page
    login_button = Button(frame, text="Already have an account? Login", fg="#57a1f8", bg="#ffffff", cursor="hand2", border=0, command=signup.destroy)
    login_button.place(x=75, y=270)

    signup.mainloop()

def enter(event, entry):
    if entry.get() == "Username":
        entry.delete(0, END)

def leave(event, entry):
    if entry.get() == "":
        entry.insert(0, "Username")

def enterP(event, entry):
    if entry.get() == "Password":
        entry.delete(0, END)
        entry.config(show="*")

def leaveP(event, entry):
    if entry.get() == "":
        entry.insert(0, "Password")
        entry.config(show="")
