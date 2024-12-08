import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def reset_game():
    result_label.config(text="Make your move!")

def exit_game():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Add a label for the game title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), pady=10)
title_label.pack()

# Add buttons for Rock, Paper, and Scissors
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), command=lambda: play_game("Rock"), width=10)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), command=lambda: play_game("Paper"), width=10)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), command=lambda: play_game("Scissors"), width=10)
scissors_button.grid(row=0, column=2, padx=10)

# Label to display results
result_label = tk.Label(root, text="Make your move!", font=("Arial", 16), pady=10)
result_label.pack()

# Add reset and exit buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=20)

reset_button = tk.Button(control_frame, text="Reset", font=("Arial", 14), command=reset_game, width=10)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(control_frame, text="Exit", font=("Arial", 14), command=exit_game, width=10)
exit_button.grid(row=0, column=1, padx=10)

# Run the main loop
root.mainloop()
