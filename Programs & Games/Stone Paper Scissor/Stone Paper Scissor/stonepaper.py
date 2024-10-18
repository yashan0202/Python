import random

def get_computer_choice():
    """Function to randomly choose between 'rock', 'paper', or 'scissors'."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """Function to get the user's choice and validate the input."""
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        choice = input("Enter your choice: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    """Function to determine the winner based on the rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Function to play the Stone, Paper, Scissors game."""
    print("Welcome to the Stone, Paper, Scissors game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Start the game
play_game()
