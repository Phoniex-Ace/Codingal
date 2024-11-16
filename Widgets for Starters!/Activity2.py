# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)
lbl.pack(pady=10)  # Ensure the label is displayed with some padding

# Add Label for getting name as input from user
name_lbl = Label(text="Full Name", bg="#3895D3", fg="white")
name_lbl.pack(pady=5)  # Display the label with padding
name_entry = Entry()
name_entry.pack(pady=5)  # Ensure the entry widget is displayed

# Add a Text Widget to display information/messages
text_box = Text(height=5, width=50)
text_box.pack(pady=10)  # Ensure the text box is displayed with some padding

# Function to display a Message
def display():
    # Read input given by user
    name = name_entry.get()

    # Declare a global variable to make it accessible anywhere in the program
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name + "\n"

    # Display details in the text box
    text_box.delete('1.0', END)  # Clear any previous content in the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))

# Add button and assign the display function to its command
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")
btn.pack(pady=10)  # Ensure the button is displayed with padding

# Run the application
root.mainloop()
