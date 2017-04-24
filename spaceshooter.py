"""
spaceshooter.py
Author: Sam Pych
Credit: source code for space shooter and tutorial

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar

Your game must include the following:

A fixed star field background.
At least one player.
Either multiple playes, or some (in)animate object(s) to avoid.
Animated rocket thrust for the ship sprites.
Collisions destroy ships.
Moving and rotating ships - physics realism at your discretion.
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        
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
        Spacewar.listenKeyEvent("keydown", "space", self.thrustOn)
        Spacewar.listenKeyEvent("keyup", "space", self.thrustOff)
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

        
        
class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def unit(self):
        r = self.mag()
        if r == 0:
            return Vector(0,0)
        else:
            return Vector(self.x/r, self.y/r)
class Spacewar(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))
        self.listenKeyEvent('keydown', 'space', self.space)

    def space(self, evt):
        if self.state in ['instructions', 'gameover']:
            for t in self.tsprites.values():
                t.visible = False
            self.state = 'playing'
            self.Tlast = time()
            evt.consumed = True
            self.ship1.newgame()
            self.ship2.newgame()

        
    def step(self):
        explosions = self.getSpritesbyClass(ExplosionSmall)
        for explosion in explosions:
            explosion.step()
        explosions = self.getSpritesbyClass(ExplosionBig)
        for explosion in explosions:
            explosion.step()
        if self.state == 'instructions':
            self.tsprites['space'].visible = True
            self.tsprites['left'].visible = True
            self.tsprites['right'].visible = True
        elif self.state == 'playing':
            T = time()
            dT = T-self.Tlast
            self.Tlast = T
            self.ship1.step(T, dT)
            self.ship2.step(T, dT)
            if self.ship1.dead or self.ship2.dead:
                self.state = 'gameover'
        elif self.state == 'gameover':
            self.tsprites['space'].visible = True
            if self.ship1.dead and self.ship2.dead:
                self.tsprites['tie'].visible = True
            else:
                self.tsprites['winner'].visible = True
                self.tsprites['winner'].x = self.width*3/4-50 if self.ship1.dead else self.width/4-50

app = Spacewar(0,0)
app.run()