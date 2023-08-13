from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import time
import threading
import psutil
import tkinter as tk
from tkinter import messagebox

import subprocess
import sys




#Executing another python script with the same interpreter
PYTHON_EXECUTABLE = sys.executable


class track:
    def __init__(self):
        # Data to store tracking information
        self.lock = threading.Lock()  # Lock to ensure thread-safe access to data
        self.tracking_thread = None
        self.is_tracking = False
        self.paused_apps = {}

        # Create the GUI and the geometry

        self.root = Tk()
        self.root.title("Application Time Tracker")
        self.root.configure(bg="white")
        self.root.geometry('250x500+300+200')
        self.root.resizable(0, 0)

        def open_page3():
            self.root.destroy()
            subprocess.Popen([PYTHON_EXECUTABLE, "frame/3home.py"])

        # GUI 
        # home page button

        self.click_homebutton = PhotoImage(file=r"images\hometitle.PNG")
        self.click_homebutton = self.click_homebutton.subsample(2)
        self.start_button = tk.Button(self.root, image=self.click_homebutton,borderwidth=5, background="white", bd=0, command=open_page3)
        self.start_button.grid()

    

        self.label_track = Label(self.root, text="Start tracking", fg="black", bg="white", font=("Microsoft Yahei UI Light",23,"bold"))
        self.label_track.grid()

         # starting button 
        self.click_btn= PhotoImage(file=r"images\startbutton.PNG")
        self.click_btn = self.click_btn.subsample(4)
        self.start_button = tk.Button(self.root, image=self.click_btn,borderwidth=5, background="white", bd=0, command=self.start_tracking)
        self.start_button.place(x=21,y=130)

        # stopping button 

        self.click_btn2= PhotoImage(file=r"images\stopbutton.PNG")
        self.click_btn2 = self.click_btn2.subsample(4)         
        self.stop_button = tk.Button(self.root, image=self.click_btn2,borderwidth=5, background="white", bd=0, command=self.stop_tracking, state=tk.DISABLED)
        self.stop_button.place(x=20,y=230)

        
  


    def start_tracking(self):
        if not self.is_tracking:
        # Check if tracking is not already in progress

            self.is_tracking = True
    # Create and start a new thread for tracking time

            self.tracking_thread = threading.Thread(target=self.track_time)
            self.tracking_thread.daemon = True  # Allows the thread to be terminated when the main program exits
            self.tracking_thread.start()
            self.start_button.config(state=tk.DISABLED)
        # Enable the "Stop Tracking" button

            self.stop_button.config(state=tk.NORMAL)
        # Show an information message box indicating tracking has started

            messagebox.showinfo("Tracking Started", "Time tracking has been started.")


    def stop_tracking(self):
        if self.is_tracking:
            self.is_tracking = False
            self.tracking_thread.join()  # Wait for the tracking thread to finish
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            messagebox.showinfo("Tracking Stopped", "Time tracking has been stopped and reset.")

    def track_time(self):
        tracked_processes = {}  # To track processes that have been counted along with their start times
        max_tracking_time = 12 * 3600
        start_time = time.time()

        while self.is_tracking and time.time() - start_time <= max_tracking_time:
            running_processes = {}
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name']:
                    process_name = proc.info['name']
                    # Check if the process is in the list of tracked applications
                    if 'chrome.exe' in process_name.lower() or 'discord' in process_name.lower() or \
                            'minecraft.exe' in process_name.lower() or 'spotify.exe' in process_name.lower() or 'zoom.exe' in process_name.lower():
                        process_pid = proc.info['pid']
                        if psutil.pid_exists(process_pid):
                            if process_name not in tracked_processes:
                                tracked_processes[process_name] = time.time()  # Record the start time for new processes
                            running_processes[process_name] = int(time.time() - tracked_processes[process_name])

            # Write tracked application data to a file
            with self.lock:
                with open("textfiles/tracked_applications.txt", "w") as f:
                    for app, duration in running_processes.items():
                        f.write(f"{app}: {self.format_duration(duration)}\n")

            time.sleep(1)  # Wait for 1 second before checking again
    # the format of the textfile displaying in minutes 

    def format_duration(self, seconds):
        minutes = seconds // 60
        return "{:03d}".format(int(minutes))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    track = track()  
    track.run()











