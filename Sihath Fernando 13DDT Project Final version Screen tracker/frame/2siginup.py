from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys

#Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable

#Function for the login button
def sign_up():
    """Function destroy home GUI and import login GUI"""
    root.destroy()
    # Open login.py using the Python interpreter
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/1signin.py"])




# Initialize the main GUI window

root = Tk()
root.title("13DDT Project")
root.configure(bg="white")
root.geometry('850x500+300+200')
root.resizable(0, 0)


# Function to clear the Email entry when focused



def on_enter(e):
    Email_entry.delete(0, "end")

# Function to restore the default value to Email entry if left empty

def on_leave(e):
    name = Email_entry.get()
    if name == "":
        Email_entry.insert(0, "Email")

def on_enter_username(e):
    user_entry.delete(0, "end")

def on_leave_username(e):
    name = user_entry.get()
    if name == "":
        user_entry.insert(0, "Username")

def on_enter_password(e):
    passwrd_entry.delete(0, "end")

def on_leave_password(e):
    name = passwrd_entry.get()
    if name == "":
        passwrd_entry.insert(0, "Password")

def register_user():
    email = Email_entry.get()
    username = user_entry.get()
    password = passwrd_entry.get()

    if email and username and password:
        if "@" in email:
            if len(password) >= 8:
                # Add your code to save user data (write to file, database, etc.)
                with open("textfiles/user_data.txt", "a") as file:
                    file.write(f"{email},{username},{password}\n")
                messagebox.showinfo("Registration", "Registration successful!")
            else:
                messagebox.showerror("Error", "Password should have at least eight characters.")
        else:
            messagebox.showerror("Error", "Invalid email format")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


# Load and display an image for the GUI


side_img = PhotoImage(file=r"images\login.png")
side_img = side_img.subsample(1) 

Label(root, image=side_img, bg="white").place(x=50,y=50)

# Create a frame for the GUI elements


frame0=Frame(root,width = 350, height=420, bg="white")
frame0.place(x=480,y=70)
signinheading = Label(frame0,text= "Sign up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light",23,"bold"))
signinheading.place(x=100,y=5)

def on_enter(e):
  Email_entry.delete(0, "end")

def on_leave(e):
  name=Email_entry.get()
  if name=="":
    Email_entry.insert(0,"Email ")

# Entry widget for Email with focus management

Email_entry = Entry(frame0,width=25,fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light",11))
Email_entry.place(x=30,y=80)
Email_entry.insert(0,"Email")
Email_entry.bind("<FocusIn>",on_enter)
Email_entry.bind("<FocusOut>", on_leave)

Frame(frame0,width=295,height=2,bg="black").place(x=25, y=107)


def on_enter(e):
  user_entry.delete(0, "end")

def on_leave(e):
  name=user_entry.get()
  if name=="":
    user_entry.insert(0,"Username ")


# Entry widget for username with focus management


user_entry= Entry(frame0,width=25,fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light",11))
user_entry.place(x=30,y=150)
user_entry.insert(0,"Username")
user_entry.bind("<FocusIn>",on_enter)
user_entry.bind("<FocusOut>", on_leave)

# Horizontal line


Frame(frame0,width=295,height=2,bg="black").place(x=25, y=177)

def on_enter(e):
  passwrd_entry.delete(0, "end")

def on_leave(e):
  name=passwrd_entry.get()
  if name=="":
    passwrd_entry.insert(0,"Password ")
 

 # Entry widget for password with focus management

passwrd_entry= Entry(frame0,width=25,fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light",11))
passwrd_entry.place(x=30,y=220)
passwrd_entry.insert(0,"Password")
passwrd_entry.bind("<FocusIn>",on_enter)
passwrd_entry.bind("<FocusOut>", on_leave)

Frame(frame0,width=295,height=2,bg="black").place(x=25, y=247)

button1= Button(frame0,width=39,pady=7,text="Sign up", bg="#57a1f8",fg="white",border=0, command= register_user).place(x=35,y=280)

label0=Label(frame0,text = "I have an account", fg='black', bg='white',font=('Microsoft Yahei UI Light',9))
label0.place(x=90,y=340)
# Button to switch to the sign-up page

sign_up= Button(frame0,width=6,text="Sign in",border=0,bg="white",cursor="hand2",fg="#57a1f8", command=sign_up)
sign_up.place(x=200,y=340)


root.mainloop()
