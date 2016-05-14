"""
spaceshooter.py
Author: Hagin
Credit: myself

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, Color, TextAsset, SoundAsset, Sound
from math import sqrt, sin, cos, radians, degrees, pi, atan
from random import randint
from time import sleep

SCREEN_WIDTH = 1000 #1200
SCREEN_HEIGHT = 600 #700
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)


if SCREEN_WIDTH >= SCREEN_HEIGHT:
    LARGER_SIDE = SCREEN_WIDTH
    SMALLER_SIDE = SCREEN_HEIGHT
else:
    LARGER_SIDE = SCREEN_HEIGHT
    SMALLER_SIDE = SCREEN_WIDTH
    
white = Color (0xffffff, 1.0) 

velocityOfX = lambda rotation, speed: -1*speed*sin(rotation)
velocityOfY = lambda rotation, speed: -1*speed*cos(rotation)

def Destroy(Dclass):
    while len(SpaceGame.getSpritesbyClass(Dclass)) > 0:
        for foo in SpaceGame.getSpritesbyClass(Dclass):
            foo.destroy()
def Opponent(EnemyCount):
    for foo in SpaceGame.getSpritesbyClass(ScoreMain):
        score = foo.score
    for bar in [1/(EnemyCount-score)*bar*2*pi for foo in list(range(0,(EmenyCount-score)))]:
        Enemy(((SMALLER_SIDE*-0.4)*sin(foo)+SCREEN_WIDTH/2,
        (SMALLER_SIDE*-0.4)*cos(x)+SCREEN_HIEGHT/2))

class Background(Sprite):
    
    if SCREEN_WIDTH >= SCREEN_HEIGHT:
        asset = ImageAsset("images/starfield.jpg", Frame(0,0,512,512,*(SMALLER_SIDE/LARGER_SIDE)))
    else:
        asset = ImageAsset("images/starfield.jpg", Frame(0,0,512*(SMALLER_SIDE/LARGER_SIDE),512))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = LARGER_SIDE/512

class Spaceship(Sprite):
    
    ShipAssest = SoundAsset("sound/pew1.mp3")
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.ShootSound = Sound(SpaceShip.asset)
        self.ShootSound = 40
        
class Pawn(ShaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    
    Frame(0,0,85,125), 4, 'vertical')
    
    def __init__(self,position):
        super().__init__(Pawn.asset, position)
        self.thrust = 0 
        self.thrustFrame = 0
        self.xSpeed = 0.1
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        self.velocity = (0,0)
        self.magnitude = 0.25
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrustOn(self, event):
        self.thrust = 1
        self.velocity[0] += -1*self.magnitude*sin(self.rotation)
        self.velocity[1] += -1*self.magnitude*cos(self.rotation)
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def explode(self):
        for x in SpaceGame.getSpritesbyClass(LifeControl):
            x.loseLife()
        PlayerExplosion((self.x, self.y))
        self.destroy()
    
    def fire(self, event):
        if len(SpaceGame.getSpritesByClass(PlayBullet)) < AMMO:
            PlayBullet((self.x, self.y))
            self.ShootSound.play()
            
    def step(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        if self.thrust == 1:
            if self.thrustframe == 3:
                self.thrustframe = 1
            else:
                self.thrustframe += 1
            self.setImage(self.thrustframe)
        else:
            self.setImage(0)
        if len(self.collidingWithSprites(EnemyBullet)) > 0:
            for x in self.collidingWithSprites(EnemyBullet):
                x.destroy()
            self.explode()
            return
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            if len(SpaceGame.getSpritesbyClass(WinText)) == 0:
                self.explode()
                return
   
    class Enemy(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.speed = 1
        self.changeDirec()
        self.dist = 0
        self.frame = 1
        self.scale = 0.75
    
    def velocitySet(self):
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
    
    def changeDirec(self):
        self.rotation = randint(0,1000)/500*pi
        self.velocitySet()
        self.dist = 0
        
    def explode(self):
            Explosion((self.x, self.y))
            for x in SpaceGame.getSpritesbyClass(ScoreControl):
                x.scoreChange()
            self.destroy()
            