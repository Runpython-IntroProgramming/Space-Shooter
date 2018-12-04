"""
spaceshooter.py
Author: Jackson
Credit: spacewar game

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame

# add your code here \/  \/  \/
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, SoundAsset

myapp = App()

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
grey = Color(0xCDC0B0, 1.0)
firyred = Color(0xFF3030, 1.0)
purple = Color(0xBF3EFF, 1.0)
gold = Color(0xFFD700, 1.0)
white = Color(0xF8F8FF, 1.0)
violet = Color(0xd147c5, 1.0)
teal = Color(0x95E8C4, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)



class sun(Sprite):
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(sun.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5

class rocket(Sprite):
    rocketpicture = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227, 0, 65, 125), 4, 'vertical')
        
    def __init__(self, pos):
        super().__init__(rocket.rocketpicture, pos)
        rocket.x = 500
        rocket.y = 250
        rocket.vx = 0
        rocket.vx = 0
        rocket.rv = 0.03
        self.move = 0
        self.moveframe = 1

        rocket.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        #rocket.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        #rocket.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        #rocket.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
    
    def rightarrow(self, event):
        self.xv += 1
    
    def leftarrowKey(self, event):
        self.vx -= 1
        
    def uparrowKey(self, event):
        self.vy -= 1
        
    def downarrowKey(self, event):
        self.vy += 1



    def step(self):
        self.x += self.xv
        self.y += self.yv
        self.rotation += self.rv
        
        if self.move == 1:
            self.setImage(self.moveframe)
            self.moveframe += 1
            if self.moveframe == 4:
                self.moveframe = 1
        else:
            self.setImage(0)

class spaceshooter(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0, 0))
        bg.scale = 2
        self.rocketship = rocket((500,30))
        self.sun = sun((500,250))
        #self.listenKeyEvent('keydown', 'right arrow', )

    
    #def step(self):
     #   self.rocketship.x += 0.75
      #  self.rocketship.y += 0.75
    
    


#----------------------------------------------------------------------------------#
myapp = spaceshooter()
myapp.run()