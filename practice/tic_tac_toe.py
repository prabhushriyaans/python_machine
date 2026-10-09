import random
board = [" "] * 9

winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def check_winner():
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None


def minimax(is_maximizing):

    result = check_winner()

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "draw":
        return 0

    if is_maximizing:
        best_score = -999

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 999

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score

def nooby():
    while True:
        move=random.randint(0, 8)
        if board[move] == " ":
            return move

def best_move():

    best_score = -999
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def print_board():
    for i in range(3):
        for j in range(3):
            print(board[i*3+j], end=" ")
            if j<2:
                print("|", end=" ")
        if i<2:
            print("\n--+---+--")
    print()
       

print("Welcome to Tic Tac Toe!")
print("what level of AI do you want to play against?")
print("1. Nooby (Random Moves)")
print("2. Pro (Optimal Moves)")
ch=int(input("enter choice:(1/2) :"))
if ch==1:
  ai_move =  nooby()
elif ch==2:
  ai_move = best_move()
else:
  print("Invalid choice!.")
  ai_move =  nooby()
toss = random.randint(0, 1)

if toss == 0:
    while True:
        print_board()
        player_move = int(input("Enter position (0-8): "))

        while player_move < 0 or player_move > 8 or board[player_move] != " ":
            print("Invalid or occupied position! Try again.")
            player_move = int(input("Enter position (0-8): "))

        board[player_move] = "X"

        result = check_winner()
        if result == "X":
            print_board()
            print("Player wins!")
            break
        elif result == "O":
            print_board()
            print("AI wins!")
            break
        elif result == "draw":
            print_board()
            print("It's a draw!")
            break

        ai_move = nooby() if ch == 1 else best_move()
        board[ai_move] = "O"
        result = check_winner()
        if result == "X":
            print_board()
            print("Player wins!")
            break
        elif result == "O":
            print_board()
            print("AI wins!")
            break
        elif result == "draw":
            print_board()
            print("It's a draw!")
            break
else:
    while True:
        ai_move = nooby() if ch == 1 else best_move()
        board[ai_move] = "O"
        result = check_winner()
        if result == "X":
            print_board()
            print("Player wins!")
            break
        elif result == "O":
            print_board()
            print("AI wins!")
            break
        elif result == "draw":
            print_board()
            print("It's a draw!")
            break

        print_board()
        player_move = int(input("Enter position (0-8): "))

        while player_move < 0 or player_move > 8 or board[player_move] != " ":
            print("Invalid or occupied position! Try again.")
            player_move = int(input("Enter position (0-8): "))

        board[player_move] = "X"
        result = check_winner()
        if result == "X":
            print_board()
            print("Player wins!")
            break
        elif result == "O":
            print_board()
            print("AI wins!")
            break
        elif result == "draw":
            print_board()
            print("It's a draw!")
            break