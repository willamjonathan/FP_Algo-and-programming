class screen_size:#for screen size
    def __init__(self,width,height):
        self.width = width
        self.height = height
#setter function
    def setWidth(self,width):
        self.width = width
    def setHeight(self,height):
        self.height = height
#getter function
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
        

class MyColor:#background color if used
    def __init__(self,color=(255,255,255)):#color is in R,G,B ranges from 0-255
        self.color = color
    def setColor(self,color):#setter function
        self.color = color
    def getColor(self):#getter function
        return self.color

class myFPS:#the FPS of the screen
    def __init__(self,FPS=(60)):#FPS is set by default
        self.FPS = FPS
    def setFPS(self,FPS):
        self.setFPS = FPS
    def getFPS (self):#getter function to call the function
        return self.FPS

class p_position:
    def __init__(self,x=370,y=450):
        self.ufoX = x
        self.ufoY = y
    def setUfoX(self,x):
        self.ufoX = x
    def setUfoY(self,y):
        self.ufoY = y
    def getUfoX(self):#getter function to call the function
        return self.ufoX
    def getUfoY(self):#getter function to call
        return self.ufoY

class myFont:
    def __init__(self,font="freesansbold.ttf"):
        self.font = font
    def setMyFont(self,font):
        self.setMyFont = font
    def getMyFont(self):
        return self.font

