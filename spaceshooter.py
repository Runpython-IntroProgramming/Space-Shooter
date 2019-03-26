"""
spaceshooter.py
Author: emBrileg08
Credit: Spacewar Source Code
www.pythoncentral.io for information on random number generation

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
import random
import math

class Bullet(Sprite):
    def __init__(self,position,vx,vy): 
        asset=ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
        super().__init__(asset,position)
        self.setImage(0)
        self.vx=vx
        self.vy=vy
    def step(self):
        self.x+=self.vx
        self.y+=self.vy

class Background(Sprite):
    def __init__(self,position):
        asset=ImageAsset("images/starfield.jpg")
        super().__init__(asset,position)
    width=512
    height=512

class Sun(Sprite):
    def __init__(self,position):
        asset=ImageAsset("images/sun.png")
        super().__init__(asset,position)
        if 0<self.x<275 and 0<self.y<275:
        #ya need something here
        #also if the bullets hit the sun, explode but the sun doesn't explode
        #also limited number of bullets maybe
            self.destroy()
    def step(self):
        collision=self.collidingWithSprites(Spaceship)
        if collision:
            self.visible=False
    
    
class Spaceship2(Sprite):
    def __init__(self, position):
        asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')
        super().__init__(asset, position)
        self.fxcenter=self.fycenter=0.5
        self.thrust = 0
        self.right=0
        self.left=0
        self.shoot=0
        self.angle=math.pi/2
        self.thrustframe = 1
        Spacewar.listenKeyEvent("keydown","a", self.rOn)
        Spacewar.listenKeyEvent("keyup","a", self.rightOff)
        Spacewar.listenKeyEvent("keydown","s", self.leftOn)
        Spacewar.listenKeyEvent("keyup","s", self.leftOff)
        Spacewar.listenKeyEvent("keydown", "z", self.bulletOn)
        Spacewar.listenKeyEvent("keyup","z",self.bulletOff)
        self.visible=True
        
    def step(self):
        if self.visible!=False:
            self.vx=-math.cos(math.pi-self.angle)
            self.vy=-math.sin(math.pi-self.angle)
            self.x+=self.vx
            self.y+=self.vy
            if self.thrust == 1:
                self.setImage(self.thrustframe)
                self.thrustframe += 1
                if self.thrustframe == 4:
                    self.thrustframe = 1
            else:
                self.setImage(0)
            if self.right==1:
                self.rotation-=.02
                self.angle-=.02
            if self.left==1:
                self.rotation+=.02
                self.angle+=.02
            if self.shoot==1:
                Bullet((self.x,self.y),2*self.vx,2*self.vy)
        if self.visible:
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
    
    def rightOn(self, event):
        self.thrust = 1
        self.right=1
    def rightOff(self, event):
        self.thrust = 0
        self.right=0
    def leftOn(self, event):
        self.thrust = 1
        self.left=1
    def leftOff(self, event):
        self.thrust = 0
        self.left=0
    def bulletOn(self,event):
        self.shoot=1
    def bulletOff(self,event):
        self.shoot=0
    
class Spaceship(Sprite):
    def __init__(self, position):
        asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')
        super().__init__(asset, position)
        self.fxcenter=self.fycenter=0.5
        self.thrust = 0
        self.right=0
        self.left=0
        self.shoot=0
        self.angle=math.pi/2
        self.thrustframe = 1
        Spacewar.listenKeyEvent("keydown","right arrow", self.rightOn)
        Spacewar.listenKeyEvent("keyup","right arrow", self.rightOff)
        Spacewar.listenKeyEvent("keydown","left arrow", self.leftOn)
        Spacewar.listenKeyEvent("keyup","left arrow", self.leftOff)
        Spacewar.listenKeyEvent("keydown", "space", self.bulletOn)
        Spacewar.listenKeyEvent("keyup","space",self.bulletOff)
        self.visible=True
        
    def step(self):
        if self.visible!=False:
            self.vx=-math.cos(math.pi-self.angle)
            self.vy=-math.sin(math.pi-self.angle)
            self.x+=self.vx
            self.y+=self.vy
            if self.thrust == 1:
                self.setImage(self.thrustframe)
                self.thrustframe += 1
                if self.thrustframe == 4:
                    self.thrustframe = 1
            else:
                self.setImage(0)
            if self.right==1:
                self.rotation-=.02
                self.angle-=.02
            if self.left==1:
                self.rotation+=.02
                self.angle+=.02
            if self.shoot==1:
                Bullet((self.x,self.y),2*self.vx,2*self.vy)
        if self.visible:
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship2)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
    
    def rightOn(self, event):
        self.thrust = 1
        self.right=1
    def rightOff(self, event):
        self.thrust = 0
        self.right=0
    def leftOn(self, event):
        self.thrust = 1
        self.left=1
    def leftOff(self, event):
        self.thrust = 0
        self.left=0
    def bulletOn(self,event):
        self.shoot=1
    def bulletOff(self,event):
        self.shoot=0

class explosion(Sprite):
    def __init__(self, position):
        asset=ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
        super().__init__(asset, position)
        self.expframe=1
    def step(self):
        self.setImage(self.expframe)
        self.expframe += 1
        if self.expframe == 26:
            self.destroy()

class Spacewar(App):
    def __init__(self):
        super().__init__()
        z=0
        a=0
        while z<self.width:
            Background((z,0))
            while a<self.height:
                Background((z,a))
                a+=Background.height
            a=0
            z+=Background.width
        Spaceship((100,100))
        Spaceship((self.width-100,self.height-100))
        for x in range(int(input("Set difficulty level, 0-20: "))):
            Sun((random.randint(0,self.width),random.randint(0,self.height)))
    def step(self):
        for ship in self.getSpritesbyClass(Spaceship):
            ship.step()
        for exp in self.getSpritesbyClass(explosion):
            exp.step()
        for sun in self.getSpritesbyClass(Sun):
            sun.step()
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()
        for ship2 in self.getSpritesbyClass(Spaceship2):
            ship2.step
            
myapp=Spacewar()
myapp.run()