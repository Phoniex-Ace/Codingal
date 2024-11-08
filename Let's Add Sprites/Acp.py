import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen with Sprites")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite settings
player_size = (50, 50)
player_pos = [WIDTH // 4, HEIGHT // 2]
sprite2_pos = [3 * WIDTH // 4, HEIGHT // 2]

# Speed
player_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement controls for the player sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Screen background
    screen.fill(WHITE)

    # Draw sprites
    player_rect = pygame.draw.rect(screen, BLUE, (*player_pos, *player_size))
    sprite2_rect = pygame.draw.rect(screen, RED, (*sprite2_pos, *player_size))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
