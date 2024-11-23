from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

#Function For Dipalying Warning Message
#This will be called once the button is clicked 
#messagebox.showwarning("Window Name", "Text to be Displayed")
def msg():
    messagebox.showwarning("Alert", "Stop Virus Found!")

button = Button(root, text= "Scan for Virus", command= msg)
button.place(x=40, y = 80)

root.mainloop()