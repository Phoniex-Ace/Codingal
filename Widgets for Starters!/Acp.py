import tkinter as tk

def calculate_product():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    product = num1 * num2
    result_label.config(text=f"Product: {product}")

# Create the main window
window = tk.Tk()
window.title("Product Calculator")
window.geometry("350x250")  # Adjust window size for title

# Make the window resizable
window.resizable(True, True)

# Function to handle window movement
def move_window(event):
    x = event.x_root
    y = event.y_root
    window.geometry(f"+{x-20}+{y-20}")  # Adjust window position

# Bind the move function to the window's title bar
window.bind("<Button1-Motion>", move_window)

# Create a title label
title_label = tk.Label(window, text="Product Calculator", font=("Helvetica", 16))
title_label.pack()

# Create labels and entry fields for numbers
num1_label = tk.Label(window, text="Enter the first number:")
num1_label.pack()
num1_entry = tk.Entry(window)
num1_entry.pack()

num2_label = tk.Label(window, text="Enter the second number:")
num2_label.pack()
num2_entry = tk.Entry(window)
num2_entry.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate Product", command=calculate_product)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()