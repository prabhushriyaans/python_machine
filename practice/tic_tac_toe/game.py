import torch

from model import TicTacToeNet


WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board):

    print()

    for i in range(0, 9, 3):

        print(
            f" {board[i]} | "
            f"{board[i + 1]} | "
            f"{board[i + 2]}"
        )

        if i < 6:
            print("---+---+---")

    print()


def check_winner(board):

    for a, b, c in WINNING_COMBINATIONS:

        if (
            board[a] != " "
            and board[a] == board[b] == board[c]
        ):
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def encode_board(board, player):

    opponent = "O" if player == "X" else "X"

    encoded = []

    for cell in board:

        if cell == player:
            encoded.append(1)

        elif cell == opponent:
            encoded.append(-1)

        else:
            encoded.append(0)

    return encoded


def neural_move(model, board, player):

    encoded = encode_board(
        board,
        player
    )

    state = torch.tensor(
        [encoded],
        dtype=torch.float32
    )

    model.eval()

    with torch.no_grad():

        output = model(state)[0]

    # Don't allow occupied positions
    for i in range(9):

        if board[i] != " ":
            output[i] = -float("inf")

    return torch.argmax(output).item()


def play_game(model):

    board = [" "] * 9

    human = "X"
    ai = "O"
    # print("\nYou are X")
    # print("AI is O")
    while True:

        print_board(board)


        while True:

            try:

                move = int(
                    input("Enter your move (0-8): ")
                )

                if move < 0 or move > 8:
                    print("Enter a number from 0 to 8.")
                    continue

                if board[move] != " ":
                    print("That position is occupied.")
                    continue

                break

            except ValueError:
                print("Please enter a number.")

        board[move] = human

        result = check_winner(board)

        if result is not None:

            print_board(board)

            if result == "X":
                print("You won!")

            else:
                print("Draw!")

            break

      

        move = neural_move(
            model,
            board,
            ai
        )

        board[move] = ai

        print(f"\nAI chose position {move}")

        result = check_winner(board)

        if result is not None:

            print_board(board)

            if result == "O":
                print("AI won!")

            else:
                print("Draw!")

            break


def main():

    model = TicTacToeNet()

    model.load_state_dict(
        torch.load(
            "tic_tac_toe_model.pth",
            weights_only=True
        )
    )

    print("Trained model loaded successfully.")

    play_game(model)


# if __name__ == "__main__":
#     main()
 