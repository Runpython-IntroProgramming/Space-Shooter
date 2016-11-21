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
        self.Spin=0
        self.Spinning=0
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
        SpaceGame.listenKeyEvent("keydown", "o", self.Rotateclock)
        SpaceGame.listenKeyEvent("keyup", "o", self.Rotateclockstop)
        SpaceGame.listenKeyEvent("keydown", "p", self.Rotatecounterclock)
        SpaceGame.listenKeyEvent("keyup", "p", self.Rotatecounterclockstop)
        
        self.fxcenter=self.fycenter=.5
    def step(self):
        if self.Spin==1:
            self.Spinning=.1
        if self.Spin==-1:
            self.Spinning=-.1
        if self.Spin==0:
            self.Spinning=0
        self.rotation+=self.Spinning
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
    def Rotateclock(self, event):
        self.Spin=1
    def Rotateclockstop(self, event):
        self.Spin=0
    def Rotatecounterclock(self, event):
        self.Spin=-1
    def Rotatecounterclockstop(self, event):
        self.Spin=0
class Star(Sprite):
    asset=ImageAsset("images/sun.png")
    height=300
    width=300
    def __init__(self, position):
        super().__init__(Star.asset, position)
    self.counter=0
    self.Starx=0
    self.Stary=0
    
    def step(self):
        if self.counter>=0 and self.counter<=1200:
            self.Starx=1
            self.Stary=0
        if self.counter>=1201 and self.counter<=2400:
            self.Starx=0
            self.Stary=-1
        if self.counter>=2401 and self.counter<=3600:
            self.Starx=-1
            self.Stary=0
        if self.counter>=3601 and self.counter<=4800:
            self.Starx=0
            self.Stary=1
        if self.counter==4801:
            self.counter=0
        self.counter+=1
        self.x=self.x+self.Starx
        self.y=self.y+self.Stary
class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        Spaceship((100, 100))
        Star((800, 450))
    def step(self):
        for ship in self.getSpritesbyClass(Spaceship):
            ship.step()

app = SpaceGame(1897, 935)
app.run()