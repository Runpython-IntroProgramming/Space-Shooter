"""
spaceshooter.py
Author: Joe Richter
Credit: StackOverflow, Python documentation, ggame documentation, tutorials on the project, pull requests, example code, and Joe Richter.
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
"""
Plan:
Create a Space Shooter game.
How:
Include these sprites:
    Background
    Sun
    Rocket 1
    Rocket 2
    Bullet Sprite - with noise
    Thruster Sprite - with noise (I think)
    Explosion Sprite - with noise (I think)
Have movement:
    Control the rockets with arrow/WASD keys
    Make the rockets move, always
Have collisions:
    When the rocket enters a certain area around the center, make the rocket explode.
    When the rockets enter a certain area around another rocket, they both explode.
    Basically, make it so that IF a sprite has the same (X, Y) as another sprite, what has been hit explodes.
    
Start!
"""
SW = 1440
SH = 768
class Rocket1(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Rocket1.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceShootOut.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceShootOut.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceShootOut.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceShootOut.listenKeyEvent("keyup", "left arrow", self.lrOff)
        SpaceShootOut.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceShootOut.listenKeyEvent("keyup", "right arrow", self.rrOff)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.rotation += 1.5*self.vr
        self.move()
        if self.thrust == 1:
            self.VX += self.vx
            self.VY += self.vy
        if 0 <= self.x <= SW:
            self.x -= 0.1*self.VX
        elif self.x < 0:
            self.x += SW
            self.x -= 0.1*self.VX
        else:    
            self.x -= (0.1*self.VX + SW)
        if 0 <= self.y <= SH:    
            self.y -= 0.1*self.VY
        elif self.y < 0:
            self.y += SH
            self.y -= 0.1*self.VY
        else:
            self.y -= (0.1*self.VY + SH)
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        collides = self.collidingWithSprites(Sun)
        if len(collides):
                self.explode()
        else:
            self.setImage(2)
        collides = self.collidingWithSprites(Rocket2)
        if len(collides):
                self.explode()
    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 1
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
class Rocket2(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Rocket2.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceShootOut.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceShootOut.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceShootOut.listenKeyEvent("keydown", "a", self.rotateLeft)
        SpaceShootOut.listenKeyEvent("keyup", "a", self.lrOff)
        SpaceShootOut.listenKeyEvent("keydown", "d", self.rotateRight)
        SpaceShootOut.listenKeyEvent("keyup", "d", self.rrOff)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.rotation += 1.5*self.vr
        self.move()
        if self.thrust == 1:
            self.VX += self.vx
            self.VY += self.vy
        if 0 <= self.x <= SW:
            self.x -= 0.1*self.VX
        elif self.x < 0:
            self.x += SW
            self.x -= 0.1*self.VX
        else:
            self.x -= (0.1*self.VX + SW)
        if 0 <= self.y <= SH:    
            self.y -= 0.1*self.VY
        elif self.y < 0:
            self.y += SH
            self.y -= 0.1*self.VY
        else:
            self.y -= (0.1*self.VY + SH)
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
        if self.thrustframe == 4:
            self.thrustframe = 1
        else:
            self.setImage(0)
        collides = self.collidingWithSprites(Sun)
        if len(collides):
                self.explode()
        else:
            self.setImage(1)
        collides = self.collidingWithSprites(Rocket1)
        if len(collides):
                self.explode()

    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 1
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
        
class Sun(Sprite):
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = 0.0
        self.fycenter = -1.0
    def step(self):
        if:
            self.setImage(1)
            collides = self.collidingWithSprites(Rocket1)
            if len(collides):
                self.explode()
        else:
            self.setImage(2)
            collides = self.collidingWithSprites(Rocket2)
            if len(collides):
                self.explode()
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 0
class ExplosionBig(Sprite):
    asset = ImageAsset("images/explosion2.png", 
    Frame(0,0,4800/25,195), 25)
    boomasset = SoundAsset("sounds/explosion2.mp3")
    def __init__(self, position):
        super().__init__(ExplosionBig.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        self.boom = Sound(ExplosionBig.boomasset)
        self.boom.play()
    def step(self):
        self.setImage(self.image//2)
        self.image += 2
        if self.image == 50:
            self.destroy()

class SpaceShootOut(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0, 0))
        bg1 = Sprite(bg_asset, (0, 256))
        bg2 = Sprite(bg_asset, (0, 512))
        bg3 = Sprite(bg_asset, (0,768))
        bg4 = Sprite(bg_asset, (256, 0))
        bg4 = Sprite(bg_asset, (256,256))
        bg5 = Sprite(bg_asset, (256, 512))
        bg6 = Sprite(bg_asset, (256, 768))
        bg7 = Sprite(bg_asset, (512, 0))
        bg7 = Sprite(bg_asset, (512, 256))
        bg8 = Sprite(bg_asset, (512, 512))
        bg9 = Sprite(bg_asset, (512, 768))
        bg11 = Sprite(bg_asset, (768, 0))
        bg10 = Sprite(bg_asset, (768, 256))
        bg11 = Sprite(bg_asset, (768, 512))
        bg12 = Sprite(bg_asset, (768,768))
        bg15 = Sprite(bg_asset, (1024, 0))
        bg13 = Sprite(bg_asset, (1024,256))
        bg14 = Sprite(bg_asset, (1024,512))
        bg15 = Sprite(bg_asset, (1024,768))
        Rocket1((200,250))
        Rocket2((1240,250))
        Sun((670,284))
    def step(self):
        for Sunn in self.getSpritesbyClass(Sun):
            Sunn.step()
        for Rocket in self.getSpritesbyClass(Rocket1):
            Rocket.step()
        for Rocket in self.getSpritesbyClass(Rocket2):
            Rocket.step()
        for explosion in self.getSpritesbyClass(ExplosionBig):
            explosion.step()
myapp = SpaceShootOut(SW, SH)
myapp.run()