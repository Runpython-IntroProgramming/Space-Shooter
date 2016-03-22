"""
spaceshooter.py
Author: Payton
Credit: Morgan, Avery, Daniel

Assignment:
Write and submit a program that implements the ControlDwon game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.thrustOff)
        SpaceGame.listenKeyEvent("keyup", "d", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "s", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustOn)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
        
    #def thrustdecel(self, event):
        #self.thrust = 0.5
        
    def rotation(self):
        """
        This attribute may be used to change the rotation of the sprite on the screen.
        Value may be a floating point number. A value of 0.0 means no rotation. A value 
        of 1.0 means  a rotation of 1 radian in a counter-clockwise direction. One radian
        is 180/pi or approximately 57.3 degrees.
        """
        return -self.GFX.rotation
        
    @rotation.setter
    def rotation(self, pi/4):
        self.GFX.rotation = -pi/4



class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg = Sprite(bg_asset, (0,512))
        bg = Sprite(bg_asset, (512,0))
        bg = Sprite(bg_asset, (512,512))
        sn_asset = ImageAsset("images/sun.png")
        sn = Sprite(sn_asset, (400,300))
        SpaceShip((100,100))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()