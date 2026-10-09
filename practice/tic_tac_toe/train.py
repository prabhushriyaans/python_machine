import itertools
import random

import torch
import torch.nn as nn
import torch.optim as optim

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


def check_winner(board):

    for a, b, c in WINNING_COMBINATIONS:

        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def get_available_moves(board):

    return [
        i for i, cell in enumerate(board)
        if cell == " "
    ]


def minimax(board, current_player, ai_player):

    winner = check_winner(board)

    if winner == ai_player:
        return 1

    if winner is not None and winner != "Draw":
        return -1

    if winner == "Draw":
        return 0

    opponent = "O" if current_player == "X" else "X"

    scores = []

    for move in get_available_moves(board):

        board[move] = current_player

        score = minimax(
            board,
            opponent,
            ai_player
        )

        board[move] = " "

        scores.append(score)

    if current_player == ai_player:
        return max(scores)

    return min(scores)


def get_best_move(board, player):

    best_score = -float("inf")
    best_moves = []

    opponent = "O" if player == "X" else "X"

    for move in get_available_moves(board):

        board[move] = player

        score = minimax(
            board,
            opponent,
            player
        )

        board[move] = " "

        if score > best_score:
            best_score = score
            best_moves = [move]

        elif score == best_score:
            best_moves.append(move)

    return random.choice(best_moves)


def is_valid_board(board):

    x_count = board.count("X")
    o_count = board.count("O")

    if not (
        x_count == o_count
        or x_count == o_count + 1
    ):
        return False

    winner = check_winner(board)

    if winner == "X" and x_count != o_count + 1:
        return False

    if winner == "O" and x_count != o_count:
        return False

    return True


def get_current_player(board):

    x_count = board.count("X")
    o_count = board.count("O")

    if x_count == o_count:
        return "X"

    return "O"


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


def generate_dataset():

    X = []
    y = []

    for cells in itertools.product(
        [" ", "X", "O"],
        repeat=9
    ):

        board = list(cells)

        if not is_valid_board(board):
            continue

        if check_winner(board) is not None:
            continue

        player = get_current_player(board)

        best_move = get_best_move(
            board,
            player
        )

        encoded_board = encode_board(
            board,
            player
        )

        X.append(encoded_board)
        y.append(best_move)

    return X, y


def train_model():

    print("Generating training data...")

    X, y = generate_dataset()

    print(f"Training samples: {len(X)}")

    X = torch.tensor(
        X,
        dtype=torch.float32
    )

    y = torch.tensor(
        y,
        dtype=torch.long
    )

    indices = torch.randperm(len(X))

    X = X[indices]
    y = y[indices]

    split = int(len(X) * 0.8)

    X_train = X[:split]
    y_train = y[:split]

    X_test = X[split:]
    y_test = y[split:]

    model = TicTacToeNet()

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.SGD(
        model.parameters(),
        lr=0.1
    )

    epochs = 300

    for epoch in range(epochs):

        model.train()

        optimizer.zero_grad()

        output = model(X_train)

        loss = criterion(
            output,
            y_train
        )

        loss.backward()

        optimizer.step()

        if (epoch + 1) % 25 == 0:

            model.eval()

            with torch.no_grad():

                test_output = model(X_test)

                predictions = torch.argmax(
                    test_output,
                    dim=1
                )

                accuracy = (
                    predictions == y_test
                ).float().mean().item()

            print(
                f"Epoch {epoch + 1:3d} | "
                f"Loss: {loss.item():.4f} | "
                f"Accuracy: {accuracy * 100:.2f}%"
            )

    torch.save(
        model.state_dict(),
        "tic_tac_toe_model.pth"
    )

    print("\nTraining completed.")
    print("Model saved as tic_tac_toe_model.pth")


if __name__ == "__main__":
    train_model()