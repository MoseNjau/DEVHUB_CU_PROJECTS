import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    if number in ["sin", "cos", "tan"]:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + number + "(")
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        if "^" in expression:
            expression = expression.replace("^", "**")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def perform_operation(operation):
    try:
        expression = entry.get()
        if "^" in expression:
            expression = expression.replace("^", "**")
        if operation == 5:
            result = eval(expression + "**2")
        elif operation == 6:
            result = math.sqrt(eval(expression))
        elif operation == 7:
            result = eval(expression + "**")
        elif operation == 8:
            result = math.factorial(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Enhanced Calculator")

entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sin", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("cos", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("tan", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("Clear", 4, 4),
    ("Square", 5, 0), ("√", 5, 1), ("^", 5, 2), ("!", 5, 3)
]

for (text, row, col) in buttons:
    if text != "Clear" and text != "=":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 12),
                           command=lambda t=text: button_click(t))
    elif text == "Clear":
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 12), command=clear)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, font=("Arial", 12), command=calculate)
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

math.sqrt(25)
