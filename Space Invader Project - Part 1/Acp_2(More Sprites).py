import math
import random
import pygame
import base64
from io import BytesIO

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background Image from file or URL (You can keep your background here)
background = pygame.image.load('background.png')  # Replace with your file path if needed

# Caption and Icon
pygame.display.set_caption("Collision Game")
icon = pygame.image.load('ufo.png')  # Replace with your actual icon path
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Villain (Enemy) Sprite in base64
villain_base64 = """
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
"""

# Decode base64 to image
villain_image_data = base64.b64decode(villain_base64)
villain_image = pygame.image.load(BytesIO(villain_image_data))

# Villain Position
villainX = random.randint(0, SCREEN_WIDTH - 64)
villainY = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
villainX_change = 4
villainY_change = 40

# Player Movement
def player_move():
    global playerX, playerX_change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > 0:
        playerX -= 5
    if keys[pygame.K_RIGHT] and playerX < SCREEN_WIDTH - 64:
        playerX += 5

# Villain Movement
def villain_move():
    global villainX, villainY, villainX_change, villainY_change
    villainX += villainX_change
    if villainX <= 0 or villainX >= SCREEN_WIDTH - 64:
        villainX_change *= -1
        villainY += villainY_change

# Collision Detection
def is_collision(villainX, villainY, playerX, playerY):
    distance = math.sqrt((math.pow(villainX - playerX, 2)) + (math.pow(villainY - playerY, 2)))
    if distance < COLLISION_DISTANCE:
        return True
    return False

# Main Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen (black)
    screen.blit(background, (0, 0))  # Draw background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_move()
    villain_move()

    # Check for collision
    if is_collision(villainX, villainY, playerX, playerY):
        print("Collision detected!")

    # Draw player and villain
    screen.blit(playerImg, (playerX, playerY))
    screen.blit(villain_image, (villainX, villainY))

    pygame.display.update()

# Quit Pygame
pygame.quit()
