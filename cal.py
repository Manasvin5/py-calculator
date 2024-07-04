import tkinter as tk
from tkinter import ttk
# FUnctions
def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear_entry():
    entry.delete(0, tk.END)
def close_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("1280x720")
root.configure(bg="black")
root.resizable(True, True)
# entry widget
entry = ttk.Entry(root, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
entry.bind("<Return>", calculate)

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# placing buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, command=calculate, bg="#4682b4", fg="white", font=("Arial", 24), borderwidth=0)
    else:
        btn = tk.Button(root, text=button, command=lambda val=button: on_button_click(val), bg="#87cefa", fg="black", font=("Arial", 24), borderwidth=0)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_entry, bg="#ff4500", fg="white", font=("Arial", 24), borderwidth=0)
clear_button.grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Close button
close_button = tk.Button(root, text="Close", command=close_app, bg="red", fg="white", font=("Arial", 24), borderwidth=0)
close_button.grid(row=row, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):  
    root.grid_rowconfigure(i, weight=1)

# starting this
root.mainloop()

