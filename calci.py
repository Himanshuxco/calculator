import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Initialize the main window
root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

# Screen to display calculations
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=8, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# List of button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Creating buttons and placing them on the grid
row_val, col_val = 1, 0
for button_text in buttons:
    btn = tk.Button(root, text=button_text, font="Arial 20", padx=20, pady=20)
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val == 4:
        col_val = 0
        row_val += 1

root.mainloop()
