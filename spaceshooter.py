"""
spaceshooter.py
Author: maBottnn14
Credit: Andrew

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset
import math
from time import time

myapp = App()

#Starfield
class Stars(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512
    
    def __init__(self, position):
        super().__init__(Stars.asset, position)
#Monster
class monster(Sprite):
    op = ImageAsset("images/Alienblue.gif")
    width = 50
    height = 50
    
    def __init__(self, position):
        super().__init__(monster.op, position)
        self.scale = 0.36
#Space ship
class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.02
        self.thrust = 0
        self.thrustframe = 1
        self.fxcenter = self.fycenter = 0.5
    
    def step(self, monster):
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            self.x += -sin(self.rotation)
            self.y += -cos(self.rotation)
            if self.collidingWith(monster):
                self.destroy()
        else:
            self.setImage(0)
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def TurnLOn(self, event):
        self.rotation += self.vr
        
    def TurnROn(self, event):
        self.rotation -= self.vr
    
Stars((512,0))
Stars((0,0))
Stars((1024,0))
Stars((0,512))
Stars((512,512))
Stars((1024,512))
SpaceShip((400,450))        
monster((500,200))
class SpaceGame(App):

    def __init__(self):
        super().__init__()
        hi = ImageAsset("images/Alienblue.gif")
        hello = ImageAsset("images/Alienblue.gif")
        
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step(self.hello_sprite)

myapp.listenKeyEvent('keydown', 'w', myapp.ship.thrustOn)
myapp.listenKeyEvent('keyup', '1', myapp.ship.thrustOff)
myapp.listenKeyEvent('keydown', 'a', myapp.ship.TurnLOn)
myapp.listenKeyEvent('keydown', 'd', myapp.ship.TurnROn)
myapp.run()
