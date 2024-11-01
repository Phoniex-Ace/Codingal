import pygame
pygame.init()
#Create Display Surface object of specific dimension
window = pygame.display.set_mode((400,400))
#Fill The Screen With White Colour
window.fill((255 , 255, 255))
#Define Colours
GREEN = (0, 255,0)
# Draw Solid Circle
pygame.draw.circle(window, GREEN, (300,300), 50)
# Draw Outlined Circle
pygame.draw.circle(window, GREEN, (100,100), 50, 3)
#Draw The Surface Object To The Screen
pygame.display.update()
#Game Loop
running = True
while running:
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Quit Pygame
pygame.quit()