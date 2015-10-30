"""
spaceshooter.py
Author: Suhan Gui
Credit: Spacewar, jeeffff
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, Color, RectangleAsset, LineStyle

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.image, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.thrust=0
        self.thrustframe=0
        SpaceGame.listenKeyEvent("keydown","s", self.moveBackward)
        SpaceGame.listenKeyEvent("keyup","s", self.NomoveBackward)
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
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrust)
            self.thrust += 1
            if self.thrust == 4:
                self.thrust = 1
        else:
            self.setImage(0)

    def moveFoward(self, event):
        self.thrust = -1
        
    def NomoveForward(self, event):
        self.thrust=0

    def moveBackward(self, event):
        self.thrust = 1
        
    def NomoveBackward(self,event):
        self.thrust=0

    def turnLeft(self,event):
        self.vr=1

    def NoturnLeft(self,event):
        self.vr=0

    def turnRight(self, event):
        self.vr=-1
        
    def NoturnRight(self,event):
        self,vr=0
        
class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.image, position)
        self.vx=0
        self.vy=0
        self.vr=0
        self.thrust=0
        self.thrustframe=0
        SpaceGame.listenKeyEvent("keydown","s", self.moveBackward)
        SpaceGame.listenKeyEvent("keyup","s", self.NomoveBackward)
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
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrust)
            self.thrust += 1
            if self.thrust == 4:
                self.thrust = 1
        else:
            self.setImage(0)

    def moveFoward(self, event):
        self.thrust = -1
        
    def NomoveForward(self, event):
        self.thrust=0

    def moveBackward(self, event):
        self.thrust = 1
        
    def NomoveBackward(self,event):
        self.thrust=0

    def turnLeft(self,event):
        self.vr=1

    def NoturnLeft(self,event):
        self.vr=0

    def turnRight(self, event):
        self.vr=-1
        
    def NoturnRight(self,event):
        self,vr=0

    
"""
class Sun(Sprite):
    image=ImageAsset("images/sun.png", Frame(100,0,100,100), 1, 'vertical')
    def __init__(self, position):
        super().__init__(Sun.image, position)
        self.fxcenter = 0
        self.fycenter = 0
        self.circularCollisionModel()
    
    def step(self):
       
"""

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black=Color(0,1)
        line=LineStyle(0,black)
        john=ImageAsset("images/starfield.jpg")
        jeff=Sprite(john,(0,0))
        jeff1=Sprite(john,(0,0))
        jeff2=Sprite(john,(0,0))
        jeff3=Sprite(john,(0,0))
        jeff4=Sprite(john,(0,0))
        jeff5=Sprite(john,(0,0))        #got the dimensions from jeefff
        Ship((500,600))

    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()

#Fin
myapp = SpaceGame(0,0)
myapp.run