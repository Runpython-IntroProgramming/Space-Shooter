"""
spaceshooter.py
Author: James Napier
Credit: Space War Source Code. Mr. Dennison


Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos
SCREEN_WIDTH = 1665
SCREEN_HEIGHT = 945

class background(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)

class ExplosionSmall(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128))
    
    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image += 1
        if self.image == 20:
            self.destroy()
            
class Sun(background):
    
    asset = ImageAsset("images/sun.png")
    width = 100
    height = 100

class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.02
        self.thrust = 0
        self.thrustframe = 1
        self.fxcenter = self.fycenter = 0.5
    
    def step(self, sun):
            
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
        
            if self.thrustframe == 4:
                self.thrustframe = 1
            self.x += -sin(self.rotation)
            self.y += -cos(self.rotation)

            if self.collidingWith(sun):
                ExplosionSmall(slf.position)
                self.destroy()
                
                

        else:
            self.setImage(0)
            
       
                
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def TurnLOn(self, event):
        self.rotation += self.vr
        
    def TurnROn(self, event):
        self.rotation -= self.vr
    
        
class SpaceGame(App):

    def __init__(self, width, height):
        super().__init__(width, height)
        BG = ImageAsset("images/starfield.jpg")
        BGS = ImageAsset("images/sun.png")
        bgsprite = background(BG, (0,0))
        bgsprite.width = SCREEN_WIDTH
        bgsprite.height = SCREEN_HEIGHT
        self.bgs_sprite = Sun(BGS, (800, 450))
        self.ship = SpaceShip((400,450))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step(self.bgs_sprite)
        explosions = self.getSpritesbyClass(ExplosionSmall)
        for explosion in explosions:
            explosion.step()
            
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'w', myapp.ship.thrustOn)
myapp.listenKeyEvent('keyup', 'w', myapp.ship.thrustOff)
myapp.listenKeyEvent('keydown', 'a', myapp.ship.TurnLOn)
myapp.listenKeyEvent('keydown', 'd', myapp.ship.TurnROn)
myapp.run()