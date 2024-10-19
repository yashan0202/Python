import tkinter as tk
import random

# List of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown', 'White']

# Initial score and time left
score = 0
time_left = 30

# Function to start the game
def start_game(event):
    if time_left == 30:
        countdown()
    next_color()

# Function to display the next color
def next_color():
    global score
    global time_left

    # If time is still left
    if time_left > 0:
        # Make the entry box active
        entry.focus_set()

        # If the entered color is correct
        if entry.get().lower() == colors[1].lower():
            score += 1

        # Clear the entry box
        entry.delete(0, tk.END)

        # Randomly choose the next word and color
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))

        # Update the score label
        score_label.config(text="Score: " + str(score))

# Countdown timer function
def countdown():
    global time_left

    # If there's time left
    if time_left > 0:
        time_left -= 1
        time_label.config(text="Time left: " + str(time_left))
        time_label.after(1000, countdown)

# Create the main window
root = tk.Tk()
root.title("Color Game")
root.geometry("400x200")

# Instructions label
instructions = tk.Label(root, text="Type the color of the word, not the text!", font=('Helvetica', 12))
instructions.pack()

# Score label
score_label = tk.Label(root, text="Press Enter to start", font=('Helvetica', 12))
score_label.pack()

# Time left label
time_label = tk.Label(root, text="Time left: " + str(time_left), font=('Helvetica', 12))
time_label.pack()

# Color word label
label = tk.Label(root, font=('Helvetica', 50))
label.pack()

# Entry box for the player's answer
entry = tk.Entry(root)
entry.pack()

# Bind the Enter key to start the game
root.bind('<Return>', start_game)

# Start the GUI
root.mainloop()
