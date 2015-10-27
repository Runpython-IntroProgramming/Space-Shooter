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

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(100,0,225,125), 4, 'vertical')
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

    def turnLeft(self,event):
        self.vr=0.5

    def turnRight(self, event):
        self.vr=0.5

class Sun(Sprite):
    image=ImageAsset("images/sun.png", Frame(100,0,100,100), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Sun.image, position)
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
        sun=Sprite(Sun(400,300))
        galaxy=Sprite(Galaxy(0,0))
        Ship(500,600)
        Ship(550,650)
        Ship(600,700)

    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()

#Fin
myapp = SpaceGame(0,0)
myapp.run