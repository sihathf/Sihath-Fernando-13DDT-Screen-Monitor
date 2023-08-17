from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
import subprocess
import sys

#Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable

#Function for the login button
def open_track():
    """Function destroy home GUI and import login GUI"""
    root.destroy()
    # Open login.py using the Python interpreter
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/4Track.py"])

def open_data():
    """Function destroy home GUI and import login GUI"""
    root.destroy()
    # Open login.py using the Python interpreter
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/5Datadisplay.py"])


# Create the main Tkinter window
root = Tk()

# Set the title of the window
root.title("13DDT Project")

# Configure the background color of the window
root.configure(bg="white")

# Set the dimensions and position of the window
root.geometry('300x500+300+200')

# Disable window resizing
root.resizable(0, 0)

# Load an image for the top of the GUI
image_top = PhotoImage(file=r"images\hometitle.PNG")
imagetop = image_top.subsample(2)

# Create a label to display the top image
labeltop = Label(root, image=imagetop, bg='white')
labeltop.grid(row=0, column=0)

# Load an image for a button
click_btn = Image.open(r"images\track.PNG")
click_btn = ImageTk.PhotoImage(click_btn)

# Create a button with the loaded image and a command
button = Button(root, image=click_btn, borderwidth=5, command=open_track)
button.grid(row=6, column=0, padx=10, pady=5)

# Load another image for a button
click_btn2 = Image.open(r"images\data.PNG")
click_btn2 = ImageTk.PhotoImage(click_btn2)

# Create another button with the loaded image and a command
button2 = Button(root, image=click_btn2, borderwidth=5, command=open_data)
button2.grid(row=12, column=0, padx=10, pady=5)





root.mainloop()
