import tkinter as tk
from tkinter import messagebox
def ask_ok_cancel():
    result = messagebox.askokcancel("Conforamtion", "Are You Sure You Wanna Cancel The Process?")
    if result:
        print("User Clicked Ok")
    else:
        print("User Clicked Cancel")

root = tk.Tk()
button = tk.Button(root, text= "Show Error", command= ask_ok_cancel)
button.pack()
root.mainloop()