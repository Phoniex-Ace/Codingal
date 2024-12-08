import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get input values
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        
        # Calculate Simple Interest
        simple_interest = (principal * time * rate) / 100
        
        # Calculate Compound Interest
        compound_interest = principal * (pow((1 + rate / 100), time)) - principal
        
        # Display results
        result_label.config(
            text=f"Simple Interest: ₹{simple_interest:.2f}\nCompound Interest: ₹{compound_interest:.2f}",
            fg="green"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def clear_inputs():
    principal_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    result_label.config(text="Enter details to calculate interest.", fg="black")

# Create the main Tkinter window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

# Principal
principal_label = tk.Label(frame, text="Principal (₹):", font=("Arial", 12))
principal_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
principal_entry = tk.Entry(frame, font=("Arial", 12))
principal_entry.grid(row=0, column=1, pady=5)

# Time
time_label = tk.Label(frame, text="Time (years):", font=("Arial", 12))
time_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
time_entry = tk.Entry(frame, font=("Arial", 12))
time_entry.grid(row=1, column=1, pady=5)

# Rate of Interest
rate_label = tk.Label(frame, text="Rate of Interest (%):", font=("Arial", 12))
rate_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
rate_entry = tk.Entry(frame, font=("Arial", 12))
rate_entry.grid(row=2, column=1, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", font=("Arial", 12), command=calculate_interest, width=12)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), command=clear_inputs, width=12)
clear_button.grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="Enter details to calculate interest.", font=("Arial", 12), pady=10, wraplength=350)
result_label.pack()

# Run the application
root.mainloop()
