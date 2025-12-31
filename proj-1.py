import tkinter as tk

def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def cal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.config(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),   # ✅ fixed font
    bg="#2d2d2d",
    fg="white",
    bd=0,
    width=19,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','C','+',
    '='
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

    tk.Button(root, text=button, width=5, height=2, command=action)\
        .grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
