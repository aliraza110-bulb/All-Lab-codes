"""
Simple To-Do List App
---------------------
Made with Tkinter (Python GUI)
Features:
✅ Add new tasks
✅ Delete selected task
✅ Clear all tasks
✅ Auto-save and load from 'tasks.txt'
"""

import tkinter as tk
from tkinter import messagebox

# ------------- Functions -------------

def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Empty Task", "Please enter a task first.")
        return
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# ------------- GUI Setup -------------

root = tk.Tk()
root.title("📝 Simple To-Do List")
root.geometry("350x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", width=10, command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Task", width=10, command=delete_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Clear All", width=10, command=clear_tasks).pack(side=tk.LEFT, padx=5)

# Task list
listbox = tk.Listbox(root, font=("Segoe UI", 12), height=15, selectmode=tk.SINGLE)
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Load tasks on start
load_tasks()

root.mainloop()


