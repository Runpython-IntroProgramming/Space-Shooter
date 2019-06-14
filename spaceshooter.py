"""
spaceshooter.py
Author: kyDoleuc04
Credit: Andrew, Matt, Tristan, Greg

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
from math import sin, cos
from time import time

width = 700
height = 500

class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Sun(Sprite):
    
    width = 80
    height = 76
    asset = ImageAsset("images/sun.png", Frame(0, 0, width, height))
    
    def __init__(self, position):
        super().__init__(Sun.asset, position, CircleAsset(32))
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5

class spaceship(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(spaceship.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0
        self.v = 0
        self.thrust = 0
        self.thrustframe = 1
        self.initposition = position
        SpaceGame.listenKeyEvent("keydown", "space", self.thruston)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustoff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.turnleft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.turnoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.turnright)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.turnoff)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        vx = -sin(self.rotation)*self.v
        vy = -cos(self.rotation)*self.v
        self.x += vx
        self.y += vy
        boom = self.collidingWithSprites(Sun)
        self.rotation += self.vr
        if self.x > myapp.width:
            self.x = 0
        if self.x < 0:
            self.x = myapp.width
        if self.y > myapp.height:
            self.y = 0
        if self.y < 0:
            self.y = myapp.height
        if len(boom) > 0:
            explosion((self.x,self.y))
            self.visible=False
            self.x = 300
            self.y = 200
            self.v = 0
            self.rotation = 0
            self.thrust = 0
            self.visible = True
        if self.thrust == 0 and self.v >= 0.1:
            self.v -= 0.1
        if self.thrust == 1 and self.v == 0:
            self.v = 1
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            if self.v < 12:
                self.v *= 1.1
        else:
            self.setImage(0)
    def thruston(self, event):
        self.thrust = 1
    def thrustoff(self, event):
        self.thrust = 0
    def turnleft(self, event):
        self.vr = 0.1
    def turnoff(self, event):
        self.vr = 0
    def turnright(self, event):
        self.vr = -0.1
    def controldown(self, event):
        if command == "forward":
                self.thrust = 40.0
                self.imagex = 1 
                self.setImage(self.imagex)
    def controlup(self, event):
        command = self.keymap[event.key]
        if command == "forward":
            self.thrust = 0.0
            self.imagex = 0 
            self.setImage(self.imagex)

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__()
        stars = Stars((0,0))
        stars.scale = self.width/stars.width
        self.ss = spaceship((300,200))
        Sun((self.width/2,self.height/2))


myapp = SpaceGame(width, height)
myapp.run()