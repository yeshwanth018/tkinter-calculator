import tkinter as tk
import math

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def cal():
    try:
        expr = entry.get()

        # Replace scientific symbols/functions
        expr = expr.replace("^", "**")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("log", "math.log10")

        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.config(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    width=22,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=10)

buttons = [
    '7','8','9','/','sqrt',
    '4','5','6','*','^',
    '1','2','3','-','(',
    '0','.','C','+',
    ')','sin','cos','tan',
    'log','π','='
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        action = clear
    elif button == '=':
        action = cal
    else:
        action = lambda x=button: press(x)

    tk.Button(
        root,
        text=button,
        width=5,
        height=2,
        font=("Segoe UI", 11),
        command=action
    ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
