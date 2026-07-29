import random

from game import (
    check_winner,
    is_draw,
    get_available_moves,
    PLAYER_X,
    PLAYER_O,
    EMPTY
)


# --------------------------------------------------
# EVALUATE BOARD
# --------------------------------------------------

def evaluate(board, ai_symbol, player_symbol):

    result = check_winner(board)

    if result:
        winner = result[0]

        if winner == ai_symbol:
            return 10

        elif winner == player_symbol:
            return -10

    return 0


# --------------------------------------------------
# MINIMAX WITH ALPHA PRUNING
# --------------------------------------------------

def minimax_alpha(
    board,
    depth,
    alpha,
    maximizing,
    ai_symbol,
    player_symbol
):

    # Check current board
    score = evaluate(
        board,
        ai_symbol,
        player_symbol
    )

    # AI wins
    if score == 10:
        return score - depth

    # Player wins
    if score == -10:
        return score + depth

    # Draw
    if is_draw(board):
        return 0


    # ----------------------------------------------
    # AI TURN - MAXIMIZING
    # ----------------------------------------------

    if maximizing:

        best_score = -1000

        for row, col in get_available_moves(board):

            # Try AI move
            board[row][col] = ai_symbol

            # Check future moves
            value = minimax_alpha(
                board,
                depth + 1,
                alpha,
                False,
                ai_symbol,
                player_symbol
            )

            # Undo move
            board[row][col] = EMPTY

            # Get highest score
            best_score = max(
                best_score,
                value
            )

            # Update alpha
            alpha = max(
                alpha,
                best_score
            )

        return best_score


    # ----------------------------------------------
    # PLAYER TURN - MINIMIZING
    # ----------------------------------------------

    else:

        best_score = 1000

        for row, col in get_available_moves(board):

            # Try player move
            board[row][col] = player_symbol

            # Check future moves
            value = minimax_alpha(
                board,
                depth + 1,
                alpha,
                True,
                ai_symbol,
                player_symbol
            )

            # Undo move
            board[row][col] = EMPTY

            # Get lowest score
            best_score = min(
                best_score,
                value
            )

            # Alpha pruning
            if best_score <= alpha:
                break

        return best_score


# --------------------------------------------------
# HARD MODE
# --------------------------------------------------

def hard_move(board, ai_symbol):

    player_symbol = (
        PLAYER_O
        if ai_symbol == PLAYER_X
        else PLAYER_X
    )

    best_score = -1000
    best_move = None

    for row, col in get_available_moves(board):

        # Try AI move
        board[row][col] = ai_symbol

        # Calculate score
        score = minimax_alpha(
            board,
            0,
            -1000,
            False,
            ai_symbol,
            player_symbol
        )

        # Undo move
        board[row][col] = EMPTY

        # Select best move
        if score > best_score:

            best_score = score
            best_move = (row, col)

    return best_move


# --------------------------------------------------
# MEDIUM MODE
# --------------------------------------------------

def medium_move(board, ai_symbol):

    available = get_available_moves(board)

    # 70% random move
    if random.random() < 0.6:
        return random.choice(available)

    # 30% intelligent move
    return hard_move(
        board,
        ai_symbol
    )

# --------------------------------------------------
# EASY MODE
# --------------------------------------------------

def easy_move(board):

    available = get_available_moves(board)

    return random.choice(
        available
    )


# --------------------------------------------------
# SELECT AI DIFFICULTY
# --------------------------------------------------

def get_ai_move(
    board,
    difficulty,
    ai_symbol
):

    if difficulty == "Easy":

        return easy_move(
            board
        )

    elif difficulty == "Medium":

        return medium_move(
            board,
            ai_symbol
        )

    else:

        return hard_move(
            board,
            ai_symbol
        )
