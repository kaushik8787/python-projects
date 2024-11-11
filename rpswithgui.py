import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to play a round
def play_round(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    # Update results and scores
    result_label.config(text=f"Computer chose: {computer_choice}")
    
    if result == "tie":
        result_label.config(text="It's a tie!")
    elif result == "user":
        result_label.config(text="You win this round!")
        user_score += 1
    else:
        result_label.config(text="Computer wins this round!")
        computer_score += 1
    
    # Update the score display
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="Make your choice to start!")

# Initializing main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x300")

# Scores
user_score = 0
computer_score = 0

# Title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Make your choice to start!", font=("Helvetica", 12))
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=20)

# Run the application
root.mainloop()
