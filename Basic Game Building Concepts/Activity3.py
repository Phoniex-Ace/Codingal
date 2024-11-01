import pygame
pygame.init()
display = pygame.display.set_mode((300,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            print("A Key Has Been Pressed")