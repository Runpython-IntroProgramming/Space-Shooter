"""
spaceshooter.py
Author: David Wilson
Credit: Mr. Dennison ("Space War Source Code" and "Advanced Graphics with Classes")

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset, Frame, TextAsset
from math import sqrt, sin, cos, radians, degrees, pi
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)

velCalcX = lambda speed, rotation: -1*speed*sin(rotation)
velCalcY = lambda speed, rotation: -1*speed*cos(rotation)

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2

class SpaceShip(Sprite):
        
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.rotSpd = 0.1
        self.fxcenter = self.fycenter = 0.5
 
    def shoot(self, event):
        Bullet((self.x,self.y))
            
class Player(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,85,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Player.asset, position)
        self.speed = 5
        self.thrust = 0
        self.thrustframe = 0
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        self.velx = 0
        self.vely = 0
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrustOn(self, event):
        self.thrust = 1
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
        self.x += self.velx
        self.y += self.vely
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def step(self):
        if self.thrust == 1:
            if self.thrustframe == 3:
                self.thrustframe = 1
            else:
                self.thrustframe += 1
            self.setImage(self.thrustframe)
        else:
            self.setImage(0)

class Enemy(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.speed = 1
        self.rotation = randint(0,1000)/500*pi
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
        self.fxcenter = self.fycenter = 0.5
        self.dist = 0
        self.frame = 1
    
    def velocitySet(self):
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
    
    def changeDirec(self):
        self.rotation = randint(0,1000)/500*pi
        self.velocitySet()
        self.dist = 0
        
    def step(self):
        collides = self.collidingWithSprites(Bullet)
        if len(collides) > 0:
            Explosion((self.x, self.y))
            self.destroy()
            return
        self.x += self.velx
        self.y += self.vely
        if self.frame == 3:
            self.frame = 1
        else:
            self.frame += 1
        self.setImage(self.frame)
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            self.rotation += pi
            self.velocitySet()
        elif self.dist > SCREEN_DIAG/5 and randint(0,20) == 0:
            self.changeDirec()
        self.dist += self.speed

class Bullet(Sprite):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8))
    
    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.fxcenter = self.fycenter = 0.5
        for x in SpaceGame.getSpritesbyClass(Player):
            self.rotation = x.rotation
        self.velx = 0
        self.vely = 0
    
    def step(self):
        if 0 <= self.x <= SCREEN_WIDTH and 0 <= self.y <= SCREEN_HEIGHT:
            self.velx = velCalcX(5, self.rotation)
            self.vely = velCalcY(5, self.rotation)
            self.x += self.velx
            self.y += self.vely
        else:
            self.destroy()
            
class Explosion(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    
    def __init__(self, position):
        super().__init__(Explosion.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.frame = 0
        self.new = True
        
    def step(self):
        if self.new == True:
            self.new == False
        if self.frame == 8:
            self.destroy()
        else:
            self.frame += 1
        self.setImage(self.frame)
        
class Score(Sprite):
    
    asset = TextAsset(

class SpaceGame(App):
        
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        Enemy((100,100))
        self.step()
        self.destroyed = 0
        
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()
        for x in self.getSpritesbyClass(Bullet):
            x.step()
        for x in self.getSpritesbyClass(Enemy):
            x.step()
        for x in self.getSpritesbyClass(Explosion):
            x.step()
            if x.new == True:
                self.destroyed += 1
        
myapp = SpaceGame()
myapp.run()
