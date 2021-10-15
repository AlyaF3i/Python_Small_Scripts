
class Listener():
    
    def __init__(self):
        print("Listener is Ready!")
    def MouseListenerClicked(self,page, MouseLocation):
        if page=='Home':
            if self.__isIn((100,100,100,100), MouseLocation):
                print("I'm in")
            else:
                print("I'm out")
    def MouseListenerNotClicked(self,page, MouseLocation):
        if self.__isIn((100,100,100,100), MouseLocation):
            return (103,103)
        else:
            return (100,100)    

    def __isIn(self,Rect,Location):
        #Rect = (x,y,width,height)
        return Rect[2]+Rect[0]-Location[0]>0 and Rect[3]+Rect[1]-Location[1]>0 and Location[0]>Rect[0] and Location[1]>Rect[1]

