"""
spaceshooter.py
Author: Suhan Gui
Credit: Spacewar
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import TextAsset, Color
import math
from time import time

class Move(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(100,0,225,125), 4,'vertical')
    def __init__(self, position):
        super().__init__(Move.asset, position)

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov.png", Frame(100,0,225,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.trust=0
        self.trustframe=0
        SpaceGame.listenKeyEvent("keydown", self.thrustOff)
        SpaceGame.listenKeyEvent("keyup", self.thrustOn)
        self.fxcenter = self.fycenter = 0.5

class Sun(Sprite):
    image=ImageAsset("images/sun.png", Frame(100,0,100,100), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Sun.asset, position)

class Galaxy(Sprite):
    image=ImageAsset("images/starfield.jpg", Frame(600,0,1000,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Galaxy.asset, position)

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        

#Fin
myapp = SpaceGame(0,0)
myapp.run