"""from config import *
def run():
    print("Still the button not initilaized")
class Page():
    def __init__(self):
        print("Displayer is ready")
        self.screen=screen
        self.Buttons=[]
        self.Canvases=[]
    def clearButtons(self):
        self.Buttons=[]
    def addButton(self,Button):
        self.Buttons.append(Button)
    def addButtons(self,Buttons):
        for Button in Buttons:
            self.addButton(Button)
    
    def clearCanvases(self):
        self.Canvases=[]
    def addCanvas(self,Canvas):
        self.Buttons.append(Canvas)
    def addCanvases(self,Canvases):
        for Canvas in Canvases:
            self.addButton(Canvas)

    def __getShadow(self,Rect):
        shadow=pygame.Surface((Rect.width,Rect.height))
        shadow.set_alpha(128)
        shadow.fill(0)
        return (shadow,(Rect.x+3,Rect.y+3))
        
    def displayButtons(self):
        for button in self.Buttons:
            rect,color=button.getButtonAttr()
            shadow,pos=self.__getShadow(rect)
            screen.blit(shadow,pos)
            pygame.draw.rect(screen, color, rect)
    class Button():
        def __init__(self,x,y,width,height,onClick=run,color=buttonDefaultColor):
            self.Rect=pygame.Rect(x,y,width,height)
            self.RectOn=pygame.Rect(x+3,y+3,width,height)
            self.color=color
            self.colorOn=(abs(color[0]-30),abs(color[1]-30),abs(color[2]-30))
            self.Click=run
            self.hover=
        def getButtonAttr(self,MousePosition):
            if self.Rect.collidepoint(pygame.mouse.get_pos()):
                return (self.Rect, self.color)
            return (self.RectOn, self.colorOn)
        def onClick(self,method):
            self.run=method
        def Pressed(self):
            self.Click()
            """