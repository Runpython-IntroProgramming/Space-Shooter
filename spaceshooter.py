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
    asset = ImageAsset("images/UFO.png", 
        Frame(145,0,145-145,145), 6, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrustL = 0
        self.thrustR = 0
        self.thrustU = 0
        self.thrustD = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLOn)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustROn)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustROff)
        
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUOff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDOn)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDOff)


        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if self.thrustL == 1:
            self.vx -= 0.03
        if self.thrustR == 1:
            self.vx += 0.03
        if self.thrustU == 1:
            self.vy -= 0.03
        if self.thrustD == 1:
            self.vy += 0.03
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrustL == 1 or self.thrustR == 1 or self.thrustU == 1 or self.thrustD == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 6:
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

    def thrustUOn(self, event):
        self.thrustU = 1

    def thrustUOff(self, event):
        self.thrustU = -1
        
    def thrustDOn(self, event):
        self.thrustD = 1
    
    def thrustDOff(self, event):
        self.thrustD = -1


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