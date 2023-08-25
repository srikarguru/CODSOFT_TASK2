import tkinter as tk
from math import sqrt, factorial
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)


def button_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def button_operator(operator):
    global first_number
    global operation
    first_number = float(entry.get())
    operation = operator
    entry.delete(0, tk.END)
    entry.insert(tk.END, operator)

def button_equal():
    global first_number
    result = None
    if operation == "+":
        second_number = float(entry.get())
        result = first_number + second_number
    elif operation == "-":
        second_number = float(entry.get())
        result = first_number - second_number
    elif operation == "*":
        second_number = float(entry.get())
        result = first_number * second_number
    elif operation == "/":
        second_number = float(entry.get())
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    elif operation == "√":
        result = sqrt(first_number)
    elif operation == "!":
        result = factorial(int(first_number))
    else:
        result = "Invalid operation"
    entry.delete(0, tk.END)
    entry.insert(tk.END, "=" + str(result))
    entry.config(state=tk.DISABLED)


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the entry field
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# Create the number buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# Create the operator buttons
button_add = tk.Button(window, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=lambda: button_operator("-"))
button_multiply = tk.Button(window, text="*", padx=41, pady=20, command=lambda: button_operator("*"))
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=lambda: button_operator("/"))
button_decimal = tk.Button(window, text=".", padx=42, pady=20, command=lambda: button_click("."))
button_square_root = tk.Button(window, text="√", padx=40, pady=20, command=lambda: button_operator("√"))
button_factorial = tk.Button(window, text="!", padx=40, pady=20, command=lambda: button_operator("!"))
button_backspace = tk.Button(window, text="<-", padx=36, pady=20, command=button_backspace)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_decimal.grid(row=4, column=1)
button_square_root.grid(row=1, column=4)
button_factorial.grid(row=2, column=4)
button_backspace.grid(row=3, column=4)
# Create the utility buttons
button_clear = tk.Button(window, text="C", padx=38, pady=20, command=button_clear)
button_equal = tk.Button(window, text="=", padx=87, pady=20, command=button_equal)

button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2, columnspan=2)

# Lock the screen from expanding
window.resizable(width=False, height=False)

# Run the GUI main loop
window.mainloop()
