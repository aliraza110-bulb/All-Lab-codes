"""
Simple Endless Calculator GUI

Save this file as `endless_calculator.py` and run with:
    python endless_calculator.py

Features:
- Easy-to-use GUI with buttons for numbers and operators
- Endless calculation (continue using result after '=')
- Clear (C) and Backspace (⌫)
"""

import tkinter as tk

# Simple Endless Calculator
def run_calculator():
    root = tk.Tk()
    root.title("Endless Calculator")

    expression = ""

    # Display box
    display = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=4, relief='ridge', justify='right')
    display.grid(row=0, column=0, columnspan=4, pady=10)

    def press(key):
        nonlocal expression
        if key == '=':
            try:
                result = str(eval(expression))
                display.delete(0, tk.END)
                display.insert(tk.END, result)
                expression = result
            except:
                display.delete(0, tk.END)
                display.insert(tk.END, 'Error')
                expression = ''
        elif key == 'C':
            expression = ''
            display.delete(0, tk.END)
        elif key == '⌫':
            expression = expression[:-1]
            display.delete(0, tk.END)
            display.insert(tk.END, expression)
        else:
            expression += str(key)
            display.delete(0, tk.END)
            display.insert(tk.END, expression)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('⌫', 5, 1)
    ]

    for (text, r, c) in buttons:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: press(t)).grid(row=r, column=c, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    run_calculator()
