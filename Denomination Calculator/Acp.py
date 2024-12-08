import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = password_entry.get()
    
    # Strength evaluation
    if len(password) < 8:
        strength = "Weak"
        color = "red"
        message = "Weak: Password should be at least 8 characters long."
    elif not any(char.isdigit() for char in password):
        strength = "Weak"
        color = "red"
        message = "Weak: Include at least one number."
    elif not any(char.isupper() for char in password):
        strength = "Medium"
        color = "black"
        message = "Medium: Include at least one uppercase letter."
    elif not any(char.islower() for char in password):
        strength = "Medium"
        color = "black"
        message = "Medium: Include at least one lowercase letter."
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength = "Strong"
        color = "light green"
        message = "Strong: For even more strength, add special characters."
    else:
        strength = "Very Strong"
        color = "green"
        message = "Very Strong: Your password is secure!"
    
    # Display the result
    result_label.config(text=message, fg=color)

def clear_input():
    password_entry.delete(0, tk.END)
    result_label.config(text="Enter a password to check its strength.", fg="black")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Add a title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), pady=10)
title_label.pack()

# Input field for password
password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

# Button to check password strength
check_button = tk.Button(root, text="Check Strength", font=("Arial", 12), command=check_password_strength, width=15)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Enter a password to check its strength.", font=("Arial", 12), wraplength=350, pady=10)
result_label.pack()

# Clear button
clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_input, width=10)
clear_button.pack()

# Run the Tkinter event loop
root.mainloop()
