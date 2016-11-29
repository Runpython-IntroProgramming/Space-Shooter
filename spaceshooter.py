"""
spaceshooter.py
Author: Marcus Helble
Credit: Wilson Rimberg

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 910
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



space_asset= ImageAsset("images/starfield.jpg",)
backg=Sprite(space_asset, (0,0))
backg2=Sprite(space_asset, (512,0))
backg3=Sprite(space_asset,(1024,0))
backg4=Sprite(space_asset, (0,512))
backg5=Sprite(space_asset, (512,512))
backg6=Sprite(space_asset, (1024, 512))
class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.rx = 1
        self.ry = -1
        self.rxa = 0
        self.rxb = 0
        self.rya = 0
        self.ryb = 0
        self.c = 0
        self.d = 0
        self.visible = True
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.left)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.stopleft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.right)
        SoaceGame.listenKeyEvent("keyup", "right arrow", self.stopright)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.up)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.stopup)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.down)
        Game.listenKeyEvent("keyup", "down arrow", self.stopdown)
        
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.rotation = 0
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

    


class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/kSQdCxM.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 0.6
        SpaceShip((125,100))
        SpaceShip((175,150))
        SpaceShip((75,150))
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()