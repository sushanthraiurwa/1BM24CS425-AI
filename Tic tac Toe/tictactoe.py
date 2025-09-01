def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return ' ' not in board

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    game_on = True

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X', Player 2 is 'O'.")
    print("Enter a number from 1-9 to place your move.")

    while game_on:
        print_board(board)
        try:
            position = int(input(f"Player {current_player}, choose your position (1-9): "))
            index = position - 1

            if 0 <= index < 9 and board[index] == ' ':
                board[index] = current_player

                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins! Congratulations!")
                    game_on = False
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    game_on = False
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This position is already taken or invalid. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tic_tac_toe()
