import math
import random
import pygame

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

# Background
background = pygame.image.load("C:\\Users\\svibh\\OneDrive\\Desktop\\Codingal\\Space Invader Project - Part 1\\Acp_Level_Up_this_game.png")

# Caption and Icon
pygame.display.set_caption("Collision Game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
num_of_enemies = 7

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Load Level Up Image
level_up_img = pygame.image.load("C:\\Users\\svibh\\OneDrive\\Desktop\\Codingal\\Space Invader Project - Part 1\\Acp_Level_Up_this_game.png")

# Play Background Sound
pygame.mixer.music.load("C:\\Users\\svibh\\OneDrive\\Desktop\\Codingal\\Space Invader Project - Part 1\\super-mario-bros-4293.mp3")
pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def isCollision(playerX, playerY, enemyX, enemyY):
    # Check if there is a collision between the player and an enemy
    distance = math.sqrt((playerX - enemyX) ** 2 + (playerY - enemyY) ** 2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))  # Use the new background image here

    # Display the Level Up image at the top right corner (or wherever you'd like)
    screen.blit(level_up_img, (SCREEN_WIDTH - 200, 20))  # Position it near the top-right corner

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player

    # Enemy Movement and Collision Check
    for i in range(num_of_enemies):
        # Check collision between player and enemy
        if isCollision(playerX, playerY, enemyX[i], enemyY[i]):
            score_value += 1
            # Reposition enemy after collision
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        # Draw enemy
        enemy(enemyX[i], enemyY[i], i)

    # Draw player and show score
    player(playerX, playerY)
    show_score(textX, textY)

    # Update the screen
    pygame.display.update()

# Stop the music when the game ends
pygame.mixer.music.stop()
