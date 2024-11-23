import tkinter as tk
from tkinter import messagebox

def ask_yes_no():
    result = messagebox.askyesno("Yes/No", "Do You Wish To Cancel This Process")
    
root = tk.Tk()
button = tk.Button(root, text= "Show Error", command= ask_yes_no)
button.pack()
root.mainloop()