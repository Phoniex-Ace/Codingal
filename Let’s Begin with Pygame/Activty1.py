#Import Necessary Libraries
import pygame

#Instalize Required Modules
pygame.init()

#Setup Window Geometry
screen = pygame.display.set_mode((400,500))

#Create A Loop To Run The Game Until It Is Quit By The User
done = False

while not done:

    #Clear Event Queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()