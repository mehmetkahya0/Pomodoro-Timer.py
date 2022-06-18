#Create Pomodoro timer with a countdown timer and a stopwatch on the same screen with Tkinter
# Mehmet Kahya - 18.06.2022 - Python 3.8.2 - Tkinter - Pomodoro Timer  

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Label, Entry, StringVar, IntVar, Tk, ttk
from tkinter import filedialog
import time
import datetime

#Create tkinter window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("280x200")

#Create today total pomodoro count
today_total_pomodoro_count = []

#Create a label to display the time
time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 30))
time_label.pack()

timer = None
pomodoro_length = 60 * 25
stop_length = 60 * 5
stop_time = None

def timer():
    global start_time
    global stop_time
    if start_time is not None:
        #Calculate the time since start_time
        time_since_start = time.time() - start_time
        #Calculate the time left
        time_left = pomodoro_length - time_since_start
        #Convert time left to a string
        time_left_string = str(datetime.timedelta(seconds=time_left))
        #Display the time left
        time_label.config(text=time_left_string)
        #Call the timer again after 1 second
        root.after(1000, timer)
    elif stop_time is not None:
        #Calculate the time since stop_time
        time_since_stop = time.time() - stop_time
        #Calculate the time left
        time_left = stop_length - time_since_stop
        #Convert time left to a string
        time_left_string = str(datetime.timedelta(seconds=time_left))
        #Display the time left
        time_label.config(text=time_left_string)
        #Call the timer again after 1 second
        root.after(1000, timer)

    if time_left <= 0:
        reset_timer()
        messagebox.showinfo("Pomodoro Timer", "Pomodoro completed!")
        print("Pomodoro completed!")
        today_total_pomodoro_count.append(1)
        print(len(today_total_pomodoro_count))
        total = len(today_total_pomodoro_count)
        #total pomodoro count label
        total_pomodoro_count_label = ttk.Label(root, text="Total Pomodoro Count: {}".format(total))
        total_pomodoro_count_label.place(x=10, y=50)

#Create functions
def start_timer():
    global start_time
    start_time = time.time()
    timer()

def stop_timer():
    global start_time
    start_time = None

def reset_timer():
    global start_time
    start_time = None
    stop_time = None
    time_label.config(text="00:00:00")


#Create a frame for the timer
timer_frame = ttk.Frame(root, padding="3 3 12 12")
timer_frame.pack(side="top", fill="both", expand=True)
timer_frame.columnconfigure(0, weight=1)
timer_frame.rowconfigure(0, weight=1)

#Create variables
current_time = tk.StringVar()
current_time.set("00:00:00")
current_time_stopwatch = tk.StringVar()
current_time_stopwatch.set("00:00:00")
current_time_pomodoro = tk.StringVar()
current_time_pomodoro.set("00:00:00")
current_time_pomodoro_stopwatch = tk.StringVar()
current_time_pomodoro_stopwatch.set("00:00:00")

# Create Buttons and Labels
button_start = ttk.Button(root, text="Start", command=start_timer)
button_start.pack(side="left")

button_stop = ttk.Button(root, text="Stop", command=stop_timer)
button_stop.pack(side="left")

button_reset = ttk.Button(root, text="Reset", command=reset_timer)
button_reset.pack(side="left")


root.mainloop()