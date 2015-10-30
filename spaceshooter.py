"""
spaceshooter.py
Author: Jeff
Credit: Space Game tutorial

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 1024
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()


class Ship1(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Ship1.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rrOff)
        self.fxcenter = self.fycenter = 0.5
    
    def step(self):
        self.rotation += 1.5*self.vr
        if self.thrust == 1:
            self.VX += self.vx
            self.VY += self.vy
        if 0 <= self.x <= SCREEN_WIDTH:
            self.x -= 0.1*self.VX
        elif self.x < 0:
            self.x += SCREEN_WIDTH
            self.x -= 0.1*self.VX
        else:    
            self.x -= (0.1*self.VX + SCREEN_WIDTH)
        if 0 <= self.y <= SCREEN_HEIGHT:    
            self.y -= 0.1*self.VY
        elif self.y < 0:
            self.y += SCREEN_HEIGHT
            self.y -= 0.1*self.VY
        else:
            self.y -= (0.1*self.VY + SCREEN_HEIGHT)
    
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            self.move()
        else:
            self.setImage(0)
            
        collides = self.collidingWithSprites(Ship1)
        if len(collides):
            if collides[0].visible:
                collides[0].explode()
                self.explode()
    
    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)
    
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 5
    
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

class Ship2(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Ship2.asset, position)
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.VX = 0
        self.VY = 0   
        self.vx = 0
        self.vy = 0
        self.turn = 0
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a", self.rotateLeft)
        SpaceGame.listenKeyEvent("keyup", "a", self.lrOff)
        SpaceGame.listenKeyEvent("keydown", "d", self.rotateRight)
        SpaceGame.listenKeyEvent("keyup", "d", self.rrOff)
        SpaceGame.listenKeyEvent("keydown", "e", self.fire)
        self.fxcenter = self.fycenter = 0.5
        self.bullet = None
    
    def step(self):
        self.rotation += 1.5*self.vr
        self.move()
        if self.thrust == 1:
            self.VX += self.vx
            self.VY += self.vy
        if 0 <= self.x <= SCREEN_WIDTH:
            self.x -= 0.1*self.VX
        elif self.x < 0:
            self.x += SCREEN_WIDTH
            self.x -= 0.1*self.VX
        else:    
            self.x -= (0.1*self.VX + SCREEN_WIDTH)
        if 0 <= self.y <= SCREEN_HEIGHT:    
            self.y -= 0.1*self.VY
        elif self.y < 0:
            self.y += SCREEN_HEIGHT
            self.y -= 0.1*self.VY
        else:
            self.y -= (0.1*self.VY + SCREEN_HEIGHT)
    
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        
        collides = self.collidingWithSprites(Ship1)
        if len(collides):
            if collides[0].visible:
                collides[0].explode()
                self.explode()
                
    
    def move(self):
        self.X = math.sin(self.rotation)
        self.Y = math.cos(self.rotation)
        self.vx = self.X/math.sqrt(self.X*self.X + self.Y*self.Y)
        self.vy = self.Y/math.sqrt(self.X*self.X + self.Y*self.Y)
    
    def explode(self):
        self.visible = False
        ExplosionBig(self.position)
        self.waitspawn = 5
    
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
    
    def fire(self, event):
        vx = 
        self.bullet= Bullet(self.position, self.vx, self.vy)
        
class Bullet(Sprite):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
    pewasset = SoundAsset("sounds/pew1.mp3")
    
    def __init__(self, position, vx, vy):
        super().__init__(Bullet.asset, position)
        self.exist = True
        self.circularCollisionModel()
        self.pew = Sound(Bullet.pewasset)
        self.pew.volume = 10
        self.appear = 1
        self.fxcenter = 0.5
        self.fycenter = 8.5
        self.X = vx
        self.Y = vy 
    
    def step(self):
        if self.exist:
            self.setImage(self.appear)
            self.appear += 1
            if self.appear == 8:
                self.appear = 1
        else:
            self.setImage(0)
        
        self.x -= 10*self.X
        self.y -= 10*self.Y
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y >SCREEN_HEIGHT:
            self.destroy()
        
        
class HealthBar:
    
    def __init__(self, indicatorasset, initvalue, position, app):
        self.sprites = [Sprite(indicatorasset, (0,app.height-75)) for i in range(initvalue)]
        for s in self.sprites:
            s.scale = 0.4
        width = self.sprites[0].width
        if position == 'left':
            x = 50
            step = width+5
        else:
            x = app.width - 50 - width
            step = -width-5
        for s in self.sprites:
            s.x = x
            x += step
        self.restart()
        
    def restart(self):
        for s in self.sprites:
            s.visible = True
        self.count = len(self.sprites)
        
    def dead(self):
        return self.count == 0
        
    def killone(self):
        if self.count > 0:
            self.count -= 1
            self.sprites[self.count].visible = False

class ExplosionSmall(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    boomasset = SoundAsset("sounds/explosion1.mp3")
    
    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        self.boom = Sound(ExplosionSmall.boomasset)
        self.boom.play()
        
    def step(self):
        self.setImage(self.image//2)
        self.image += 1
        if self.image == 20:
            self.destroy()

class ExplosionBig(Sprite):
    
    asset = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
    boomasset = SoundAsset("sounds/explosion2.mp3")
    
    def __init__(self, position):
        super().__init__(ExplosionBig.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        self.boom = Sound(ExplosionBig.boomasset)
        self.boom.play()
        
    def step(self):
        self.setImage(self.image//2)
        self.image += 1
        if self.image == 50:
            self.destroy()
            
class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg1 = Sprite(bg_asset, (512,512))
        bg2 = Sprite(bg_asset, (0,512))
        bg3 = Sprite(bg_asset, (512,0))
        bg4 = Sprite(bg_asset, (1024,512))
        bg5 = Sprite(bg_asset, (1024,0))
        
        Ship1((250,250))
        Ship2((400,400))
        Sun((50,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(Ship1):
            ship.step()
        for ship in self.getSpritesbyClass(Ship2):
            ship.step()
        
        explosions = self.getSpritesbyClass(ExplosionSmall)
        for explosion in explosions:
            explosion.step()
        explosions = self.getSpritesbyClass(ExplosionBig)
        for explosion in explosions:
            explosion.step()
        for bullets in self.getSpritesbyClass(Bullet):
            bullets.step()
        
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
