import tkinter as tk
from tkinter import messagebox

def show_error():
    messagebox.showerror("This Is Used To display an error", "An error Occured")

root = tk.Tk()
button = tk.Button(root, text= "Show Error", command= show_error)
button.pack()
root.mainloop()