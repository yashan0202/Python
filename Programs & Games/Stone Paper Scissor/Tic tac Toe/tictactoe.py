def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    # Check rows, columns, and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                move = int(input("Enter a position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    play_game()
    
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game()
        else:
            print("Thanks for playing!")
            break