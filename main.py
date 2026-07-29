import pygame
import time

from game import (
    create_board, make_move, check_winner,
    is_draw, reset_board,
    PLAYER_X, PLAYER_O
)

from ai import get_ai_move

from ui import (
    WINDOW_WIDTH, WINDOW_HEIGHT,
    BOARD_SIZE, CELL_SIZE,
    GREEN, RED,
    restart_rect, difficulty_rect,
    draw_background, draw_title,
    draw_scoreboard, draw_grid,
    draw_symbols, draw_restart_button,
    draw_message, draw_difficulty,
    draw_winning_line, draw_overlay
)

pygame.init()

screen = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT),
    pygame.RESIZABLE
)

pygame.display.set_caption("Tic Tac Toe AI")
clock = pygame.time.Clock()

board = create_board()

player_symbol = PLAYER_X
ai_symbol = PLAYER_O

difficulty = "Hard"

player_score = ai_score = 0

game_over = False
message = ""
winning_line = None

ai_wait = False
ai_start = 0


def cell_from_mouse(pos):
    x, y = pos

    bx = (screen.get_width() - BOARD_SIZE) // 2
    by = 277

    if not (bx <= x <= bx + BOARD_SIZE and
            by <= y <= by + BOARD_SIZE):
        return None

    return (
        (y - by) // CELL_SIZE,
        (x - bx) // CELL_SIZE
    )


def end_game(symbol, color):
    global game_over, message, winning_line
    global player_score, ai_score

    result = check_winner(board)

    if result:
        winner, line = result

        if winner == player_symbol:
            player_score += 1
        else:
            ai_score += 1

        game_over = True
        message = f"{winner} WINS!"
        winning_line = (line, color)
        return True

    if is_draw(board):
        game_over = True
        message = "DRAW!"
        return True

    return False


running = True
while running:

    clock.tick(60)

    # ---------------- AI MOVE ----------------
    if ai_wait and not game_over and time.time() - ai_start >= 1:

        move = get_ai_move(board, difficulty, ai_symbol)

        if move:
            make_move(board, move[0], move[1], ai_symbol)
            end_game(ai_symbol, RED)

        ai_wait = False

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:

            screen = pygame.display.set_mode(
                (event.w, event.h),
                pygame.RESIZABLE
            )

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse = pygame.mouse.get_pos()

            # Restart
            if restart_rect.collidepoint(mouse):

                reset_board(board)

                game_over = False
                message = ""
                winning_line = None
                ai_wait = False
                continue

            # Difficulty
            if difficulty_rect.collidepoint(mouse):

                difficulty = {
                    "Easy": "Medium",
                    "Medium": "Hard",
                    "Hard": "Easy"
                }[difficulty]

                continue

            if game_over or ai_wait:
                continue

            cell = cell_from_mouse(mouse)

            if not cell:
                continue

            row, col = cell

            if not make_move(board, row, col, player_symbol):
                continue

            if not end_game(player_symbol, GREEN):
                ai_wait = True
                ai_start = time.time()
                    # ---------------- DRAW ----------------

    draw_background(screen)
    draw_title(screen)

    draw_scoreboard(
        screen,
        player_score,
        ai_score,
        player_symbol,
        ai_symbol
    )

    draw_difficulty(screen, difficulty)

    board_x = (screen.get_width() - BOARD_SIZE) // 2
    board_y = 250

    draw_grid(screen, board_x, board_y)
    draw_symbols(screen, board, board_x, board_y)

    # Winning line
    if winning_line:

        line, color = winning_line
        (r1, c1), (r2, c2) = line

        draw_winning_line(
            screen,
            (
                board_x + c1 * CELL_SIZE + CELL_SIZE // 2,
                board_y + r1 * CELL_SIZE + CELL_SIZE // 2
            ),
            (
                board_x + c2 * CELL_SIZE + CELL_SIZE // 2,
                board_y + r2 * CELL_SIZE + CELL_SIZE // 2
            ),
            color
        )

    # Restart Button
    restart_rect.center = (
        screen.get_width() // 2,
        board_y + BOARD_SIZE + 67
    )

    draw_restart_button(screen)

    # Game Over Popup
    if game_over:

        draw_overlay(screen)

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                screen.get_width() // 2 - 220,
                screen.get_height() // 2 - 100,
                440,
                200
            ),
            border_radius=20
        )

        color = (
            GREEN if "X WINS" in message
            else RED if "O WINS" in message
            else (255, 215, 0)
        )

        draw_message(
            screen,
            message,
            color
        )

    pygame.display.flip()

pygame.quit()
