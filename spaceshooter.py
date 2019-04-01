"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame
import math, random
from time import time
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        for i in range (1,10):
            white=Color(0xbbbb00,1)
            starline=LineStyle(2,white)
            star_asset =RectangleAsset(10, 10, starline, white)
            star = Sprite(star_asset, ((random.randint(0,1000)),(random.randint(0,500))))
        SpaceShip((100,100))
        asteroid((random.randint(0,800),random.randint(0,400)))
        asteroid((random.randint(0,800),random.randint(0,400)))
        asteroid((random.randint(0,800),random.randint(0,400)))
        asteroid((random.randint(0,800),random.randint(0,400)))
        asteroid((random.randint(0,800),random.randint(0,400)))
        asteroid((random.randint(0,800),random.randint(0,400)))
        Bullet((500,500))
            

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(asteroid):
            ship.step()
            

class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, (400,400))
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotationlefton)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.rotationleftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotationrighton)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rotationrightoff)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.thrust == 1 and self.rotation ==0 :
            self.x += 0
            self.y += -1
        if self.thrust == 1 and self.rotation == 1:
            self.x += -1
            self.y += -1
        if self.thrust == 1 and self.rotation ==-1:
            self.x += 1
            self.y += -1
        if self.thrust == 1 and self.rotation ==-2:
            self.x += 1
            self.y += 1
        if self.thrust == 1 and self.rotation ==2:
            self.x += -1
            self.y += 1
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
    
    def rotationleftoff(self, event):
        if self.rotation==0:
            self.rotation = 0
        elif self.rotation==1:
            self.rotation = 1
    
    def rotationlefton(self,event):
        self.rotation = self.rotation+1
    
    def rotationrightoff(self,event):
        if self.rotation==0:
            self.rotation = 0
        elif self.rotation==1:
            self.rotation = 1
    
    def rotationrighton(self,event):
        self.rotation = self.rotation-1
        k=1
class Bullet(Sprite):
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
    collisionasset = RectangleAsset(4,4)
    pewasset = SoundAsset("sounds/pew1.mp3")
    
    def __init__(self, position):
        super().__init__(Bullet.asset, Bullet.collisionasset, position)
        self.visible = False
        self.firing = False
        self.time = 0
        
    def shoot(self, position, velocity, time):
        self.position = position
        self.vx = velocity[0]
        self.vy = velocity[1]
        self.time = time
        self.visible = True
        self.firing = True
        self.pew.play()

    def step(self, T, dT):
        self.time = self.time - dT
        if self.visible:
            if self.time <= 0:
                self.visible = False
            else:
                self.nextImage(True)
                super().step(T, dT)
                if self.collidingWith(self.sun):
                    self.visible = False
                    ExplosionSmall(self.position)
                else:
                    ships = self.collidingWithSprites(Ship1)
                    ships.extend(self.collidingWithSprites(Ship2))
                    for ship in ships:
                        if not self.firing and ship.visible:
                            ship.explode()
                            self.visible = False
                    if not ships:
                        self.firing = False
        
class asteroid(Sprite):
    grey=Color(0xbebebe,1)
    asteroidline=LineStyle(2,grey)
    asteroid_asset =RectangleAsset(30, 30, asteroidline, grey)
    def __init__(self, position):
        super().__init__(asteroid.asteroid_asset, position)
        self.vx = 0
        self.vy = 0
    def step(self):
        self.x += self.vx
        self.y += self.vy
    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.thrust == 1:
            self.x += 0
            self.y += 1
    thrust = 1

class ExplosionSmall(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    
    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

myapp = SpaceGame()
myapp.run()


