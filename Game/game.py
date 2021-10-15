import pygame
from pygame.locals import *


pygame.init()

width,height = 800, 800

screen= pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")
sun=pygame.image.load("img/sun.png")
background = pygame.image.load("img/bg.jpg")
background = pygame.transform.scale(background, (800,800))
class Player():
    def __init__(self,x,y):
        self.images_right=[
            pygame.transform.scale(pygame.image.load("img/blueCharacter0.png"),(40, 80)),
            pygame.transform.scale(pygame.image.load("img/blueCharacter1.png"),(40, 80))
            ]
        #pygame.transform.flip(pygame.transform.scale(img,(40, 80)), xBool=True)
        img=pygame.image.load("img/blueCharacter0.png")
        self.image= pygame.transform.scale(img,(40, 80))
        self.images_right=[
            self.image,
            pygame.transform.scale(pygame.image.load("img/blueCharacter1.png"),(40, 80))
            ]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.vel_y=0
        self.jump=False
    def update(self):
        dx=0
        dy=0
        key=pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.jump:
            self.vel_y=-10
            self.jump=True
        if not key[pygame.K_SPACE]:
            self.jump=False
        if key[pygame.K_LEFT]:
            dx-=5
        if key[pygame.K_RIGHT]:
            dx+=5
        self.vel_y+=1
        if self.vel_y>10:
            self.vel_y=10
        dy+=self.vel_y
        self.rect.x+=dx
        self.rect.y+=dy
        if self.rect.bottom>height:
            self.rect.bottom=height
            dy=0
        
        screen.blit(self.images_right[self.rect.x%2],self.rect)
        

class World():
    def __init__(self,data):
        self.rects=[]
        self.dirt=pygame.transform.scale(pygame.image.load("img/dirt.jpg"),(50,50))
        for row,i in zip(data,range(16)):
            for its,j in zip(row,range(16)):
                if its:
                    imgRect=self.dirt.get_rect()
                    imgRect.x=j*50
                    imgRect.y=i*50
                    self.rects.append(imgRect)

    def draw(self):
        for rect in self.rects:
            screen.blit(self.dirt,rect)
#ground = pygame.image.load("img/ground.jpg")
running= True
w=width//16
h=height//16
world_data=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0],
    [0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
player=Player(100,height-130)
world=World(world_data)
dirt=pygame.transform.scale(pygame.image.load("img/dirt.jpg"),(50,50))
while running:
    screen.blit(background, (0,0))
    screen.blit(sun, (50,50))
    world.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    for a in range(1,16):
        pygame.draw.line(screen, (255,255,255), (0,a*h), (width,a*h))
        pygame.draw.line(screen, (255,255,255), (a*w,0), (a*w,height))                
    pygame.display.update()
    pygame.event.wait(1000//60)
pygame.quit()
exit()