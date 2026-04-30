import tkinter as tk

# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x500")
root.configure(bg="black")

expression = ""

# Display
entry = tk.Entry(
    root,
    font=("Arial", 28),
    bd=0,
    bg="black",
    fg="white",
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# Functions
def press(key):
    global expression
    expression += str(key)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression, {"__builtins__": None}, {}))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Button Frame
frame = tk.Frame(root, bg="black")
frame.pack()

# Button creator
def create_button(text, bg, command):
    return tk.Button(
        frame,
        text=text,
        font=("Arial", 16),
        fg="white",
        bg=bg,
        activebackground="#444",
        bd=0,
        width=5,
        height=2,
        command=command
    )

# Layout
buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0','0', '.', '=']
]

colors = {
    "num": "#2e2e2e",
    "op": "#ff9500",
    "top": "#a5a5a5",
    "equal": "#00c853"
}

# Create buttons
for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        col_index = 0

        if btn == "0" and c == 1:
            continue

        if btn == "C":
            b = create_button(btn, colors["top"], clear)

        elif btn == "⌫":
            b = create_button(btn, colors["top"], backspace)

        elif btn == "=":
            b = create_button(btn, colors["equal"], calculate)

        elif btn in ['+', '-', '*', '/', '%']:
            b = create_button(btn, colors["op"], lambda x=btn: press(x))
        

        else:
            b = create_button(btn, colors["num"], lambda x=btn: press(x))

        # Make 0 double width
        if btn == "0" and c == 0:
            b.grid(row=r, column=c, columnspan=3, sticky="we", padx=6, pady=6)
            col_index +=2
        else:
            b.grid(row=r, column=c+ (1 if btn != "0" and c > 0 else 0), padx=6, pady=6)
            col_index +=1

# Keyboard Support
def key_input(event):
    key = event.char

    if key in "0123456789+-*/.%":
        press(key)

    elif key == "\r":  # Enter
        calculate()

    elif key == "\x08":  # Backspace
        backspace()

root.bind("<Key>", key_input)

root.mainloop()