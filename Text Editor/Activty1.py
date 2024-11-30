import tkinter as tk
from tkinter import filedialog

# Setup Root Window
window = tk.Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")

# Adjust weight for responsive resizing
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)  # Column weight needed for buttons

# Function to Open a File
def open_file():
    """Open a file for editing."""
    filepath = filedialog.askopenfilename(
        title="Open File",  # Clearer dialog title
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    try:
        # Clear text widget before loading new content
        txt_edit.delete(1.0, tk.END)

        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
    except FileNotFoundError:
        # Handle file not found error gracefully
        message = "Error: File not found."
        show_error_message(message)  # Call a function to display error message

    # Update window title with filename
    window.title(f"Codingal's Text Editor - {filepath}")

# Function to display error messages
def show_error_message(message):
    error_window = tk.Tk()
    error_window.title("Error")
    error_label = tk.Label(error_window, text=message)
    error_label.pack()
    error_window.mainloop()  # Run the error window

# Function to Save the File
def save_file():
    """Save the current text to a new file."""
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    try:
        # Read text from editor
        text = txt_edit.get(1.0, tk.END)

        with open(filepath, "w") as output_file:
            output_file.write(text)
    except (IOError, OSError) as e:  # Catch broader file I/O errors
        message = f"Error saving file: {e}"
        show_error_message(message)

    # Update window title with filename
    window.title(f"Codingal's Text Editor - {filepath}")

# Text Editing Area
txt_edit = tk.Text(window)
txt_edit.pack(fill=tk.BOTH, expand=True)

# Button Frame and Buttons
fr_buttons = tk.Frame(window)  # Removed unnecessary relief and bd
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_open.pack(side=tk.LEFT, padx=5, pady=5)  # Add padding for better spacing
btn_save.pack(side=tk.LEFT, padx=5, pady=5)
fr_buttons.pack(fill=tk.X, padx=5, pady=5)  # Add padding to the frame

# Start the main event loop
window.mainloop()