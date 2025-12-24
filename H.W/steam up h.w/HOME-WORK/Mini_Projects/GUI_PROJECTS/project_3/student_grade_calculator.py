import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    name = name_entry.get().strip()
    score_text = score_entry.get().strip()
    
    if not name:
        messagebox.showerror("Error", "Please enter the student's name.")
        return

    try:
        score = float(score_text)
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")

        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        # Update the result label
        result_label.config(text=f"{name} - Score: {score} - Grade: {grade}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number (0-100) for score.")

# Create main window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("400x250")
root.resizable(False, False)

# Using frames for better layout
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Student Name:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="e")
name_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Score (0-100):", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
score_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
score_entry.grid(row=1, column=1, pady=5)

tk.Button(root, text="Calculate Grade", font=("Arial", 12), command=calculate_grade).pack(pady=10)

# Result label (button ke niche clearly show hoga)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="green")
result_label.pack(pady=10)

root.mainloop()
