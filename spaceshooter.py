"""
spaceshooter.py
Author: Adam Pikielny
Credit: Morgan
Roger
ggame documentation
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')


    def __init__(self, position, app):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        #explosionTime=0
        #self.img=img
        self.app = app
        #self.vr = math.atan(self.vy/self.vx)
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.moveleft)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.moveright)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.moveforward)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.movebackward)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
        #if self.collidingWith(sun)==True:
            #self.stop
    """imageNum=1       
    if imageNum==1:
        asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    if imageNum==2:
        asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(500,0,292-227,125), 4, 'horizontal')"""

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation = self.vr
        if self.thrust==1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        #if self.vy!=0:
            #self.rotation = -1*math.pi+math.atan(self.vx/self.vy)
            
        #is the below function in the write step?
        #if collidingWithSprites(self)==True:
            #print("collision")
        if self.collidingWith(self.app.sun)==True:
            self.explode()
    def moveleft(self,event):
        self.vr+=.4
    def moveright(self,event):
        self.vr-=.4
    def moveforward(self,event):
        self.vy+=(-.3*(math.cos(self.rotation)))
        self.vx+=(-.3*(math.sin(self.rotation)))
    def movebackward(self,event):
        self.vy+=(.3*(math.cos(self.rotation)))
        self.vx+=(.3*(math.sin(self.rotation)))

    
    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    
    def explode(self):
        explosion(self.position)
        self.destroy()
    
#class Ship1(SpaceShip):
    #def __init__():
    
class explosion(Sprite):
    asset = ImageAsset("images/explosion2.png", Frame(0,0,192-0,195), 25, 'horizontal')
    def __init__(self, position):
        super().__init__(explosion.asset, position)
        self.FrameNum=0
        self.speed=0.0
    def step(self):
        self.setImage(self.FrameNum)
        self.speed+=0.2
        self.FrameNum=int(self.speed)
        self.FrameNum += 1
        if self.FrameNum==25:
            self.destroy()
        #if self.FrameNum == 4:
            #self.FrameNum = 1
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #bg_asset = RectangleAsset(width, height, noline, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg=Sprite(bg_asset,(0,0))
        sun_asset = ImageAsset("images/sun.png")
        self.sun=Sprite(sun_asset, (200,200))
        SpaceShip((100,100), self)
        #SpaceShip((200,100), self, 2)

        #SpaceShip((150,150))
        #SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explode in self.getSpritesbyClass(explosion):
            explode.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()