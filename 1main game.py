import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
GRID_SIZE = 5
CELL_SIZE = WIDTH // GRID_SIZE
COLORS = [(128, 0, 128), (0, 0, 255), (0, 255, 0), (255, 255, 0)]  #violet,plava,zelensa,zolta
BG_COLOR = (200, 200, 200)
LINE_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Fill Puzzle")
board = [[-1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
def is_valid_color(row, col, color):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and board[nr][nc] == color:
            return False
    return True

def draw_board():
    screen.fill(BG_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)  # Рамка на квадратот
            if board[row][col] != -1:
                pygame.draw.rect(screen, COLORS[board[row][col]], rect.inflate(-4, -4))

running = True
selected_cell = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            col, row = mx // CELL_SIZE, my // CELL_SIZE
            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                selected_cell = (row, col)
        elif event.type == pygame.KEYDOWN:
            if selected_cell:
                row, col = selected_cell
                if event.key == pygame.K_1 and is_valid_color(row, col, 0):
                    board[row][col] = 0
                elif event.key == pygame.K_2 and is_valid_color(row, col, 1):
                    board[row][col] = 1
                elif event.key == pygame.K_3 and is_valid_color(row, col, 2):
                    board[row][col] = 2
                elif event.key == pygame.K_4 and is_valid_color(row, col, 3):
                    board[row][col] = 3

    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()
