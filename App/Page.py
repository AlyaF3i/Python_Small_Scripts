from config import *
def run():
    print("Still the button not initilaized")
class Page():
    font=pygame.font.Font('freesansbold.ttf', 20)
    def __init__(self,pageName):
        self.PageName=pageName
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
    def displayButtons(self,MousePosition):
        for button in self.Buttons:
            rect,color,text=button.getButtonAttr(MousePosition)
            shadow,pos=self.__getShadow(rect)
            self.screen.blit(shadow,pos)
            but=pygame.draw.rect(screen, color, rect)
            text=Page.font.render(text, True,  buttonTextColor)
            size=text.get_rect()
            temp=(but.x+abs(size[2]-but.width)/2,but.y+abs(size[3]-but.height)/2)
            self.screen.blit(text,temp)
    
    def displayCanvases(self):
        for canvas in self.Canvases:
            img,rect=canvas.getCanvas()
            self.screen.blit(img,rect)
    def update(self):
        self.displayButtons()
        self.displayCanvases()

    class Button():
        def __init__(self,x,y,width,height,onClick=run,text="Button",color=buttonDefaultColor):
            self.Rect=pygame.Rect(x,y,width,height)
            self.RectOn=pygame.Rect(x+3,y+3,width,height)
            self.color=color
            self.colorOn=(abs(color[0]-30),abs(color[1]-30),abs(color[2]-30))
            self.Click=run
            self.text=text
        def getButtonAttr(self,MousePosition):
            if self.Rect.collidepoint(pygame.mouse.get_pos()):
                return (self.Rect, self.color,self.text)
            return (self.RectOn, self.colorOn,self.text)
        def onClick(self,method):
            self.run=method
        def Pressed(self):
            self.Click()
    
    class Canvas():
        def __init__(self,x,y,width,height,img=pygame.image.load("Hi.png")):
            self.Rect=pygame.Rect(x,y,width,height)
            self.img=pygame.transform.scale(img,(width,height))
        def updateImg(self,img):
            self.img=img
        def getCanvas(self):
            return self.img,self.Rect

            