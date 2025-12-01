import tkinter as tk
from tkinter import ttk, messagebox
import random, string

def generate_password():
    words = words_entry.get().strip().split()
    length = int(length_var.get())

    if len(words) < 2:
        messagebox.showwarning("Input Error", "Please enter at least 2 words separated by spaces.")
        return
    if not (8 <= length <= 20):
        messagebox.showwarning("Length Error", "Password length must be between 8 and 20.")
        return

    random.shuffle(words)
    base = "".join(words)
    characters = string.ascii_letters + string.digits + string.punctuation
    extra = "".join(random.choice(characters) for _ in range(max(0, length - len(base))))

    password = list(base + extra)
    random.shuffle(password)
    final_password = "".join(password)
    result_var.set(final_password)

def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# Update label when slider moves
def update_length_label(value):
    length_display.config(text=f"Selected Length: {int(float(value))}")

# ---------------- GUI SETUP ----------------
root = tk.Tk()
root.title("----- UNBREAKABLE PASSWORD GENERATOR -----")
root.geometry("420x430")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Title
ttk.Label(frame, text="🔐 UNBREAKABLE PASSWORD GENERATOR", font=("Segoe UI", 14, "bold")).pack(pady=15)

# Input box for words
ttk.Label(frame, text="Enter 2 or 3 words (separated by spaces):", font=("Segoe UI", 10)).pack(pady=5)
words_entry = ttk.Entry(frame, font=("Segoe UI", 12))
words_entry.pack(fill="x", padx=10, pady=5)

# Password length slider + label
length_var = tk.IntVar(value=12)
ttk.Label(frame, text="Select Password Length (8–20):", font=("Segoe UI", 10)).pack(pady=5)
length_slider = ttk.Scale(frame, from_=8, to=20, orient="horizontal", variable=length_var, command=update_length_label)
length_slider.pack(fill="x", padx=10, pady=5)

length_display = ttk.Label(frame, text="Selected Length: 12", font=("Segoe UI", 10, "italic"), foreground="gray")
length_display.pack(pady=5)

# Generate button
ttk.Button(frame, text="Generate Password 🔄", command=generate_password).pack(pady=15)

# Result box
result_var = tk.StringVar()
result_entry = ttk.Entry(frame, textvariable=result_var, font=("Segoe UI", 13), justify="center")
result_entry.pack(fill="x", padx=10, pady=10)

# Copy button
ttk.Button(frame, text="Copy Password 📋", command=copy_password).pack(pady=8)

# Tip / info label
ttk.Label(frame, text="💡 Each time you click Generate, you get a unique and strong password!",
          wraplength=350, foreground="gray", justify="center").pack(pady=15)

# Start the app
root.mainloop()
