import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        # Get the input value in inches
        inches = float(inches_entry.get())
        
        # Convert inches to centimeters
        centimeters = inches * 2.54
        
        # Display the result
        result_label.config(text=f"{inches} inches = {centimeters:.2f} centimeters", fg="green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value.")

def clear_input():
    inches_entry.delete(0, tk.END)
    result_label.config(text="Enter length in inches to convert.", fg="black")

# Create the main Tkinter window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x200")

# Title label
title_label = tk.Label(root, text="Inches to Centimeters Converter", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

# Input field for inches
frame = tk.Frame(root)
frame.pack(pady=20)

inches_label = tk.Label(frame, text="Length in inches:", font=("Arial", 12))
inches_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
inches_entry = tk.Entry(frame, font=("Arial", 12))
inches_entry.grid(row=0, column=1, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert", font=("Arial", 12), command=convert_to_cm, width=12)
convert_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), command=clear_input, width=12)
clear_button.grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="Enter length in inches to convert.", font=("Arial", 12), pady=10, wraplength=350)
result_label.pack()

# Run the Tkinter application
root.mainloop()
