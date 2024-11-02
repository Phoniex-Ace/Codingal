import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 600

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

# Set a color (RGB)
background_color = (0, 0, 0)  # Black

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()