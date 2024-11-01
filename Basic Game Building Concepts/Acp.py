import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen")

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up the font and text
font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", True, blue)

# Define the rectangle
rect_x = 300
rect_y = 200
rect_width = 200
rect_height = 100
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill(white)

    # Draw the rectangle
    pygame.draw.rect(screen, blue, rectangle)

    # Render the text on the screen
    screen.blit(text, (250, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
