from tkinter import *

window = Tk()

def handle_keypress(event):
    # Print the character associated to the key pressed
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()