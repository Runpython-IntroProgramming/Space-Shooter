"""
spaceshooter.py
Author: emBrileg08
Credit: Spacewar Source Code
www.pythoncentral.io for information on random number generation

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
import random

class Background(Sprite):
    def __init__(self,position):
        asset=ImageAsset("images/starfield.jpg")
        super().__init__(asset,position)
    width=512
    height=512

class Sun(Sprite):
     def __init__(self,position):
        asset=ImageAsset("images/sun.png")
        super().__init__(asset,position)
    
    
class Spaceship(Sprite):
    def __init__(self, position):
        asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
            Frame(227,0,65,125), 4, 'vertical')
        super().__init__(asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        self.thrust = 0
        self.thrustframe = 1
        Spacewar.listenKeyEvent("keydown","space", self.thrustOn)
        Spacewar.listenKeyEvent("keyup","space", self.thrustOff)
        print(self.thrust)
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

class Spacewar(App):
    def __init__(self):
        super().__init__()
        z=0
        a=0
        while z<self.width:
            Background((z,0))
            while a<self.height:
                Background((z,a))
                a+=Background.height
            a=0
            z+=Background.width
        Spaceship((100,100))
        for x in range(int(input("Set difficulty level, 0-20 "))):
            Sun((random.randint(0,self.width),random.randint(0,self.height)))
    def step(self):
        for ship in self.getSpritesbyClass(Spaceship):
            ship.step()
    
myapp=Spacewar()
myapp.run()