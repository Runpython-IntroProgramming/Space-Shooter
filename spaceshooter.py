"""
spaceshooter.py
Author: Bauti Gallino
Credit: Liam S.

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

class Background(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    height= 512
    width= 512
    
    def __init__(self, position):
        super().__init__(Background.asset, position)

class Spaceship(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Spaceship.asset, position)
        self.Engineframe=1
        self.Thrust=0
        self.Velocityspaceshipright=0
        self.Velocityspaceshipleft=0
        SpaceGame.listenKeyEvent("keydown", "space", self.Engineon)
        SpaceGame.listenKeyEvent("keyup", "space", self.Engineoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.Velocityright)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.Velocityrightstop)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.Velocityleft)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.Velocityleftstop)
    def step(self):
        if self.Velocityspaceshipright==1:
            self.x=self.x+1
        else:
            self.x=self.x
        if self.Velocityspaceshipleft==1:
            self.x=self.x-1
        else:
            self.x=self.x
        if self.Thrust == 1:
            self.setImage(self.Engineframe)
            self.Engineframe = self.Engineframe + 1
            if self.Engineframe == 4:
                self.Engineframe = 1
        else:
            self.setImage(0)
    def Engineon(self, event):
        self.Thrust=1
    def Engineoff(self, event):
        self.Thrust=0
        self.Engineframe=1
    def Velocityright(self, event):
        self.Velocityspaceshipright=1
    def Velocityrightstop(self, event):
        self.Velocityspaceshipright=0
    def Velocityleft(self, event):
        self.Velocityspaceshipleft=1
    def Velocityleftstop(self, event):
        self.Velocityspaceshipleft=0
class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        Spaceship((0, 0))
    def step(self):
        for ship in self.getSpritesbyClass(Spaceship):
            ship.step()

app = SpaceGame(1897, 935)
app.run()
"""
super().__init__(width, height)
    for x in range(self.width//Background.width + 1):
        for y in range(self.height//Background.height + 1):
            Background((x*Background.width, y*Background.height))
"""
