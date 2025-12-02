import tkinter as tk
from tkinter import messagebox

# =======================
# Data Storage
# =======================
products = {}
cart = {}

# =======================
# Functions
# =======================
def add_product():
    pid = entry_pid.get()
    name = entry_name.get()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid Price or Quantity")
        return

    if pid in products:
        messagebox.showerror("Error", "Product ID already exists!")
        return
    products[pid] = {"Name": name, "Price": price, "Quantity": quantity}
    messagebox.showinfo("Success", f"Product '{name}' added!")
    clear_entries()
    view_products()

def update_product():
    pid = entry_pid.get()
    if pid in products:
        name = entry_name.get()
        try:
            price = float(entry_price.get())
            quantity = int(entry_quantity.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Price or Quantity")
            return
        products[pid] = {"Name": name, "Price": price, "Quantity": quantity}
        messagebox.showinfo("Success", f"Product '{name}' updated!")
        clear_entries()
        view_products()
    else:
        messagebox.showerror("Error", "Product not found!")

def delete_product():
    pid = entry_pid.get()
    if pid in products:
        products.pop(pid)
        messagebox.showinfo("Deleted", f"Product '{pid}' deleted!")
        clear_entries()
        view_products()
    else:
        messagebox.showerror("Error", "Product not found!")

def add_to_cart():
    pid = entry_pid.get()
    try:
        qty = int(entry_quantity.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid Quantity")
        return
    if pid in products:
        if qty > products[pid]["Quantity"]:
            messagebox.showerror("Error", "Insufficient stock!")
            return
        if pid in cart:
            cart[pid]["Quantity"] += qty
        else:
            cart[pid] = {"Name": products[pid]["Name"], "Price": products[pid]["Price"], "Quantity": qty}
        products[pid]["Quantity"] -= qty
        messagebox.showinfo("Success", f"{qty} {products[pid]['Name']} added to cart!")
        view_products()
        view_cart()
    else:
        messagebox.showerror("Error", "Product not found!")

def remove_from_cart():
    pid = entry_pid.get()
    if pid in cart:
        products[pid]["Quantity"] += cart[pid]["Quantity"]
        cart.pop(pid)
        messagebox.showinfo("Removed", f"Product '{pid}' removed from cart")
        view_products()
        view_cart()
    else:
        messagebox.showerror("Error", "Product not in cart!")

def checkout():
    if cart:
        total = sum(info["Price"] * info["Quantity"] for info in cart.values())
        messagebox.showinfo("Checkout", f"Total Amount: ${total}\nOrder Placed Successfully!")
        cart.clear()
        view_cart()
        view_products()
    else:
        messagebox.showinfo("Cart Empty", "No items in cart!")

def view_products():
    list_products.delete(0, tk.END)
    for pid, info in products.items():
        list_products.insert(tk.END, f"ID:{pid} Name:{info['Name']} Price:${info['Price']} Stock:{info['Quantity']}")

def view_cart():
    list_cart.delete(0, tk.END)
    for pid, info in cart.items():
        list_cart.insert(tk.END, f"ID:{pid} Name:{info['Name']} Qty:{info['Quantity']} Subtotal:${info['Price']*info['Quantity']}")

def clear_entries():
    entry_pid.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# =======================
# GUI Setup
# =======================
root = tk.Tk()
root.title("E-Commerce Management System")
root.geometry("900x500")

# Frames
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

frame_products = tk.Frame(root)
frame_products.pack(side=tk.LEFT, padx=20)

frame_cart = tk.Frame(root)
frame_cart.pack(side=tk.RIGHT, padx=20)

# Input Fields
tk.Label(frame_input, text="Product ID").grid(row=0, column=0, padx=5)
entry_pid = tk.Entry(frame_input)
entry_pid.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Name").grid(row=0, column=2, padx=5)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=0, column=3, padx=5)

tk.Label(frame_input, text="Price").grid(row=1, column=0, padx=5)
entry_price = tk.Entry(frame_input)
entry_price.grid(row=1, column=1, padx=5)

tk.Label(frame_input, text="Quantity").grid(row=1, column=2, padx=5)
entry_quantity = tk.Entry(frame_input)
entry_quantity.grid(row=1, column=3, padx=5)

# Buttons
tk.Button(frame_buttons, text="Add Product", command=add_product).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update Product", command=update_product).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete Product", command=delete_product).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Add to Cart", command=add_to_cart).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Remove from Cart", command=remove_from_cart).grid(row=0, column=4, padx=5)
tk.Button(frame_buttons, text="Checkout", command=checkout).grid(row=0, column=5, padx=5)

# Product List
tk.Label(frame_products, text="Products").pack()
list_products = tk.Listbox(frame_products, width=60)
list_products.pack()

# Cart List
tk.Label(frame_cart, text="Shopping Cart").pack()
list_cart = tk.Listbox(frame_cart, width=60)
list_cart.pack()

# Start GUI
root.mainloop()
