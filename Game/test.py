import sys, pygame
pygame.init()

size = width, height = 800, 640
black = 0, 0, 255
color= 255,255,255
SPEED=20
screen = pygame.display.set_mode(size,0,32)
screen.fill(black)
location=pygame.Rect(10, 10, 30, 150)
rect = pygame.draw.rect(screen, color, location)
up=False
down=False
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        """
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                up=True
            if event.key==pygame.K_DOWN:
                down=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                up=not up
            if event.key==pygame.K_DOWN:
                down=not down
        if up:
            location = rect.move(0, -SPEED)
            rect = pygame.draw.rect(screen, color, location)
        if down:
            location = rect.move(0, SPEED)
            rect = pygame.draw.rect(screen, color, location)
        """
        keys = pygame.key.get_pressed()
    
        rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
        rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
            
        rect.centerx = rect.centerx % window.get_width()
        rect.centery = rect.centery % window.get_height()

        screen.fill(0)
        pygame.draw.rect(screen, (255, 0, 0), rect)
        pygame.display.flip()
    