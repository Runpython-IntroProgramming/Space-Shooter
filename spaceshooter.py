"""
spaceshooter.py
Author: Payton
Credit: Morgan, Avery, Daniel, Original Spacewar Code

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
        left_location = 1
        ControlDwon.listenKeyEvent("keydown", "w", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "w", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "a", self.rotation)
        ControlDwon.listenKeyEvent("keyup", "a", self.rotation)
        ControlDwon.listenKeyEvent("keyup", "d", self.rotation)
        ControlDwon.listenKeyEvent("keydown", "d", self.rotation)
        ControlDwon.listenKeyEvent("keyup", "s", self.rotation)
        ControlDwon.listenKeyEvent("keydown", "s", self.rotation)
        right_location = 2
        ControlDwon.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "down arrow", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "down arrow", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "left arrow", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "left arrow", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "right arrow", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "right arrow", self.thrustOn)
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
        if self.vr == 0.1:
            self.rotation = 0.001
        if self.vr == -0.1:
            self.rotation = -0.001

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
        
    #def thrustdecel(self, event):
        #self.thrust = 0.5


class ControlDwon(App):
    """
    Tutorial4 space game example.
    """
    strings = {'winner': 'WINNER!',
        'tie': 'TIE!',
        'space': 'Press SPACE to play.',
        'left': 'AWD\nSpace to FIRE',
        'right': 'Arrow Keys\nEnter to FIRE',
        }
    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg = Sprite(bg_asset, (0,512))
        bg = Sprite(bg_asset, (512,0))
        bg = Sprite(bg_asset, (512,512))
        sn_asset = ImageAsset("images/sun.png")
        sn = Sprite(sn_asset, (400,300))
        left_location = 1
        SpaceShip((100,100))
        right_location = 2
        SpaceShip((500,500))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = ControlDwon(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()