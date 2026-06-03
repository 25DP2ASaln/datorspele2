def create_board():
    board = [
        ["r","n","b","q","k","b","n","r"],
        ["p","p","p","p","p","p","p","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["P","P","P","P","P","P","P","P"],
        ["R","N","B","Q","K","B","N","R"]
    ]
    return board


def print_board(board):
    print("\n  a b c d e f g h")
    print("  ----------------")
    for i, row in enumerate(board):
        print(8 - i, end="| ")
        print(" ".join(row))
    print()