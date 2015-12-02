"""
spaceshooter.py
Author: James Napier
Credit: Space War Source Code, Morgan

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""


#still need to flesh out what I need to write on my own
#some parts of the classes need to be redefined so that they are not including elements included in the SpaceWar Source Code


from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class background(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)
        
        

            
class gravitysprite(Sprite):
    #error in line above. Don't know what it is
    def __init__(self, asset, position, velocity):
        super().__init__(position)
    #insert asset, if it does not work
        self.vx=velocity[0]
        self.vy=velocity[1]
        self.fxcenter=0.5
        self.fycenter=0.5
        self.rrate=0.0
        self.thrust=0.0
        self.mass=1.0
    #not sure how to translate this -->class GracitySprite(Sprite)<-- from the sourcecode 


class Ship(gravitysprite):
    
    def registerKeys(self, leys):
        commands = ["left", "right", "forward"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
        
    def controldown(self, keys):
        if self.visible:
            command=self.keymap[event.key]
            if command=="left":
                sef.rrate=Ship.R
            elif command=="right":
                self.rrate=Ship.R
            elif command=="forward":
                self.thrust=40.0
                self.imagex=0
                self.setImage(self.imagex)
                
    def controlup(self, event):
        command = self.keymap[eventkey,key]
        if command in ["left", "right"]:
            self.rrate=0.0
        elif command =="forward":
            self.thrust=0.0
            self.imagex=0
            self.setImage(self.imagex)
            #still got some stuff for class(Ship)
        
class Ship1(Ship):
        asset = ImageAsset("images/four_spaceship_by_albertiv_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')
            
        def __init__(self, app, position, velocity):
            super()._init_(Ship1.asset, app, position, velocity)
            self.registerKeys(["a", "d", "w"])
            
        def step(self, t, dT):
            super().step(T, dT)
            if self.visible:
                collides = self.collidingWithSprites(Ship2)
                if len(collides):
                    if collides[0].visible:
                        collides[0].explode()
                        self.explode()
                            
class Ship2(Ship):
        asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
            Frame(0,0,86,125), 4, 'vertical')
            
        def __init__(self, app, position, velocity):
            super()._init_(Ship2.asset, app, position, velocity)
            self.registerKeys(["left arrow", "right arrow", "up arrow"])
            
        def step(self, T, dT):
            super().step(T, dT)
            if self.visible:
                collides = self.collidingWithSprites(Ship1)
                if len(collides): 
                    if collides[0].visible:
                        collides[0].explode()
                        self.explode()
class SpaceWar(App):
    
    
    
    
    def __init__ (self, width, height):
        super().__init__(width, height)
        BG = ImageAsset("images/starfield.jpg")
        
        
        background(BG, (0, 0))
        self.ship1=Ship1(self,(self.width/2-140, self.height/2), (0, -120))
        self.ship2=Ship2(self,(self.width/2+140, self.height/2), (0, 120))
    #
        self.tsprites = {k:Sprite(TextAsset(text=v, width=200, align='center',style='20px Arial', fill=Color(0xff2222,1))) 
            for k, v in Spacewar.strings.items()}
        self.listenKeyEvent('keydown', 'space', self.space)
    #
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
    
    

app = SpaceWar(0,0)
app.run()

