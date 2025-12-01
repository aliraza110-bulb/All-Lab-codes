import tkinter as tk
from tkinter import messagebox

# Function to save password
def save_password():
    site = site_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if site and username and password:
        try:
            with open("passwords.txt", "a") as file:
                file.write(f"{site} | {username} | {password}\n")
            messagebox.showinfo("Success", "Password saved successfully!")
            
            # Clear entries
            site_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save password: {e}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields!")

# Main Window
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x250")
root.resizable(False, False)  # Prevent window resizing

# Labels and Entry Fields
tk.Label(root, text="Site:").pack(pady=(10, 0))
site_entry = tk.Entry(root, width=40)
site_entry.pack()

tk.Label(root, text="Username:").pack(pady=(10, 0))
username_entry = tk.Entry(root, width=40)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=(10, 0))
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

# Save Button
tk.Button(root, text="Save Password", width=20, command=save_password).pack(pady=15)

root.mainloop()
