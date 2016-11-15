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
        self.Velocityspaceshipdown=0
        self.Velocityspaceshipup=0
        self.Rotatespaceship=0
        self.Truerotation=0
        SpaceGame.listenKeyEvent("keydown", "space", self.Engineon)
        SpaceGame.listenKeyEvent("keyup", "space", self.Engineoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.Velocityright)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.Velocityrightstop)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.Velocityleft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.Velocityleftstop)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.Velocitydown)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.Velocitydownstop)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.Velocityup)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.Velocityupstop)
        SpaceGame.listenKeyEvent("keydown", "p", self.Rotateright)
        SpaceGame.listenKeyEvent("keyup", "p", self.Rotaterightstop)
        SpaceGame.listenKeyEvent("keydown", "o", self.Rotateleft)
        SpaceGame.listenKeyEvent("keyup", "o", self.Rotateleftstop)
    def step(self):
        if self.Rotatespaceship==1:
            self.Truerotation=.3
        elif self.Rotationspaceship==-1:
            self.Truerotation=-.3
        else:
            self.Truerotation=0
        self.rotation+=self.Truerotation
        if self.Velocityspaceshipup==1:
            self.y=self.y+2
        else:
            self.y=self.y
        if self.Velocityspaceshipdown==1:
            self.y=self.y-2
        else:
            self.y=self.y
        if self.Velocityspaceshipright==1:
            self.x=self.x+2
        else:
            self.x=self.x
        if self.Velocityspaceshipleft==1:
            self.x=self.x-2
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
    def Velocitydown(self, event):
        self.Velocityspaceshipup=1
    def Velocitydownstop(self, event):
        self.Velocityspaceshipup=0
    def Velocityup(self, event):
        self.Velocityspaceshipdown=1
    def Velocityupstop(self, event):
        self.Velocityspaceshipdown=0
    def Rotateright(self, event):
        self.Rotatespaceship=1
    def Rotaterightstop(self, event):
        self.Rotatespaceship=0
    def Rotateleft(self, event):
        self.Rotatespaceship=-1
    def Rotateleftstop(self, event):
        self.Rotatespaceship=0
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