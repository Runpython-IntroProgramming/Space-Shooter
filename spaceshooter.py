"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame
import math, random
from time import time
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        for i in range (1,100):
            white=Color(0xbbbb00,1)
            starline=LineStyle(2,white)
            star_asset =RectangleAsset(10, 10, starline, white)
            star = Sprite(star_asset, ((random.randint(0,1000)),(random.randint(0,1000))))
            SpaceShip((100,100))
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0

myapp = SpaceGame()
myapp.run()

