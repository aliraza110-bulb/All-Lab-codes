import tkinter as tk

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        
        # Example fixed exchange rates (for simplicity)
        rates = {
            "USD": 1,
            "EUR": 0.91,
            "PKR": 285,
            "JPY": 150
        }
        
        if from_curr in rates and to_curr in rates:
            converted = amount / rates[from_curr] * rates[to_curr]
            result_label.config(text=f"{amount} {from_curr} = {converted:.2f} {to_curr}")
        else:
            result_label.config(text="Invalid currency")
    except ValueError:
        result_label.config(text="Enter a valid amount")

# Main Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x200")

# Amount entry
tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# From currency
tk.Label(root, text="From Currency:").pack()
from_currency = tk.StringVar(root)
from_currency.set("USD")  # default value
tk.OptionMenu(root, from_currency, "USD", "EUR", "PKR", "JPY").pack()

# To currency
tk.Label(root, text="To Currency:").pack()
to_currency = tk.StringVar(root)
to_currency.set("EUR")  # default value
tk.OptionMenu(root, to_currency, "USD", "EUR", "PKR", "JPY").pack()

# Convert button
tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
