"""
spaceshooter.py
Author: Funjando
Credit: Don-the-wott, Payton-man (like....so much)

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
#Imports
from ggame import math, App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

#ScreenSize
SCREEN_WIDTH=1200
SCREEN_HEIGHT=850

sun=none

class SpaceShip(Sprite):
    #The actual animated spaceship

    asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227, 0, 292-227, 125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Spaceship.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0.0
        self.thrust=0
        self.thrustframe=1
        self.rotation=0
        left_location=1
        ControlDwon.listenKeyEvent("keydown", "w", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "w", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "d", self.rotationOnLeft)
        ControlDwon.listenKeyEvent("keyup", "d", self.rotationOff)
        ControlDwon.listenKeyEvent("keydown", "a", self.rotationOnRight)
        ControlDwon.listenKeyEvent("keyup", "a", self.rotationOff)
        self.fxcenter=self.fycenter=0.5

    def step(self):
        self.x+=self.vx
        self.y+=self.vy
        self.rotation+=self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx += 0.5*math.cos((self.rotation+math.pi/2))

#HWWWWW:
#    Find out who walter Payton was