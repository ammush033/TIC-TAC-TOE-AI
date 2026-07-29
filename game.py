EMPTY = ""

PLAYER_X = "X"
PLAYER_O = "O"


def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def make_move(board, row, col, symbol):
    if board[row][col] != EMPTY:
        return False

    board[row][col] = symbol
    return True


def check_winner(board):

    # Rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0], ((row, 0), (row, 2))

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col], ((0, col), (2, col))

    # Main diagonal
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0], ((0, 0), (2, 2))

    # Anti diagonal
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2], ((0, 2), (2, 0))

    return None


def is_draw(board):
    if check_winner(board):
        return False

    return all(cell != EMPTY for row in board for cell in row)


def get_available_moves(board):
    return [
        (row, col)
        for row in range(3)
        for col in range(3)
        if board[row][col] == EMPTY
    ]


def reset_board(board):
    for row in range(3):
        for col in range(3):
            board[row][col] = EMPTY
