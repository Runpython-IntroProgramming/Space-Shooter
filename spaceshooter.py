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
        super().__init__(Ship.image, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.trust=0
        self.trustframe=0
        SpaceGame.listenKeyEvent("keydown", self.thrustOff)
        SpaceGame.listenKeyEvent("keyup", self.thrustOn)
        SpaceGame.listenKeyEvent("keyleft",self.turnLeft)
        Spacegame.listenKeyEvent("keyright", self.turnRight)
        self.fxcenter = self.fycenter = 0.5

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

    def turnLeft(self,event):
        self.vr

    def turnRight(self, event):
        self.vr=

class Sun(Sprite):
    image=ImageAsset("images/sun.png", Frame(100,0,100,100), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Sun.asset, position)
    self.fxcenter = 0
    self.fycenter = 0
    self.circularCollisionModel()

class Galaxy(Sprite):
    image=ImageAsset("images/starfield.jpg", Frame(600,0,1000,125), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Galaxy.image, position)

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        back=Sprite(Ship(0,0))
        SpaceShip(500,600)
        SpaceShip(550,650)
        SpaceShip(600,700)

    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()

#Fin
myapp = SpaceGame(0,0)
myapp.run