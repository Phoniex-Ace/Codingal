import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("This Function Is Used To Display An Informative Message", "its the show info function")

root = tk.Tk()
button = tk.Button(root , text= "Show Info", command= show_info)
button.pack()
root.mainloop()