import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser Canvas")

# Create grid
rows = HEIGHT // CELL_SIZE
cols = WIDTH // CELL_SIZE
grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col],
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check for mouse drag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
            eraser_x = mouse_x // CELL_SIZE
            eraser_y = mouse_y // CELL_SIZE

            # Erase cells within eraser size
            for i in range(-ERASER_SIZE // CELL_SIZE, ERASER_SIZE // CELL_SIZE):
                for j in range(-ERASER_SIZE // CELL_SIZE, ERASER_SIZE // CELL_SIZE):
                    new_x, new_y = eraser_x + i, eraser_y + j
                    if 0 <= new_x < cols and 0 <= new_y < rows:
                        grid[new_y][new_x] = WHITE  # Erasing effect

    pygame.display.flip()  # Update display

pygame.quit()

     