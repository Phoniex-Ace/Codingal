import pygame
import random

Screen_Width, Screen_Height = 500, 400
Movement_Speed = 5
Font_Size = 72

pygame.init()

# Set up background and font
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (Screen_Width, Screen_Height))
font = pygame.font.SysFont("Times New Roman", Font_Size)

# Sprite Class
class Dot(pygame.sprite.Sprite):
    def __init__(self, color, radius):
        super().__init__()
        self.color = color
        self.radius = radius
        self.image = pygame.Surface([2 * radius, 2 * radius], pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        # Ensure sprite stays within bounds
        self.rect.x = max(min(self.rect.x + x_change, Screen_Width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, Screen_Height - self.rect.height), 0)

    def change_color(self, new_color):
        """Change the color of the dot"""
        self.color = new_color
        self.image.fill((0, 0, 0, 0))  # Clear the current image
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

# Set up the screen and sprite group
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Dot Collision")
all_sprites = pygame.sprite.Group()

# Create two dots
dot_1 = Dot(pygame.Color('blue'), 20)
dot_1.rect.x, dot_1.rect.y = random.randint(0, Screen_Width - dot_1.rect.width), random.randint(0, Screen_Height - dot_1.rect.height)
all_sprites.add(dot_1)

dot_2 = Dot(pygame.Color('red'), 20)
dot_2.rect.x, dot_2.rect.y = random.randint(0, Screen_Width - dot_2.rect.width), random.randint(0, Screen_Height - dot_2.rect.height)
all_sprites.add(dot_2)

# Game loop flags
running, won = True, False
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Movement_Speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Movement_Speed
        dot_1.move(x_change, y_change)

    # Check for collision
    if dot_1.rect.colliderect(dot_2.rect):
        # Change colors upon collision
        dot_1.change_color(pygame.Color('green'))  # Change dot_1 to green
        dot_2.change_color(pygame.Color('yellow'))  # Change dot_2 to yellow
        won = True  # Set win flag

    # Drawing
    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You Win!", True, pygame.Color('black'))
        screen.blit(win_text, ((Screen_Width - win_text.get_width()) // 2, (Screen_Height - win_text.get_height()) // 2))

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Frame rate limit

# Quit Pygame
pygame.quit()
