class TicTacToe:
    def __init__(self):
        self.board=[" "]*9
        self.winning_combinations=[
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        
    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i*3+j],end=" ")
                if j<2:
                    print("|",end=" ")
            if i<2:
                print("\n--+---+--")
        print()
    
    def check_winner(self):
        for a,b,c in self.winning_combinations:
            if self.board[a]==self.board[b]==self.board[c] and self.board[a]!=" ":
                return self.board[a]
        if " " not in self.board:
            return "Draw"
        return None
    
    def minmax(self,maxing):
        winner=self.check_winner()
        if winner=="X":
            return -1
        elif winner=="O":
            return 1
        elif winner=="Draw":
            return 0
        if maxing:
            top_score=-float("inf")
            for i in range(9):
                if self.board[i]==" ":
                    self.board[i]="O"
                    score=self.minmax(False)
                    self.board[i]=" "
                    top_score=max(top_score,score)
            return top_score
        else:
            top_score=float("inf")
            for i in range(9):
                if self.board[i]==" ":
                    self.board[i]="X"
                    score=self.minmax(True)
                    self.board[i]=" "
                    top_score=min(top_score,score)
            return top_score
        
    def AI_move(self):
        top_score=-float("inf")
        move=None
        for i in range(9):
            if self.board[i]==" ":
                self.board[i]="O"
                score=self.minmax(False)
                self.board[i]=" "
                if score > top_score:
                    top_score=score
                    move=i
        return move
    
    def nooby(self):
        import random
        while True:
            move=random.randint(0,8)
            if self.board[move]==" ":
                return move
            
    def play(self):
        from game import main
        print("Welcome to Tic Tac Toe!")
        print("What level of AI do you want to play against? (1: Nooby, 2: Intermidiate, 3:Pro)")
        # level=int(input("Enter your choice (1 or 2): "))
        level=0
        flag=1
        while flag==1:
            level=int(input("Enter your choice (1 or 2 or 3): "))
            if level==1 or level==2 or level==3:
                flag=0
            else:
                print("Invalid choice.")
        if level==2:
            main()
            return
        while True:
            self.display_board()
            winner=self.check_winner()
            if winner is not None:
                if winner=="Draw":
                    print("It's a draw!")
                else:
                    print(f"{"AI" if winner=="O" else "player"} wins!")
                break
            move=int(input("Enter your move (0-8): "))
            if self.board[move]==" ":
                self.board[move]="X"
            else:
                print("Invalid move. Try again.")
                continue
            winner=self.check_winner()
            if winner is not None:
                continue
            ai_move=self.AI_move() if level==3 else self.nooby()
            if ai_move is not None:
                self.board[ai_move]="O"