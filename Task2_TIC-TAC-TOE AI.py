import math

# Initialize empty board
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

# Check for winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(b[pos] == player for pos in condition) for condition in win_conditions)

# Check if the board is full
def is_draw(b):
    return ' ' not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        while True:
            try:
                human_move = int(input("Enter your move (1-9): ")) - 1
                if board[human_move] == ' ':
                    board[human_move] = 'X'
                    break
                else:
                    print("Cell already taken. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Enter a number between 1 and 9.")
        
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations! You win! 🎉")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time. 🤖")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
