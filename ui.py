import pygame

# =========================
# WINDOW SETTINGS
# =========================

WINDOW_WIDTH, WINDOW_HEIGHT = 700, 850
BOARD_SIZE = 500
CELL_SIZE = BOARD_SIZE // 3

# =========================
# COLORS
# =========================

BACKGROUND = (38, 187, 181)
WHITE = (255, 255, 255)
GRID_COLOR = (20, 150, 145)
GREEN = (0, 255, 100)
RED = (255, 80, 80)
BUTTON_TEXT = (33, 150, 243)
BUTTON_COLOR = WHITE

# =========================
# FONTS
# =========================

pygame.font.init()

TITLE_FONT = pygame.font.SysFont("Segoe UI", 42, True)
SCORE_FONT = pygame.font.SysFont("Segoe UI", 40, True)
CELL_FONT = pygame.font.SysFont("Segoe UI", 120, True)
MESSAGE_FONT = pygame.font.SysFont("Segoe UI", 70, True)
BUTTON_FONT = pygame.font.SysFont("Segoe UI", 26, True)

# =========================
# BUTTONS
# =========================

restart_rect = pygame.Rect(0, 760, 200, 55)
difficulty_rect = pygame.Rect(20, 20, 150, 40)

# =========================
# DRAW FUNCTIONS
# =========================

def draw_background(screen):
    screen.fill(BACKGROUND)


def draw_title(screen):
    text = TITLE_FONT.render("TIC TAC TOE", True, WHITE)
    screen.blit(text, text.get_rect(center=(screen.get_width() // 2, 50)))


def draw_scoreboard(screen, player_score, ai_score, player_symbol, ai_symbol):

    # Player score box
    # Player score box - LEFT
    player_rect = pygame.Rect(75, 95, 200, 80)
    pygame.draw.rect(screen, WHITE, player_rect, border_radius=8)

    player = SCORE_FONT.render(
        f"{player_symbol}     {player_score}",
        True,
        (0, 0, 0)
    )

    screen.blit(
        player,
        player.get_rect(center=player_rect.center)
    )

    # AI score box
    # AI score box - RIGHT
    ai_rect = pygame.Rect(
         screen.get_width() - 275,
        95,
        200,
    80
)
    pygame.draw.rect(screen, WHITE, ai_rect, border_radius=8)

    ai = SCORE_FONT.render(
        f"{ai_symbol}     {ai_score}",
        True,
        (0, 0, 0)
    )

    screen.blit(
        ai,
        ai.get_rect(center=ai_rect.center)
    )

def draw_grid(screen, board_x, board_y):
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (board_x + i * CELL_SIZE, board_y),
            (board_x + i * CELL_SIZE, board_y + BOARD_SIZE),
            8,
        )

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (board_x, board_y + i * CELL_SIZE),
            (board_x + BOARD_SIZE, board_y + i * CELL_SIZE),
            8,
        )


def draw_symbols(screen, board, board_x, board_y):
    for row in range(3):
        for col in range(3):
            symbol = board[row][col]

            if symbol:
                color = (0, 0, 0) if symbol == "X" else WHITE

                text = CELL_FONT.render(symbol, True, color)

                screen.blit(
                    text,
                    text.get_rect(
                        center=(
                            board_x + col * CELL_SIZE + CELL_SIZE // 2,
                            board_y + row * CELL_SIZE + CELL_SIZE // 2,
                        )
                    ),
                )


def draw_restart_button(screen):
    pygame.draw.rect(screen, BUTTON_COLOR, restart_rect, border_radius=12)

    text = BUTTON_FONT.render("RESTART", True, BUTTON_TEXT)
    screen.blit(text, text.get_rect(center=restart_rect.center))


def draw_message(screen, message, color):
    if not message:
        return

    text = MESSAGE_FONT.render(message, True, color)

    screen.blit(
        text,
        text.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2)
        ),
    )


def draw_difficulty(screen, difficulty):
    pygame.draw.rect(screen, WHITE, difficulty_rect, border_radius=8)

    text = BUTTON_FONT.render(difficulty, True, BUTTON_TEXT)
    screen.blit(text, (difficulty_rect.x + 15, difficulty_rect.y + 8))


def draw_winning_line(screen, start_pos, end_pos, color):
    pygame.draw.line(screen, color, start_pos, end_pos, 12)


def draw_overlay(screen):
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))
    overlay.set_alpha(150)
    screen.blit(overlay, (0, 0))
