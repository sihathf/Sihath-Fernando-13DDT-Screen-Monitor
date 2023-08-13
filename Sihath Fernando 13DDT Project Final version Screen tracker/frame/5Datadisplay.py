import matplotlib.pyplot as plt  # Importing matplotlib for plotting graphs
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, PhotoImage
import subprocess
import sys

# Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable

def open_page3():
    """Function to destroy the current GUI and open another page"""
    root.destroy()
    subprocess.Popen([PYTHON_EXECUTABLE, "frame/3home.py"])

def show_graph():
    """Function to display a bar graph of tracked application data"""
    apps = []
    Time = []
    file = open("textfiles/tracked_applications.txt", "r")
    data = file.read().splitlines()
    for i in data:
        brakedata = i.split(": ")
        apps.append(brakedata[0])
        Time.append(int(brakedata[1]))
    file.close()

    plt.bar(apps, Time)
    plt.xlabel("Apps")
    plt.ylabel("Time(Minutes MMM)")
    plt.show()

# Initialize the main GUI window
root = Tk()
root.title("13DDT Project")
root.configure(bg="white")
root.geometry('350x500+300+200')
root.resizable(0, 0)

click_homebutton = PhotoImage(file=r"images/hometitle.PNG")
click_homebutton = click_homebutton.subsample(2)
start_button = Button(root, image=click_homebutton, borderwidth=5, background="white", bd=0, command=open_page3)
start_button.grid()

label = Label(root, text="Data", fg="black", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
label.grid()

label_datainfo = Label(root, text="Data and Information", fg="black", bg="white", font=("Microsoft Yahei UI Light", 15, "bold"))
label_datainfo.grid(row=1, column=0)

label_tracked = Label(root, text="Apps that get tracked:", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_tracked.grid(row=4, column=0)

# Labels for tracked applications
label_chrome = Label(root, text="Chrome", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_chrome.grid(row=5, column=0)

label_spotify = Label(root, text="Spotify", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_spotify.grid(row=6, column=0)

label_zoom = Label(root, text="Zoom", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_zoom.grid(row=7, column=0)

label_discord = Label(root, text="Discord", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_discord.grid(row=8, column=0)

label_minecraft = Label(root, text="Minecraft", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_minecraft.grid(row=9, column=0)

label_minecraft = Label(root, text="Press the graph to display tracked time:", fg="black", bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
label_minecraft.grid(row=9, column=0)

# Button to show the graph
graph_button = Button(root, text="Show Graph", bg="#57a1f8", fg="white", border=0, command=show_graph, width=39, pady=7)
graph_button.grid(row=10, column=0)

# Start the GUI event loop
root.mainloop()
