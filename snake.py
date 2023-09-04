import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
WIDTH, HEIGHT = 640, 480

# Snake settings
snake_pos = [[100, 100], [90, 100], [80, 100]]
snake_speed = [1, 0]
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Pygame settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def display_snake(snake_pos):
    print(snake_pos)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def display_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

while snake_pos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_RIGHT]:
                snake_speed = [10, 0]
            if keys[pygame.K_LEFT]:
                snake_speed = [-10, 0]
            if keys[pygame.K_UP]:
                snake_speed = [0, -10]
            if keys[pygame.K_DOWN]:
                snake_speed = [0, 10]
    
    new_snake_pos = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]
    snake_pos = [new_snake_pos] + snake_pos

    # Wrap around mechanics
    if snake_pos[0][0] < 0:
        snake_pos[0][0] = WIDTH
    if snake_pos[0][0] > WIDTH:
        snake_pos[0][0] = 0
    if snake_pos[0][1] < 0:
        snake_pos[0][1] = HEIGHT
    if snake_pos[0][1] > HEIGHT:
        snake_pos[0][1] = 0

    # Food mechanics
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True

    screen.fill(WHITE)
    display_snake(snake_pos)
    display_food(food_pos)
    pygame.display.flip()
    clock.tick(10)
