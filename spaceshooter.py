"""
spaceshooter.py
Author: Marcus Helble
Credit: None

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 910
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



space_asset= ImageAsset("images/starfield.jpg",)
space=Sprite(space_asset, (0,0))
space2=Sprite(space_asset, (512,0))
space3=Sprite(space_asset,(1024,0))
space4=Sprite(space_asset, (0,512))
space5=Sprite(space_asset, (512,512))
space6=Sprite(space_asset, (1024, 512))
class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.leftKey)
        SpaceGame.listenKeyEvent("keydown", "d", self.rightKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.upKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.downKey)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
    

   

    def leftKey(self, event):
        SpaceShip.go = True
        SpaceShip.ygo= False
        SpaceShip.thrust = 1
        SpaceShip.rotation=(pi/2)
        left(SpaceShip)



    def rightKey(self, event):
        SpaceShip.go = True
        SpaceShip.ygo=False
        SpaceShip.thrust = 1
        SpaceShip.rotation=(pi/2)
        right(SpaceShip)
  
    def upKey(self, event):
        SpaceShip.ygo = True
        SpaceShip.go=False
        SpaceShip.thrust = 1
        SpaceShip.rotation=0
        up(SpaceShip)
  
    def downKey (self, event):
        SpaceShip.ygo = True
        SpaceShip.go = False
        SpaceShip.thrust = 1
        SpaceShip.rotation=pi
        down(SpaceShip)


class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/kSQdCxM.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 0.6
        SpaceShip((125,100))
        SpaceShip((175,150))
        SpaceShip((75,150))
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()