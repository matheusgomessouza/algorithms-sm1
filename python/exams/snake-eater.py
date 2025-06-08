import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10  # Back to original size

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set up game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    """Draw the snake on the screen"""
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], block_size, block_size])

def game_loop():
    """Main game loop"""
    game_over = False
    game_close = False

    # Start position (centered)
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = BLOCK_SIZE  # Start moving right
    y_change = 0

    # Initialize snake with 4 blocks
    snake_list = []
    snake_length = 4  # Keep 4 blocks
    # Create initial snake body (4 blocks to the left of center)
    for i in range(4):
        snake_list.append([x - (i * BLOCK_SIZE), y])

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Wait for first key press
    waiting_for_key = True
    while waiting_for_key and not game_over:
        screen.fill(GREEN)
        message = font.render("Press any arrow key to start", True, BLACK)
        # Center the start message as well
        text_width = message.get_width()
        text_height = message.get_height()
        screen.blit(message, [(WIDTH - text_width) // 2, (HEIGHT - text_height) // 2])
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                waiting_for_key = False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    waiting_for_key = False
                    # Set initial direction based on first key press
                    if event.key == pygame.K_LEFT:
                        x_change = -BLOCK_SIZE
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = BLOCK_SIZE
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -BLOCK_SIZE
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = BLOCK_SIZE
                        x_change = 0

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
            # Calculate text width and position to center it
            text_width = message.get_width()
            text_height = message.get_height()
            screen.blit(message, [(WIDTH - text_width) // 2, (HEIGHT - text_height) // 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        x += x_change
        y += y_change

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(GREEN)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()

game_loop()