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
import math

SCREEN_WIDTH = 1536   #dimensions from jeffffff
SCREEN_HEIGHT = 1024

class Ship1(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship1.image, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.thrust=0
        SpaceGame.listenKeyEvent("keydown","w", self.moveForward)
        SpaceGame.listenKeyEvent("keyup","w", self.NomoveForward)
        SpaceGame.listenKeyEvent("keydown","a",self.turnLeft)
        SpaceGame.listenKeyEvent("keyup","a",self.NoturnLeft)
        SpaceGame.listenKeyEvent("keydown","d", self.turnRight)
        SpaceGame.listenKeyEvent("keyup","d", self.NoturnRight)
        self.fxcenter = 0.5
        self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.movar
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrust)
            self.thrust += 1
            if self.thrust == 4:
                self.thrust = 1
        else:
            self.setImage(0)
    
    def movar(self):
        

    def moveForward(self, event):
        self.thrust = 1
        
    def NomoveForward(self, event):
        self.thrust=0

    def turnLeft(self,event):
        self.vr=0.05

    def NoturnLeft(self,event):
        self.vr=0

    def turnRight(self, event):
        self.vr=-0.05
        
    def NoturnRight(self,event):
        self.vr=0
        
        
class Sh(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship2.image, position)
        self.Vx=0
        self.vy=0
        self.vr=0
        self.thrust=0
        SpaceGame.listenKeyEvent("keydown","i", self.moveforward)
        SpaceGame.listenKeyEvent("keyup","i", self.Nomoveforward)
        SpaceGame.listenKeyEvent("keydown","j",self.turnleft)
        SpaceGame.listenKeyEvent("keyup","j",self.Noturnleft)
        SpaceGame.listenKeyEvent("keydown","l", self.turnright)
        SpaceGame.listenKeyEvent("keyup","l", self.Noturnright)
        self.fxcenter = 0.5
        self.fycenter = 0.5

    def step(self):
        self.x += self.Vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrust)
            self.thrust += 1
            if self.thrust == 4:
                self.thrust = 1
        else:
            self.setImage(0)

    def moveforward(self, event):
        self.thrust = 1
        
    def Nomoveforward(self, event):
        self.thrust=0

    def turnleft(self,event):
        self.vr=0.05

    def Noturnleft(self,event):
        self.vr=0

    def turnright(self, event):
        self.vr=-0.05
        
    def Noturnright(self,event):
        self.vr=0

class Sun(Sprite):
    image=ImageAsset("images/sun.png")
    height=400
    wdth=400
    def __init__(self, position):
        super().__init__(Sun.image, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        suhan=ImageAsset("images/starfield.jpg")
        jeff=Sprite(suhan,(0,0))
        jeff1=Sprite(suhan,(512,512))
        jeff2=Sprite(suhan,(0,512))
        jeff3=Sprite(suhan,(512,0))
        jeff4=Sprite(suhan,(1024,512))
        jeff5=Sprite(suhan,(1024,0))        #got the dimensions from Jeff
        jeff6=Sprite(suhan,(0,1024))
        jeff7=Sprite(suhan,(1024,2014))
        jeff8=Sprite(suhan,(512,1024))
        
        Ship((300,400))
        Ship1((1000,400))

        Sun((650,500))
        Sun((450,200))
        Sun((199,54))
        Sun((478,400))
        Sun((900,900))
        Sun((20,350))
        Sun((900,90))
        Sun((800,700))
        Sun((347,784))
        Sun((1000,1100))
        Sun((1500,1000))
        Sun((1300,600))
        Sun((1199,400))
        Sun((340,1000))
        Sun((1250,900))
        Sun((1500,900))
        Sun((100,1000))
        Sun((1200,1350))
        Sun((700,200))
        Sun((950,800))

    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
      
#Fin
myapp = SpaceGame(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()