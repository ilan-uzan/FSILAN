# What you will create
# Create a TicTacToe game in python, where two users can play together.
# tic-tac-toe
# # Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# Hint
# To do this project, you basically need to create four functions:
# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.
# Tips : Consider the following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

def display_board(board):
    print("\nWELCOME TO TIC TAC TOE")
    print(" ************* ")
    print(" * 1 | 2 | 3 * ")
    print(" *---|---|---* ")
    print(" * 4 | 5 | 6 * ")
    print(" *---|---|---* ")
    print(" * 7 | 8 | 9 * ")
    print(" ************* ")
    print("Current board:")
    print(" *-----------*")
    count = 1
    for row in board:
        row_display = []
        for cell in row:
            row_display.append(cell if cell != " " else str(count))
            count += 1
        print("  |  ".join(row_display))
        print(" *-----------*")
    print()

    

def player_input(player):
    while True:
        try :
            position = int(input(f"Player {player}, enter your position (1-9): "))
            if position < 1 or position > 9:
                print("Invalid position. Please enter a number between 1 and 9.")
                continue
            return position
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")  
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    display_board(board)
    player = "X"
    for _ in range(9):
        position = player_input(player)
        row = (position - 1) // 3
        col = (position - 1) % 3
        if board[row][col] != " ":
            print("Position already taken. Try again.")
            continue
        board[row][col] = player
        display_board(board)
        if check_win(board):
            print(f"Player {player} wins!")
            break
        player = "O" if player == "X" else "X"
    else:
        print("It's a tie!")
play()


    

