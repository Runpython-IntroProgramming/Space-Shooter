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
        
class Player(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    
    Frame(0,0,85,125), 4, 'vertical')
    
    def __init__(self,position):
        super().__init__(Player.asset, position)
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
    def step(self):
        if len(self.collidingWithSprites(Player)) > 0:
            for x in SpaceGame.getSpritesbyClass(Player):
                x.explode()
            self.explode()
            return
        if len(self.collidingWithSprites(PlayerBullet)) > 0:
            for x in self.collidingWithSprites(PlayerBullet):
                x.destroy()
            self.explode()
            return
        self.x += self.velx
        self.y += self.vely
        if self.frame == 3:
            self.frame = 1
        else:
            self.frame += 1
        self.setImage(self.frame)
        if self.x > SCREEN_WIDTH or self.x < 0 or self.y > SCREEN_HEIGHT or self.y < 0:
            self.rotation += pi
            self.velocitySet()
        elif self.dist > SCREEN_DIAG/5 and randint(0,20) == 0:
            self.changeDirec()
        self.dist += self.speed
        if randint(0,500) == 0:
            EnemyBullet((self.x,self.y))
            self.ShootSound.play()
            
class Bullet(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.velx = 0
        self.vely = 0
    
    def step(self):
        if 0 <= self.x <= SCREEN_WIDTH and 0 <= self.y <= SCREEN_HEIGHT:
            self.velx = velCalcX(self.speed, self.rotation)
            self.vely = velCalcY(self.speed, self.rotation)
            self.x += self.velx
            self.y += self.vely
        else:
            self.destroy()

class PlayerBullet(Bullet):
    
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8))
    
    def __init__(self, position):
        super().__init__(PlayerBullet.asset, position)
        self.speed = 5
        for x in SpaceGame.getSpritesbyClass(Player):
            self.rotation = x.rotation
            
class EnemyBullet(Bullet):
    
    asset = ImageAsset("images/blast.png", Frame(40,0,8,8))
    
    def __init__(self, position):
        super().__init__(EnemyBullet.asset, position)
        self.speed = 1
        self.scale = 2
        for x in SpaceGame.getSpritesbyClass(Player):
            self.rotation = atan((x.x-self.x)/(x.y-self.y))
            if self.y < x.y:
                self.rotation += pi
            self.rotation += radians(randint(-101,100)/10)
class Explosion(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    SAsset = SoundAsset("sounds/explosion1.mp3")
    
    def __init__(self, position):
        super().__init__(Explosion.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.frame = 0
        self.ExplodeSound = Sound(Explosion.SAsset)
        self.ExplodeSound.volume = 10
        self.ExplodeSound.play()
        
    def step(self):
        if self.frame == 8:
            self.destroy()
        else:
            self.frame += 1
        self.setImage(self.frame)
        
class PlayerExplosion(Explosion):
    
    def __init__(self, position):
        super().__init__(position)
    
    def step(self):
        super().step()
        if self.frame == 8:
            for x in SpaceGame.getSpritesbyClass(LifeControl):
                x.respawn()
            self.destroy()
        
class ScoreControl(Sprite):
    
    asset = TextAsset("Score:", fill=white)
    
    def __init__(self, position):
        super().__init__(ScoreControl.asset, position)
        self.score = 0
        self.dispScore()
        
    def dispScore(self):
        Score(TextAsset(str(self.score), fill=white), (65,0))
        
    def scoreChange(self):
        for x in SpaceGame.getSpritesbyClass(Score):
            x.destroy()
        self.score += 1
        self.dispScore()
        if self.score == NUM_ENEMIES:
            for x in SpaceGame.getSpritesbyClass(LifeControl):
                if x.lives > 0:
                    classDestroy(EnemyBullet)
                    WinText((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
class Score(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        
class LifeControl(Sprite):
    
    asset = TextAsset("Lives:", fill=white)
    SAsset = SoundAsset("sounds/reappear.mp3")
    
    def __init__(self, position):
        super().__init__(LifeControl.asset, position)
        self.lives = LIVES
        self.dispLives()
        self.RespawnSound = Sound(LifeControl.SAsset)
        self.RespawnSound.volume = 10
        
            