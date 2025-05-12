from tkinter import *
from tkinter import messagebox

def open_dashboard():
    dashboard = Toplevel()
    dashboard.title("Gym Dashboard")
    dashboard.geometry("600x400")
    dashboard.config(bg="#f0f0f0")

    Label(dashboard, text="Welcome to the Gym Dashboard!", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333").pack(pady=40)
    Label(dashboard, text="Add here", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)

def call():
    
    new = str(user.get())
    passData = str(password.get())
    if new == "Username" or passData == "Password":
        if new == "Username":
            messagebox.showerror("Showerror", "Invalid Username")
        elif passData == "Password":
            messagebox.showerror("Showerror", "Invalid Password")
    elif new == "admin" and passData == "admin123":  # Example valid credentials
        messagebox.showinfo("Success", f"Welcome {new}!")
        root.withdraw()  # Hide login window
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

root = Tk()
root.title("Login Page For GYM")
root.configure(bg="#fff")
root.geometry("925x500+300+200")
root.resizable(False, False)

img = PhotoImage(file="login.png")  # Make sure this image exists
lbl = Label(root, image=img, bg="#ffffff")
lbl.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="#ffffff")
frame.place(x=480, y=60)

heading = Label(frame, text="GYM", fg="#57a1f8", bg="#ffffff", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg="#000000", bg="#ffffff", border=0, font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", enter)
user.bind("<FocusOut>", leave)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=107)

password = Entry(frame, width=25, fg="#000000", bg="#ffffff", border=0, font=("Microsoft YaHei UI Light", 11))
password.place(x=30, y=150)
password.insert(0, "Password")
password.bind("<FocusIn>", enterP)
password.bind("<FocusOut>", leaveP)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=177)

Button(frame, text="Sign in", width=42, pady=7, bg="#57a2f8", fg="#fff",
       activeforeground="#fff", border=0, font=("Microsoft YaHei UI Light", 9), command=call).place(x=25, y=215)

lable = Label(frame, text="Don't have an account?", fg="#000", bg="#fff", font=("Microsoft YaHei UI Light", 9))
lable.place(x=75, y=270)

sign_up = Button(frame, text="Sign Up", bg="#fff", fg="#57a1f8", cursor="hand2", border=0)
sign_up.place(x=215, y=270)

root.mainloop()
