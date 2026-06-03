from chess_board import create_board, print_board
from game_logic import move_piece, is_valid_input


def convert(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col


def main():
    board = create_board()
    player = "White"

    while True:
        print_board(board)
        print(f"{player} gājiens")

        start = input("No (piem. e2): ")
        end = input("Uz (piem. e4): ")

        sx, sy = convert(start)
        ex, ey = convert(end)

        if not (is_valid_input(sx, sy) and is_valid_input(ex, ey)):
            print("Nepareizs gājiens!")
            continue

        board = move_piece(board, sx, sy, ex, ey)

        player = "Black" if player == "White" else "White"


if __name__ == "__main__":
    main()