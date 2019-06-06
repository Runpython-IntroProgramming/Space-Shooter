"""
spaceshooter.py
Author: Andrew
Credit: Matt, Source Code 

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset, Color, LineStyle
from math import sin, cos
import math
from time import time

width = 1250
height = 700

myapp = App()

class SpaceShip(Sprite):
 
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0.1
        self.vy = 0.1
        self.vr = 0.01
        self.v = 0
        self.thrust = 0.5
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thruston)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustoff)
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
        self.rotation += self.vr
        colision = self.collidingWithSprites(chungus)
        if colision:
            self.explode(self)
            self.visible = False
            self.v = 0
            self.rotation = 0
            self.thrust = 0
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
                self.thrust = 10.0
                self.imagex = 1 
                self.setImage(self.imagex)
    def controlup(self, event):
        command = self.keymap[event.key]
        if command == "forward":
            self.thrust = 0
            self.imagex = 0 
            self.setImage(self.imagex)
    def explode(self, event):
        self.visible = False
        self.vx = 0
        self.vy = 0
        explosionn(self.position)


class explosionn(Sprite):
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    def __init__(self, position):
        super().__init__(explosionn.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
    def step(self):
        self.setImage(self.image//2)
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()
    
class SpaceGame(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        asset = ImageAsset("images/starfield.jpg")
        Sprite(asset,(0,0))
        Sprite(asset,(512,0))
        Sprite(asset,(0, 512))
        Sprite(asset,(512, 512)) 
        Sprite(asset,(1024, 512))
        Sprite(asset,(1024, 0))
        SpaceShip((100,100))
        chungus((300,200))
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explosion in self.getSpritesbyClass(explosionn):
            explosion.step()

    def register(self, keys):
        commands= ["left", "right", "forward"]
        self.keymap= dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
    


class chungus(Sprite):
    asset = ImageAsset("images/98a.png")
    def __init__(self, position):
        super().__init__(chungus.asset, position)
        self.scale = 0.35


myapp = SpaceGame(width, height)
myapp.run()