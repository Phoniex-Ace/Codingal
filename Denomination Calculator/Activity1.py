from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top,text="This Is A Top level Window")
    l2.pack()

    top.mainloop()

l = Label(root,text="This is a root window")
btn = Button(root,text= "Click Here To Open Another Window", command= topwin)
l.pack()
btn.pack()
root.mainloop()