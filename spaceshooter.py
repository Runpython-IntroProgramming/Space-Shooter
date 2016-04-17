"""
spaceshooter.py
Author: Suhan Gui
Credit: Spacewar, Jeff
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset
from ggame import Frame, Color, RectangleAsset, LineStyle
import time
import math

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 860

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.image, position)
        self.vy=0
        self.vr=0
        self.vx=0
        self.thrust=0
        self.thrust1=1
        SpaceGame.listenKeyEvent("keydown","w", self.moveForward)
        SpaceGame.listenKeyEvent("keyup","w", self.NomoveForward)
        SpaceGame.listenKeyEvent("keydown","a",self.turnLeft)
        SpaceGame.listenKeyEvent("keyup","a",self.NoturnLeft)
        SpaceGame.listenKeyEvent("keydown","d", self.turnRight)
        SpaceGame.listenKeyEvent("keyup","d", self.NoturnRight)
        self.fxcenter = 0.5
        self.fycenter = 0.5

    def step(self):
        self.y += self.vy
        self.x += self.vx
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrust1)
            self.thrust += 1
            if self.thrust == 4:
                self.thrust = 1
        else:
            self.setImage(0)
        
        collision = self.collidingWithSprites(Sip)
        if len(collision):
            if collision[0].visible:
                collision[0].destroy()
                self.rekt()
                
        collision = self.collidingWithSprites(Sun)
        if len(collision):
            if collision[0].visible:
                collision[0].destroy()
                self.rekt()
                
    def moveForward(self, event):
        self.thrust = 1
        self.boris=math.sin(self.rotation)     #math skills from Jeff
        self.moris=math.cos(self.rotation)
        self.vx = -3*self.boris
        self.vy = -3*self.moris
        
    def NomoveForward(self, event):
        self.thrust=0
        self.vy=0
        self.vx=0

    def turnLeft(self,event):
        self.vr=0.1

    def NoturnLeft(self,event):
        self.vr=0

    def turnRight(self, event):
        self.vr=-0.1
        
    def NoturnRight(self,event):
        self.vr=0

    def rekt(self):
        self.appear=False
        BigExplosion(self.position)
        self.destroy()
    
class Sip(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(158,0,71,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Sip.image, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.frame=0
        self.thrustframe=1
        SpaceGame.listenKeyEvent("keydown","i", self.moveforward)
        SpaceGame.listenKeyEvent("keyup","i", self.Nomoveforward)
        SpaceGame.listenKeyEvent("keydown","j",self.turnleft)
        SpaceGame.listenKeyEvent("keyup","j",self.Noturnleft)
        SpaceGame.listenKeyEvent("keydown","l", self.turnright)
        SpaceGame.listenKeyEvent("keyup","l", self.Noturnright)
        self.fxcenter = 0.5
        self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.frame == 1:
            self.setImage(self.thrustframe)
            self.frame += 1
            if self.frame == 4:
                self.frame = 1
        else:
            self.setImage(0)
        
        collision = self.collidingWithSprites(Ship)
        if len(collision):
            if collision[0].visible:
                collision[0].destroy()
                self.rekt()
                
        collision = self.collidingWithSprites(Sun)
        if len(collision):
            if collision[0].visible:
                collision[0].destroy()
                self.rekt()
                self.destroy

    def moveforward(self, event):
        self.frame = 1
        self.boris=math.sin(self.rotation)     #math skills from Jeff
        self.moris=math.cos(self.rotation)
        self.vx = -3*self.boris
        self.vy = -3*self.moris
        
    def Nomoveforward(self, event):
        self.frame=0
        self.vy=0
        self.vx=0

    def turnleft(self,event):
        self.vr=0.1

    def Noturnleft(self,event):
        self.vr=0

    def turnright(self, event):
        self.vr=-0.1
        
    def Noturnright(self,event):
        self.vr=0

    def rekt(self):
        self.appear=False
        BigExplosion(self.position)
        self.destroy()

class Sun(Sprite):
    image=ImageAsset("images/sun.png")
    def __init__(self, position):
        super().__init__(Sun.image, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()

class BigExplosion(Sprite):
    image=ImageAsset("images/explosion2.png", Frame(0,0,192,195), 25)
    def __init__(self, position):
        super().__init__(BigExplosion.image, position)
        self.frame=0
        self.fxcenter = 0.5
        self.fycenter = 0.5
    
    def step(self):
        self.frame += 1
        if self.frame == 50:
            self.destroy()

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        suhan=ImageAsset("images/starfield.jpg")

        quiter=Sprite(suhan,(0,0))     #jjeeeefffffff
        quiter1=Sprite(suhan,(512,512))
        quiter2=Sprite(suhan,(0,512))
        quiter3=Sprite(suhan,(512,0))
        quiter4=Sprite(suhan,(1024,512))
        quiter5=Sprite(suhan,(1024,0))
        quiter6=Sprite(suhan,(0,1024))
        quiter10=Sprite(suhan,(512,2014))
        quiter11=Sprite(suhan,(1024,1024))
        quiter12=Sprite(suhan,(512,1024))
        quiter13=Sprite(suhan,(1024,512))
        
        Sun((700,430))
        Sun((500,600))
        Sun((500,250))
        Sun((900,600))
        Sun((900,250))
        Sun((700,760))
        Sun((700,100))

#SCREEN_WIDTH = 1400
#SCREEN_HEIGHT = 860
        Ship((400,430))
        Sip((1000,430))

    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
        for ship in self.getSpritesbyClass(Sip):
            ship.step()
        explosions = self.getSpritesbyClass(BigExplosion)
        for explosion in explosions:
            explosion.step()

#Fin
myapp = SpaceGame(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()