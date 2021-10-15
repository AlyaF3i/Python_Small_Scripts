import pygame
import random

score=0
pygame.init()
height,width= 800,800
screen=pygame.display.set_mode((height,width))
font = pygame.font.Font('freesansbold.ttf', 32)
FinalScore=f"Score: {score}"
text = font.render(FinalScore, True,  (0,15,115))
class Player():
    def __init__(self,x,y,speed):
        self.speed=speed
        self.right=[
            pygame.transform.scale(pygame.image.load(r"img\Ch\right0.png"),(80,140)),
            pygame.transform.scale(pygame.image.load(r"img\Ch\right1.png"),(80,140))
        ]
        self.location=self.right[0].get_rect()
        self.location.x=x
        self.location.y=y
        self.left=[
            pygame.transform.scale(pygame.image.load(r"img\Ch\left0.png"),(80,140)),
            pygame.transform.scale(pygame.image.load(r"img\Ch\left1.png"),(80,140))
        ]
        self.up=[
            pygame.transform.scale(pygame.image.load(r"img\Ch\up0.png"),(80,140)),
            pygame.transform.scale(pygame.image.load(r"img\Ch\up1.png"),(80,140))
        ]
        self.down=[
            pygame.transform.scale(pygame.image.load(r"img\Ch\down0.png"),(80,140)),
            pygame.transform.scale(pygame.image.load(r"img\Ch\down1.png"),(80,140))
        ]
        self.scope=self.right
             


    def update(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.scope=self.right
            if self.speed+self.location.right<=width:
                self.location.x+=self.speed
        if key[pygame.K_LEFT]:
            self.scope=self.left
            if self.location.left>=self.speed:
                self.location.x-=self.speed
        if key[pygame.K_DOWN]:
            self.scope=self.down
            if self.speed+self.location.bottom<=height:
                self.location.y+=self.speed
        if key[pygame.K_UP]:
            self.scope=self.up
            if self.location.top>=self.speed:
                self.location.y-=self.speed

        screen.blit(self.scope[(self.location.x+self.location.y)%2], self.location)

    def isCollision(self,rect):
        global score,text
        its = self.location.colliderect(rect)
        if its:
            score+=1
            FinalScore=f"Score: {score}"
            text = font.render(FinalScore, True,  (0,15,115))
        return its

        ##################Player Class End####################

class FoodGenerater():
    def __init__(self):
        self.apple=pygame.transform.scale(pygame.image.load(r"img\apple.png"),(50,50))
        self.rect=self.apple.get_rect()
        self.isEaten=True
    def generate(self):
        if self.isEaten:
            x,y=random.randint(0, width-50),random.randint(0, height-50)
            self.rect.x=x
            self.rect.y=y
            self.isEaten=False
        else:
            screen.blit(self.apple, self.rect)

        ##################Food Class End####################
class Monster():
    def __init__(self,speed,loc,size):
        self.img=pygame.transform.scale(pygame.image.load(r'img\dirt.jpg'),size)
        self.speed=speed
        self.rect=self.img.get_rect()
        self.rect.x=loc[0]
        self.rect.y=loc[1]
    def follow(self,human):
        if human.x>self.rect.x:
            self.rect.x+=self.speed
        else:
            self.rect.x-=self.speed
        if human.y>self.rect.y:
            self.rect.y+=self.speed
        else:
            self.rect.y-=self.speed
        screen.blit(self.img, self.rect)
        ###################Monster Class End####################           


running=True
background=pygame.transform.scale(pygame.image.load(r"img\background.jpg"),(800,800))
player=Player(0, 0, 5)
food=FoodGenerater()
food.generate()
monster=Monster(2,(width,0),(30,30))
monster1=Monster(2,(0,height),(30,30))
monster2=Monster(2,(width,height),(30,30))
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background, (0,0))
    player.update()
    food.isEaten=player.isCollision(food.rect)
    food.generate()
    #or player.isCollision(monster2.rect)
    if player.isCollision(monster.rect) or player.isCollision(monster1.rect) :
        score=0
        player=Player(0, 0, 5)
    screen.blit(text, (0,0))
    monster.follow(player.location)
    monster1.follow(player.location)
    monster2.follow(player.location)
    pygame.display.update()
    pygame.event.wait(1000//60)
pygame.quit()
exit()
    