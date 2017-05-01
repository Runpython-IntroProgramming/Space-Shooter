"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5

class Spacewar(App):
    
    strings = {'winner': 'WINNER!',
        'tie': 'TIE!',
        'space': 'Press SPACE to play.',
        'left': 'AWD\nSpace to FIRE',
        'right': 'Arrow Keys\nEnter to FIRE',
        }

    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))
        self.sun = Sun((self.width/2, self.height/2))
        self.ship1 = Ship1(self, (self.width/2-140,self.height/2), (0,-120), self.sun)
        self.ship2 = Ship2(self, (self.width/2+140,self.height/2), (0,120), self.sun)
        self.tsprites = {k:Sprite(TextAsset(text=v, width=200, align='center',style='20px Arial', fill=Color(0xff2222,1))) 
            for k, v in Spacewar.strings.items()}
        self.tsprites['winner'].visible = False
        self.tsprites['winner'].y = self.height/2
        self.tsprites['tie'].visible = False
        self.tsprites['tie'].position = (self.width/2 - 100, self.height/2 + 50)
        self.tsprites['space'].position = (self.width/2 - 100, self.height*3/4)
        self.tsprites['left'].position = (self.width/4 - 50, self.height/2)
        self.tsprites['right'].position = (self.width*3/4 - 50, self.height/2)
        self.state = 'instructions'
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

app.run()