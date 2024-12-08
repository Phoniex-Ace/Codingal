import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        # Get input values (date, month, year)
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        # Get today's date
        today = datetime.today()
        
        # Create a datetime object for the date of birth
        dob = datetime(year, month, day)
        
        # Calculate age
        age = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1  # Adjust age if birthday hasn't occurred yet this year
        
        # Display the result
        result_label.config(text=f"Your age is: {age} years", fg="green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid date values.")

def clear_input():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    result_label.config(text="Enter your date of birth to calculate age.", fg="black")

# Create the main Tkinter window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x250")

# Title label
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

# Input fields for Date of Birth (Day, Month, Year)
frame = tk.Frame(root)
frame.pack(pady=10)

# Day input
day_label = tk.Label(frame, text="Day:", font=("Arial", 12))
day_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(frame, font=("Arial", 12), width=5)
day_entry.grid(row=0, column=1, pady=5)

# Month input
month_label = tk.Label(frame, text="Month:", font=("Arial", 12))
month_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(frame, font=("Arial", 12), width=5)
month_entry.grid(row=1, column=1, pady=5)

# Year input
year_label = tk.Label(frame, text="Year:", font=("Arial", 12))
year_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(frame, font=("Arial", 12), width=5)
year_entry.grid(row=2, column=1, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate Age", font=("Arial", 12), command=calculate_age, width=15)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), command=clear_input, width=15)
clear_button.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(root, text="Enter your date of birth to calculate age.", font=("Arial", 12), pady=10)
result_label.pack()

# Run the Tkinter application
root.mainloop()