"""
spaceshooter.py
Author: Jeff
Credit: Space Game tutorial

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rrOff)
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
        self.vx = math.sin(math.pi * abs(self.rotation))
        self.vy = math.cos(math.pi * abs(self.rotation))

    def thrustOff(self, event):
        self.thrust = 0
        self.vx = 0
        self.vy = 0
        
    def rotateLeft(self, event):
        self.vr = 0.05
        
    def lrOff(self,  event):
        self.vr = 0
        
    def rotateRight(self, event):
        self.vr = -0.05
        
    def rrOff(self,  event):
        self.vr = 0
class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg1 = Sprite(bg_asset, (512,512))
        bg2 = Sprite(bg_asset, (0,512))
        bg3 = Sprite(bg_asset, (512,0))
        bg4 = Sprite(bg_asset, (1024,512))
        bg5 = Sprite(bg_asset, (1024,0))
        
        SpaceShip((200,200))
        SpaceShip((250,250))
        SpaceShip((300,150))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
