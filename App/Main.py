from config import *
from AppListener import Listener as listen
from Page import Page as displayer
Button=displayer.Button
Listener=listen()
Displayer=displayer()
Displayer.addButton(Button(10,10,100,50,text="ClickMe",color=(200,200,200)))
CurrentPage='Home'

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
    screen.fill(screenColor)
    Displayer.displayButtons(pygame.mouse.get_pos())
    pygame.display.update()
    pygame.time.wait(1000//60)
pygame.quit()
exit()