import pygame
import random

from pygame.sprite import _Group

Screen_Width , Screen_Height = 500, 400
Movement_Speed = 5
Font_Size = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("bg.jpg"), (Screen_Width, Screen_Height))
font = pygame.font.SysFont("Times New Roman", Font_Size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__
        self.image  = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image , color, pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min (self.rect.x + x_change, Screen_Width - self.rect.width), 0)
        self.rect.y = max(min (self.rect.y + y_change, Screen_Height - self.rect.height), 0)

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Sprite Collison")
all_sprites = pygame.sprite.Group()

sprite_1 = Sprite(pygame.Color('black'), 20 , 30) 
sprite_1.rect.x, sprite_1.rect.y = random.randint(0, Screen_Width - sprite_1.rect.width),random.randint(0,Screen_Height - sprite_1.rect.height)
all_sprites.add(sprite_1)


sprite_2 = Sprite(pygame.Color('red'), 20 , 30) 
sprite_2.rect.x, sprite_2.rect.y = random.randint(0, Screen_Width - sprite_2.rect.width),random.randint(0,Screen_Height - sprite_2.rect.height)
all_sprites.add(sprite_2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
        if not won:
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT]- keys[pygame.K_LEFT]) * Movement_Speed
            y_change = (keys[pygame.K_DOWN]- keys[pygame.K_UP]) * Movement_Speed
            sprite_1.move(x_change, y_change)
    if sprite_1.rect.colliderect(sprite_2.rect):
        all_sprites.remove(sprite_2)
        won = True
    # Drawing
screen.blit(background_image, (0, 0))
all_sprites.draw(screen)

# Display win message
if won:
    win_text = font.render("You win!", True, pygame.Color('black'))
    screen.blit(win_text, ((Screen_Width - win_text.get_width()) // 2,
                           (Screen_Height - win_text.get_height()) // 2))

pygame.display.flip()
clock.tick(90)

pygame.quit()