import pygame
from PIL import Image
img=Image.new('RGB', (500,500),(255,0,0))
strr=img.tobytes()
xx=pygame.image.fromstring(strr, (500,500), 'RGB')
pygame.init()
width,height=500,500
screen=pygame.display.set_mode((width,height))
square=pygame.transform.scale(pygame.image.load(r"img\dirt.jpg"),(50,50))
location=square.get_rect()
speed=5
def change():
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and location.right+speed<=width:
        location.x+=speed
    if key[pygame.K_LEFT] and location.left>=speed:
        location.x-=speed
    if key[pygame.K_DOWN] and location.bottom+speed<=height:
        location.y+=speed
    if key[pygame.K_UP] and location.top>=speed:
        location.y-=speed




    screen.blit(square,location)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.blit(xx, (0,0))
    change()
    pygame.display.update()
    pygame.time.wait(1000//60)
    


pygame.exit()