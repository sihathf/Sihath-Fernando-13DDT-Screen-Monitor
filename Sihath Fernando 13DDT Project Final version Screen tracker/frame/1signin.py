from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess
import sys

# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable

# Function for the login button
def sign_up():
    """Function destroy home GUI and import login GUI"""
    root.destroy()
    # Open login.py using the Python interpreter
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/2siginup.py"])

def on_enter(e):
    user_entry.delete(0, "end")

def on_leave(e):
    name = user_entry.get()
    if name == "":
        user_entry.insert(0, "Username or Email ")

def open_page3():
    root.destroy()
    # Open login.py using the Python interpreter
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/3home.py"])

def login():
    entered_value = user_entry.get()
    entered_password = pass_entry.get()

    with open("textfiles/user_data.txt", "r") as file:
        for line in file:
            stored_data = line.strip().split(",")
            stored_email = stored_data[0]
            stored_username = stored_data[1]
            stored_password = stored_data[2]

            if (entered_value == stored_email or entered_value == stored_username) and entered_password == stored_password:
                messagebox.showinfo("Login", "Login successful!")
                open_page3()
                return
    messagebox.showerror("Login", "Invalid credentials")

# Initialise the main GUI window
root = Tk()
root.title("13DDT Project")
root.configure(bg="white")
root.geometry('850x500+300+200')
root.resizable(0, 0)
root.title('Login Page')

# Load and display an image using PhotoImage
side_img = PhotoImage(file=r"images\loginsidepage-removebg-preview_1_398x332.png")
side_img = side_img.subsample(1)
Label(root, image=side_img, bg="white").place(x=50, y=50)

# Create a frame for the GUI elements
frame1 = Frame(root, bg="white")
frame1.grid(row=0, column=0)

# Create widgets using StringVar to manage dynamic text
words2 = StringVar()
words3 = StringVar()

# Create another frame
frame1 = Frame(root, bg="white")
frame1.grid(row=0, column=0)

# Create a frame to hold the login components
frame0 = Frame(root, width=350, height=350, bg="white")
frame0.place(x=480, y=70)

# Create a heading label for the sign-in section
signinheading = Label(frame0, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
signinheading.place(x=100, y=5)

# Create an entry widget for the username or email
user_entry = Entry(frame0, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
user_entry.place(x=30, y=80)
user_entry.insert(0, "Username or Email")
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

# Create a horizontal line
Frame(frame0, width=295, height=2, bg="black").place(x=25, y=107)

# Define functions for handling focus events on password entry
def on_enter(e):
    pass_entry.delete(0, "end")

def on_leave(e):
    name = pass_entry.get()
    if name == "":
        pass_entry.insert(0, "Password ")

# Create an entry widget for the password
pass_entry = Entry(frame0, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
pass_entry.place(x=30, y=150)
pass_entry.insert(0, "Password")
pass_entry.bind("<FocusIn>", on_enter)
pass_entry.bind("<FocusOut>", on_leave)

# Create a horizontal line
Frame(frame0, width=295, height=2, bg="black").place(x=25, y=177)

# Create a button to initiate the login process
button1 = Button(frame0, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=login)
button1.place(x=35, y=204)

# Create a label and a button for signing up
label0 = Label(frame0, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label0.place(x=75, y=270)
sign_up = Button(frame0, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign_up)
sign_up.place(x=215, y=270)

# Start the GUI event loop
root.mainloop()
