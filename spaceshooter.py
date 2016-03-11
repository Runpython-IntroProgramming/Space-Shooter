"""
spaceshooter.py
Author: David Wilson
Credit: Mr. Dennison ("Space War Source Code" and "Advanced Graphics with Classes"),
http://ubuntuforums.org/showthread.php?t=879970

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
'''
from ggame import App, Sprite, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2

class SpaceShip(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
        
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.rotSpd = 0.1
        self.fxcenter = self.fycenter = 0.5
        self.thrust = 0
        self.thrustframe = 0
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def shoot(self, event):
        Bullet((100,100))
        
    def step(self):
        if self.thrust == 1:
            if self.thrustframe == 3:
                self.thrustframe = 1
            else:
                self.thrustframe += 1
            self.setImage(self.thrustframe)
        else:
            self.setImage(0)
            
class Bullet(Sprite):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8))
    
    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.velx = 5
        self.vely = 5
    
    def step(self):
        if 0 <= self.x <= SCREEN_WIDTH and 0 <= self.y <= SCREEN_HEIGHT:
            self.x += self.velx
            self.y += self.vely
        else:
            self.destroy()

class SpaceGame(App):
        
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        SpaceShip((100,100))
        
    def step(self):
        for x in self.getSpritesbyClass(SpaceShip):
            x.step()
        for x in self.getSpritesbyClass(Bullet):
            x.step()
        
myapp = SpaceGame()
myapp.run()

'''
"""
spaceshooter.py
Author: David Wilson
Credit: Mr. Dennison ("Space War Source Code" and "Advanced Graphics with Classes")

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset, Frame
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

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
        Bullet((100,100))
            
class Player(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Player.asset, position)
        self.thrust = 0
        self.thrustframe = 0
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrustOn(self, event):
        self.thrust = 1
        
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

class Enemy(SpaceShip):
    
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        
    def step(self):
        self.rotation -= self.rotSpd

class Bullet(Sprite):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8))
    
    def __init__(self, position):
        super().__init__(Bullet.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.rotation = Player.rotation
        self.velx = 5/math.sin(self.rotation)
        self.vely = 5/math.cos(self.rotation)
    
    def step(self):
        if 0 <= self.x <= SCREEN_WIDTH and 0 <= self.y <= SCREEN_HEIGHT:
            self.x += self.velx
            self.y += self.vely
        else:
            self.destroy()

class SpaceGame(App):
        
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()
        for x in self.getSpritesbyClass(Bullet):
            x.step()
        for x in self.getSpritesbyClass(Sun):
            x.step()
        
myapp = SpaceGame()
myapp.run()
