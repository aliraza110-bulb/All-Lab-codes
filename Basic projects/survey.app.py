"""
survey_app.py
A simple beginner-friendly Survey GUI using Tkinter.

Features:
- Name, Age, Gender (radio), Interests (checkboxes)
- Satisfaction rating (1-5) and Comments
- Submit saves to responses.csv (appends; creates file if missing)
- View Responses opens a window showing saved CSV rows
- Easy to explain: input widgets -> collect -> save -> show

Run: python survey_app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

CSV_FILE = "responses.csv"
FIELDNAMES = ["Name", "Age", "Gender", "Interests", "Satisfaction", "Comments"]

# Ensure CSV header exists
def ensure_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

# Save a response dictionary to CSV
def save_response(data: dict):
    ensure_csv()
    with open(CSV_FILE, "a", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(data)

# Read all responses (returns list of dicts)
def read_responses():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# ---------- GUI ----------
class SurveyApp:
    def __init__(self, root):
        self.root = root
        root.title("Beginner Survey App")

        pad = 8
        frm = ttk.Frame(root, padding=pad)
        frm.grid(row=0, column=0, sticky="nsew")

        # Name
        ttk.Label(frm, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.name_var, width=30).grid(row=0, column=1, columnspan=2, sticky="w")

        # Age
        ttk.Label(frm, text="Age:").grid(row=1, column=0, sticky="w")
        self.age_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.age_var, width=10).grid(row=1, column=1, sticky="w")

        # Gender (radio)
        ttk.Label(frm, text="Gender:").grid(row=2, column=0, sticky="w")
        self.gender_var = tk.StringVar(value="Prefer not to say")
        genders = ["Male", "Female", "Other", "Prefer not to say"]
        for i, g in enumerate(genders):
            ttk.Radiobutton(frm, text=g, value=g, variable=self.gender_var).grid(row=2, column=1+i, sticky="w")

        # Interests (checkboxes)
        ttk.Label(frm, text="Interests:").grid(row=3, column=0, sticky="nw")
        self.interest_vars = {}
        interests = ["Programming", "Design", "Data Science", "Gaming", "Other"]
        for i, it in enumerate(interests):
            var = tk.BooleanVar()
            self.interest_vars[it] = var
            ttk.Checkbutton(frm, text=it, variable=var).grid(row=3+i//3, column=1 + (i % 3), sticky="w")

        # Satisfaction scale
        ttk.Label(frm, text="Satisfaction (1=low, 5=high):").grid(row=6, column=0, sticky="w")
        self.sat_var = tk.IntVar(value=4)
        sat_scale = ttk.Scale(frm, from_=1, to=5, orient="horizontal", variable=self.sat_var)
        sat_scale.grid(row=6, column=1, columnspan=2, sticky="we")

        # Comments
        ttk.Label(frm, text="Comments:").grid(row=7, column=0, sticky="nw")
        self.comments_txt = tk.Text(frm, width=40, height=5)
        self.comments_txt.grid(row=7, column=1, columnspan=2, pady=(0,6), sticky="w")

        # Buttons: Submit and View Responses
        ttk.Button(frm, text="Submit", command=self.on_submit).grid(row=8, column=1, sticky="e", padx=4, pady=4)
        ttk.Button(frm, text="View Responses", command=self.on_view).grid(row=8, column=2, sticky="w", padx=4, pady=4)

        # Make layout a bit nicer
        for c in range(3):
            frm.columnconfigure(c, weight=1)

    def on_submit(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        gender = self.gender_var.get()
        interests = [k for k, v in self.interest_vars.items() if v.get()]
        comments = self.comments_txt.get("1.0", tk.END).strip()
        satisfaction = int(self.sat_var.get())

        # Basic validation
        if not name:
            messagebox.showwarning("Validation", "Please enter your name.")
            return
        if age and not age.isdigit():
            messagebox.showwarning("Validation", "Please enter a valid numeric age (or leave blank).")
            return

        data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Interests": ";".join(interests),
            "Satisfaction": satisfaction,
            "Comments": comments
        }

        try:
            save_response(data)
            messagebox.showinfo("Thank you", "Your response has been saved.")
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save response: {e}")

    def clear_form(self):
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("Prefer not to say")
        for v in self.interest_vars.values():
            v.set(False)
        self.sat_var.set(4)
        self.comments_txt.delete("1.0", tk.END)

    def on_view(self):
        rows = read_responses()
        view = tk.Toplevel(self.root)
        view.title("Saved Responses")
        txt = tk.Text(view, width=80, height=20)
        txt.pack(fill="both", expand=True)
        if not rows:
            txt.insert(tk.END, "No responses yet.\n")
            return
        # Pretty-print CSV rows
        for i, r in enumerate(rows, start=1):
            txt.insert(tk.END, f"Response #{i}\n")
            for f in FIELDNAMES:
                txt.insert(tk.END, f"  {f}: {r.get(f,'')}\n")
            txt.insert(tk.END, "\n")

# Run the app
if __name__ == "__main__":
    ensure_csv()
    root = tk.Tk()
    try:
        style = ttk.Style(root)
        style.theme_use('clam')
    except: pass
    app = SurveyApp(root)
    root.mainloop()
