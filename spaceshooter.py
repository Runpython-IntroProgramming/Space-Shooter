"""
spaceshooter.py
Author: Liam
Credit: http://stackoverflow.com/questions/16442923/how-to-insert-an-image-in-python,
http://stackoverflow.com/questions/28553439/python-pygame-how-would-i-get-my-sprite-to-rotate-in-the-direction-its-moving
https://upload.wikimedia.org/wikipedia/commons/8/86/Asteroid1.png
https://docs.python.org/3/library/random.html#random.random
http://people.mozilla.org/~jmuizelaar/webgl-worse/asteroid.png

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 930
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679


class SpaceShip(Sprite):
    #Animated space ship
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
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
        #SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        #SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.moveL)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.moveR)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.moveD)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.moveU)
        
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.nMoveL) #stop moving to the left
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.nMoveR) #stop moving to the right
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.nMoveD) #stop moving down
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.nMoveU) #stop moving up
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation = 0
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        
        #x motion
        if self.rxa == 2 and self.rxb == 2:
            self.x=self.x
            self.c = 0 #don't set rotation based on x motion
        else:
            if self.rx == -5: #moving left
                self.x=self.x-10
                self.c=1
            if self.rx == 5: #moving right
                self.x=self.x+10
                self.c=2
        #y motion
        if self.rya == 2 and self.ryb == 2:
            self.y=self.y
            self.d = 0 #don't set rotation based on y motion
        else:
            if self.ry == -5: #moving up
                self.y=self.y-10
                self.d = 1
            if self.ry == 5: #moving down
                self.y=self.y+10
                self.d = 2
        
        #thrust
        if self.rxa == 2 and self.rxb == 2 and self.rya == 2 and self.ryb == 2:
            self.thrust = 0
        else:
            self.thrust = 1
        #rotation
        
        if self.c==0 and self.d==0:
            self.rotation = 0
        else:
            if self.c==1: #if it's moving left
                if self.d==1: #moving up
                    self.rotation=(1/4)*pi
                elif self.d==2: #down
                    self.rotation=(3/4)*pi
                else:
                    self.rotation=pi/2
            if self.c==2: #if it's moving right
                if self.d==1: #moving up
                    self.rotation=(7/4)*pi
                elif self.d==2: #down
                    self.rotation=(5/4)*pi
                else:
                    self.rotation=(3/2)*pi
            else:
                if d==1: #moving up
                    self.rotation=0
                elif d==2: #down
                    self.rotation=pi
    
    def thrustOn(self, event):
        self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def moveL(self,event):
        self.rx = -5
        self.rxa=0
    def moveR(self,event):
        self.rx = 5
        self.rxb=0
    def moveD(self,event):
        self.ry = 5
        self.rya=0
    def moveU(self,event):
        self.ry = -5
        self.ryb=0
    
    def nMoveL(self,event):
        self.rxa = 2
    def nMoveR(self,event):
        self.rxb = 2
    def nMoveD(self,event):
        self.rya = 2
    def nMoveU(self,event):
        self.ryb = 2    

class Asteroid(Sprite):
    asset = ImageAsset("images/Asteroid2_spritesht.png",
        Frame(256,0,128,128), 8, 'vertical')
    def __init__(self,im_num,position):
        super().__init__(Asteroid.asset, position)
        self.setImage(im_num)

    
class SpaceGame(App):
    #Tutorial4 space game example.
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/kSQdCxM.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 0.6
        SpaceShip((125,100))
        SpaceShip((225,200))
        SpaceShip((25,200))
        SpaceShip((175,150))
        SpaceShip((75,150))
        Asteroid(1,(200,400))
        for a in range(8):
            x=random()
            x=x*1400 + 100
            y=random()
            y=y*800 + 100
            pos=(x,y)
            Asteroid(a,pos)
            #print("Aster(" + str(x) + " " + str(y) + ")")
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()