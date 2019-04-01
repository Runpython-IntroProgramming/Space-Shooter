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

class Bullet1(Sprite):
    def __init__(self,position,vx,vy): 
        asset=ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
        super().__init__(asset,position)
        self.setImage(0)
        self.fxcenter=self.fycenter=0.5
        self.vx=vx
        self.vy=vy
    def step(self):
        if self.visible!=False:
            self.x+=self.vx
            self.y+=self.vy
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship2)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
class Bullet2(Sprite):
    def __init__(self,position,vx,vy): 
        asset=ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
        super().__init__(asset,position)
        self.setImage(0)
        self.fxcenter=self.fycenter=0.5
        self.vx=vx
        self.vy=vy
    def step(self):
        if self.visible!=False:
            self.x+=self.vx
            self.y+=self.vy
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
            

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
        if 0<self.x<200 and 0<self.y<200:
            self.destroy()
        elif 872<self.x and 350<self.y:
            self.destroy()
    
    
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
        Spacewar.listenKeyEvent("keydown","a", self.rightOn)
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
                self.rotation+=.02
                self.angle+=.02
            if self.left==1:
                self.rotation-=.02
                self.angle-=.02
            if self.shoot==1:
                Bullet2((self.x,self.y),2*self.vx,2*self.vy)
        if self.visible:
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
            collision3=self.collidingWithSprites(Bullet1)
            if collision3:
                self.visible=False
    
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
                Bullet1((self.x,self.y),2*self.vx,2*self.vy)
        if self.visible:
            collision=self.collidingWithSprites(Sun)
            collision2=self.collidingWithSprites(Spaceship2)
            if collision or collision2:
                self.visible=False
                explosion(self.position)
            collision3=self.collidingWithSprites(Bullet2)
            if collision3:
                self.visible=False
    
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
        self.fxcenter=self.fycenter=0.5
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
        self.go=1
        self.sp = Spaceship((100,100))
        self.sp2 = Spaceship2((self.width-100,self.height-100))
        for x in range(int(input("Set difficulty level, 0-10: "))):
            Sun((random.randint(0,self.width),random.randint(0,self.height)))
        self.ste=True
            
    def step(self):
        for exp in self.getSpritesbyClass(explosion):
            exp.step()
        for bullet in self.getSpritesbyClass(Bullet1):
                    bullet.step()
        for bull in self.getSpritesbyClass(Bullet2):
                    bull.step()
        if self.ste==True:
            if self.sp.visible==False:
                self.go=0
            elif self.sp.x<-50:
                self.go=0
            elif self.sp.x>self.width+50:
                self.go=0
            elif self.sp.y<-50:
                self.go=0
            elif self.sp.y>self.height+50:
                self.go=0
            elif self.sp2.visible==False:
                self.go=2
            elif self.sp2.x<-50:
                self.go=2
            elif self.sp2.x>self.width+50:
                self.go=2
            elif self.sp2.y<-50:
                self.go=2
            elif self.sp2.y>self.height+50:
                self.go=2
            if self.go==1:
                for ship in self.getSpritesbyClass(Spaceship):
                    ship.step()
                for ship2 in self.getSpritesbyClass(Spaceship2):
                    ship2.step()
            if self.go==0:
                print("Player 2 wins!")
                self.ste=False
            if self.go==2:
                print("Player 1 wins!")
                self.ste=False


myapp=Spacewar()
myapp.run()