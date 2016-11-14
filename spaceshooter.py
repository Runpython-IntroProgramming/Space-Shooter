"""
spaceshooter.py
Author: vinzentmoesch
Credit: 
http://freegameassets.blogspot.com/2013/09/asteroids-and-planets-if-you-needed-to.html

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
import random
zufaellig = round((random.random())*100)
#Hintergrund
class Stars(Sprite):

    asset = ImageAsset("images/starswithoutspacesmall.jpg")
    width = 7485
    height = 4930

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        self.scale = 0.23
        
class astroid(Sprite):
    asset = ImageAsset("images/asteroid1.png",
        Frame(0,0,72,72), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(astroid.asset, position)    
        self.avx = 0
        self.avy = 0
        self.avr = 1
        self.random1 = round((random.random())*100)
        self.ranom2 = round((random.random())*10)
        number = 0
    def step(self):
        if number >= random1:
            self.avx = random1
            number = 0
        number += 12
        
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/UFO2.png", 
        Frame(0,0,485,490), 6, 'vertical')
    

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.scale = 0.15
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrustL = 0
        self.thrustR = 0
        self.thrustU = 0
        self.thrustD = 0
        self.panic = 0
        self.thrustframe = 1
        self.imagenumber = 0
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLOn)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustROn)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustROff)
        SpaceGame.listenKeyEvent("keydown", "p", self.panicOn)
        SpaceGame.listenKeyEvent("keyup", "p", self.panicOff)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUOff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDOn)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDOff)


        self.fxcenter = self.fycenter = 0.5

    def step(self):
        if self.thrustL == 1:
            self.vx -= 0.06
        if self.thrustR == 1:
            self.vx += 0.06
        if self.thrustU == 1:
            self.vy -= 0.06
        if self.thrustD == 1:
            self.vy += 0.06
        if self.panic == 1:
            self.vx = 0
            self.vy = 0
            self.panic = 0
        if self.panic == -1:
            self.vx = 0
            self.vy = 0
            self.panic = 0
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrustL == 1 or self.thrustR == 1 or self.thrustU == 1 or self.thrustD == 1 or self.panic == 1:
            self.setImage(self.thrustframe)
            self.imagenumber += 1
            if self.imagenumber == 9:
                self.thrustframe += 1
                self.imagenumber = 0
                if self.thrustframe == 7:
                    self.thrustframe = 2
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
    
    def panicOn(self, event):
        self.panic = 1
        
    def panicOff(self, event):
        self.panic = -1
    

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        Stars((0,0))
        SpaceShip((500,500))
        astroid((0,0))


    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for Bstroid in self.getSpritesbyClass(astroid):
            Bstroid.step()


myapp = SpaceGame(1900, 950)
myapp.run()