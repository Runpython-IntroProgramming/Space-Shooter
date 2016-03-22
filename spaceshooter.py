"""
spaceshooter.py
Author: Daniel Wilson
Credit: 

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.UPON)
        SpaceGame.listenKeyEvent("keyup", "s", self.stop)
        SpaceGame.listenKeyEvent("keydown", "w", self.DOWNON)
        SpaceGame.listenKeyEvent("keyup", "w", self.stop)
        SpaceGame.listenKeyEvent("keydown", "a", self.Left)
        SpaceGame.listenKeyEvent("keyup", "a", self.stop)
        SpaceGame.listenKeyEvent("keydown", "d", self.Right)
        SpaceGame.listenKeyEvent("keyup", "d", self.stop)
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

    def UPON(self, event):
        self.vy=1
    def DOWNON(self, event):
        self.vy=-1
    def Right(self, event):
        self.vx = 1
    def Left(self, event):
        self.vx = -1
    def stop(self, event):
        self.vy=0
        self.vx=0
    


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg1 = Sprite(bg_asset, (0,0))
        bg2 = Sprite(bg_asset, (512,0))
        bg3 = Sprite(bg_asset, (0, 512))
        bg4 = Sprite(bg_asset, (512, 512)) 
        bg5 = Sprite(bg_asset, (1024, 512))
        bg6 = Sprite(bg_asset, (1024, 0))
        SpaceShip((100,100))
        SpaceShip((500,100))

        

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


def registerKeys(self, keys):
        commands = ["left", "right", "forward", "fire"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
       

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()