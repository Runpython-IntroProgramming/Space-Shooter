"""
spaceshooter.py
Author: Jackson
Credit: spacewar game, ggame documentation

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
        self.vx = 1
        self.vy = 1
        self.vr = .008
        self.thrust = 0
        self.thrustframe = 1

        spaceshooter.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        spaceshooter.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        spaceshooter.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        spaceshooter.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
    
    def rightarrowKey(self, event):
        self.vx+=0.9
        
    def leftarrowKey(self, event):
        self.vx+=-0.9
        
    def uparrowKey(self, event):
        self.vy -= 0.9
        
    def downarrowKey(self, event):
        self.vy+=.9


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        c = self.collidingWith

        if self.thrust == 5:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 2:
                self.thrustframe = 1
        else:
            self.setImage(0)
        #colliding = self.collidingWith(myapp.sun)
        #collidinglist = self.collidingWithSprites(sun)
    
    
 
        
            

class spaceshooter(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0, 0))
        bg.scale = 2
        self.rocketship = rocket((500,30))
        self.sun = sun((500,250))
        
    def step(self):
        pass
        

class Explos(Sprite):
    explos = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    
    def __init__(self, position):
        super().__init__(explos.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5


    def step(self):
        self.nextImage()
        if self.rocketship:
            self.rocketship.step()
            if self.rocketship.collidingWith(self.sun):
                self.rocketship.destroy()
                self.rocketship = Explos

            









#----------------------------------------------------------------------------------#
myapp = spaceshooter()
myapp.run()