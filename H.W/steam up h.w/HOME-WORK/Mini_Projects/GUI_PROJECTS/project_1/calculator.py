import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=25, font=("Arial", 18))
entry.pack(pady=10)

def btn_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

frame = tk.Frame(root)
frame.pack()

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for btn in buttons:
    action = lambda x=btn: btn_click(x) if x != "=" else calculate()
    tk.Button(frame, text=btn, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Clear", width=20, height=2, font=("Arial", 14),
          command=clear).pack(pady=10)

root.mainloop()
