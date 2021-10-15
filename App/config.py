import pygame
pygame.init()
#Background color
screenColor=(100,100,100)
#To Keep Program running
running= True
# width and height for the window
width,height=500,500
#initialize the window
screen = pygame.display.set_mode((width,height))
#title of the window
pygame.display.set_caption("Desert Route Navigation")
#Buttons Color
buttonDefaultColor=(100,150,200)
#Button Text Color
buttonTextColor=(0,0,0)