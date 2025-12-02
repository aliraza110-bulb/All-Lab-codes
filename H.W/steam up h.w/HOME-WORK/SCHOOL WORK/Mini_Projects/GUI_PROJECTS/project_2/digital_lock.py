import tkinter as tk
import time

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)

# Clock label
clock_label = tk.Label(
    root,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="cyan"
)
clock_label.pack(expand=True)

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

# Start the clock
update_time()

# Run the app
root.mainloop()
