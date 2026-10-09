import random
board=[" "]*9
winning_positions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner_index():
  for a,b,c in winning_positions:
    if board[a]==board[b]==board[c] and board[a]!=" ":
      return board[a]
  if " " not in board:
      return "draw"
  return None

def Board():
  for i in range(3):
    for j in range(3):
      print(f"{board[i*3+j]}",end=" ")
      if j<2:
        print("|",end=" ")
    if i<2:
      print("\n--+---+--")
  print()

def minmax(maxing):
  win=winner_index()
  if win=="O":
    return 1
  elif win=="X":
    return -1
  elif win=="draw":
    return 0
  if maxing:
    top_score=-999
    for i in range(9):
      if board[i]==" ":
        board[i]="O"
        score=minmax(False)
        board[i]=" "
        top_score=max(top_score,score)
    return top_score
  else:
    top_score=999
    for i in range(9):
      if board[i]==" ":
        board[i]="X"
        score=minmax(True)
        board[i]=" "
        top_score=min(top_score,score)
    return top_score

def AI_move():
  top_score=-999
  move=None
  for i in range(9):
    if board[i]==" ":
      board[i]="O"
      score=minmax(False)
      board[i]=" "
      if score>top_score:
        top_score=score
        move=i
  return move


def best_move():
  return AI_move()

def print_board():
   return Board()

def check_winner():
    return winner_index()

def nooby():
    while True:
        move=random.randint(0, 8)
        if board[move] == " ":
            return move

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