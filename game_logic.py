def move_piece(board, start_x, start_y, end_x, end_y):
    piece = board[start_x][start_y]
    board[start_x][start_y] = "."
    board[end_x][end_y] = piece
    return board


def is_valid_input(x, y):
    return 0 <= x < 8 and 0 <= y < 8