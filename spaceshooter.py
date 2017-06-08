"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math 
 
class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 505
    height = 505

    def __init__(self, position):
        super().__init__(Stars.asset, position)
 
class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(160,0,292-227,125), 4, 'vertical')
 
    def __init__(self, position, s):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrust = 0
        self.thrustframe = 1
        self.sun = s
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn) 
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.goup)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.turnright)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.turnleft)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.goback)
 
        self.fxcenter = self.fycenter = 0.5
 
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation = self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        if self.collidingWith(self.sun):
            self.explode()
             
    def thrustOn(self, event):
        self.thrust = 1
 
    def thrustOff(self, event):
        self.thrust = 0
         
    def goup(self, event):
        self.vy+=(-.3*(math.cos(self.rotation)))
        self.vx+=(-.3*(math.sin(self.rotation)))
         
    def goback(self, event):
        self.vy+=(.3*(math.cos(self.rotation)))
        self.vx+=(.3*(math.sin(self.rotation)))
         
    def turnright(self, event):
        self.vr-=.4
 
    def turnleft(self, event):
        self.vr+=.4

    def explode(self):
        explosion(self.position)
        self.destroy()

class explosion(Sprite):
    asset = ImageAsset("images/explosion2.png", Frame(0,0,192-0,195), 25, 'horizontal')
    def __init__(self, position):
        super().__init__(explosion.asset, position)
        self.explosion = 0 
        self.explosionframe = 1
    def step(self):
        self.setImage(self.explosionframe)
        self.explosionframe +=1
        if self.explosionframe ==25:
            self.destroy()

class SpaceGame(App):

    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))
        black = Color(0, 1)
        noline = LineStyle(0, black)
        s_asset = ImageAsset("images/sun.png")
        s = Sprite(s_asset, (600,235))
        SpaceShip((100,100),s)

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explode in self.getSpritesbyClass(explosion):
            explode.step()
         

 
myapp = SpaceGame(0,0)
myapp.run()
