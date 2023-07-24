import tkinter as tk
from tkinter import ttk, messagebox
import time
import datetime

# Create tkinter window
root = tk.Tk()
root.title("Pomodoro Timer🍅")
root.geometry("290x200")
root.resizable(False, False)

# Create today total pomodoro count
today_total_pomodoro_count = []

# Create a label to display the time
time_label = tk.Label(root, text="00:00:00", font=("SF pro", 30, "bold"))
time_label.pack()

pomodoro_length = 0
start_time = None
stop_time = None

def set_time():
    global pomodoro_length
    pomodoro_length = int(pomodoro_length_entry.get()) * 60
    print(f"Timer set {pomodoro_length} seconds ({pomodoro_length/60} minutes)")

def start_timer():
    global start_time
    start_time = time.time()
    timer()

def stop_timer():
    global start_time
    start_time = None

def reset_timer():
    global start_time, stop_time
    start_time = None
    stop_time = None
    time_label.config(text="00:00:00")

def timer():
    global start_time, stop_time, pomodoro_length
    if start_time is not None:
        time_since_start = time.time() - start_time
        time_left = max(0, pomodoro_length - time_since_start)
    elif stop_time is not None:
        time_since_stop = time.time() - stop_time
        time_left = max(0, stop_length - time_since_stop)

    # Format the time left as hours:minutes:seconds
    time_left_string = str(datetime.timedelta(seconds=time_left))
    # Remove milliseconds from the formatted string
    time_left_string = time_left_string.split(".")[0]
    time_label.config(text=time_left_string)

    if time_left <= 0:
        reset_timer()
        messagebox.showinfo("Pomodoro Timer", "Pomodoro completed!")
        print("Pomodoro completed!")
        today_total_pomodoro_count.append(1)
        total = len(today_total_pomodoro_count)
        total_pomodoro_count_label.config(text="Total Pomodoro Count: {}".format(total))

    root.after(1000, timer)

# Create a frame for the timer
timer_frame = ttk.Frame(root, padding="3 3 12 12")
timer_frame.pack(side="top", fill="both", expand=True)
timer_frame.columnconfigure(0, weight=1)
timer_frame.rowconfigure(0, weight=1)

# Create a label and entry to display the pomodoro length
pomodoro_length_label = ttk.Label(root, text="Pomodoro Length:", font=("SF pro", 12, "bold"))
pomodoro_length_label.place(x=10, y=55)

pomodoro_length_entry = ttk.Entry(root, width=8, font=("SF pro", 15, "bold"))
pomodoro_length_entry.place(x=120, y=50)

pomodoro_length_button = ttk.Button(root, text="Set", command=set_time)
pomodoro_length_button.place(x=190, y=50)

# Create Buttons and Labels
button_start = ttk.Button(root, text="Start", command=start_timer, width=3.5)
button_start.pack(side="left")

# button_break = ttk.Button(root, text="Break", width=3.5)
# button_break.pack(side="left")

button_stop = ttk.Button(root, text="Stop", command=stop_timer, width=3.5)
button_stop.pack(side="left")

button_reset = ttk.Button(root, text="Reset", command=reset_timer, width=3.5)
button_reset.pack(side="left")

total_pomodoro_count_label = ttk.Label(root, text="Total Pomodoro Count: 0", font=("SF pro", 15, "bold"))
total_pomodoro_count_label.place(x=10, y=80)

root.mainloop()
