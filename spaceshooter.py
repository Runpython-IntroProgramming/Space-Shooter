"""
spaceshooter.py
Author: Adam Pikielny
Credit: Morgan
ggame documentation
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position, app):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.app = app
        #self.vr = math.atan(self.vy/self.vx)
        self.thrust = 0
        self.thrustframe = 1
        #self.explodeframe = 
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.moveleft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.moveright)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.moveup)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.movedown)
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
        #if self.collidingWith(sun)==True:
            #self.stop

    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.vy!=0:
            self.rotation = -1*math.pi+math.atan(self.vx/self.vy)
            
        #is the below function in the write step?
        #if collidingWithSprites(self)==True:
            #print("collision")
        if self.collidingWith(self.app.sun)==True:
            self.explode()
        """if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)"""

    def moveleft(self, event):
        if self.vx>-1:
            self.vx += -.1
    def moveright(self, event):
        if self.vx<1:
            self.vx += .1
    def movedown(self, event):
        if self.vy<1:
            self.vy += .1
    def moveup(self, event):
        if self.vy>-1:
            self.vy += -.1
    """def moveleft(self, event):
        self.vr+=.001
    def moveright(self, event):
        self.vr-=.001
    magnitude=0
    def moveup(self, event):
        magnitude+=.1
        self.vx=-magnitude*math.sin(self.rotation)
        self.vy=-.1*math.cos(self.rotation)"""
    
    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    
    """def explode(self):
        self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        self.vx=0
        self.vy=0"""



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #bg_asset = RectangleAsset(width, height, noline, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg=Sprite(bg_asset,(0,0))
        sun_asset = ImageAsset("images/sun.png")
        self.sun=Sprite(sun_asset, (200,200))
        SpaceShip((100,100), self)
        #SpaceShip((150,150))
        #SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()