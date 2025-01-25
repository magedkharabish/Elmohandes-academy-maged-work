import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Set up display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to display message
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position
    x = width / 2
    y = height / 2

    # Snake movement
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(blue)
            display_message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handling key events for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Check for boundary conditions (game over if snake hits boundaries)
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)

        # Draw food
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])

        # Update snake body
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
