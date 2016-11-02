"""
spaceshooter.py
Author: vinzentmoesch
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
"""
tutorial4.py
by E. Dennison
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

#Hintergrund
class Stars(Sprite):

    asset = ImageAsset("images/starswithoutspacesmall.jpg")
    width = 7485
    height = 4930

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        self.scale = 0.23


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 0
        self.vr = 0
        self.thrustL = 0
        self.thrustR = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLOn)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustROn)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustROff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if self.thrustL == 1:
            self.vx -= 0.01
        if self.thrustL == -1:
            self.vx += 0.01
        if self.thrustR == 1:
            self.vx -= -0.01
        if self.thrustR == -1:
            self.vx -= 0.01
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrustL == 1 or self.thrustR == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustLOn(self, event):
        self.thrustL = 1

    def thrustLOff(self, event):
        self.thrustL = -1
    
    def thrustROn(self, event):
        self.thrustR = 1
        
    def thrustROff(self, event):
        self.thrustR = -1


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        Stars((0,0))
        SpaceShip((500,500))


    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(1900, 950)
myapp.run()