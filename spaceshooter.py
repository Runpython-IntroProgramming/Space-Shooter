"""
spaceshooter.py
Author: Jeff
Credit: Space Game tutorial

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

class SpaceShip(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rrOff)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self):
        self.rotation += self.vr
        self.VX += self.vx
        self.VY += self.vy
        self.x -= 0.1*self.VX
        self.y -= 0.1*self.VY
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            self.move()
        else:
            self.setImage(0)
    
    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)
    
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def rotateLeft(self, event):
        self.vr = 0.05
        
    def lrOff(self,  event):
        self.vr = 0
        
    def rotateRight(self, event):
        self.vr = -0.05
        
    def rrOff(self,  event):
        self.vr = 0

class Bullet(Sprite):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
    pewasset = SoundAsset("sounds/pew1.mp3")
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
    
class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg1 = Sprite(bg_asset, (512,512))
        bg2 = Sprite(bg_asset, (0,512))
        bg3 = Sprite(bg_asset, (512,0))
        bg4 = Sprite(bg_asset, (1024,512))
        bg5 = Sprite(bg_asset, (1024,0))
        
        SpaceShip((200,200))
        SpaceShip((250,250))
        SpaceShip((300,150))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
