"""
spaceshooter.py
Author: David Wilson
Credit: Mr. Dennison ("Space War Source Code" and "Advanced Graphics with Classes"),
http://brythonserver.github.io/ggame/, 
http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

#movement

from ggame import App, Sprite, ImageAsset, Frame, Color, TextAsset, SoundAsset, Sound
from math import sqrt, sin, cos, radians, degrees, pi, atan
from random import randint
from time import sleep

SCREEN_WIDTH = 1000#1200
SCREEN_HEIGHT = 600#700
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)

if SCREEN_WIDTH >= SCREEN_HEIGHT:
    LARGER_SIDE = SCREEN_WIDTH
    SMALLER_SIDE = SCREEN_HEIGHT
else:
    LARGER_SIDE = SCREEN_HEIGHT
    SMALLER_SIDE = SCREEN_WIDTH

white = Color(0xffffff, 1.0)

velCalcX = lambda speed, rotation: -1*speed*sin(rotation)
velCalcY = lambda speed, rotation: -1*speed*cos(rotation)

def classDestroy(sclass):
    while len(SpaceGame.getSpritesbyClass(sclass)) > 0:
        for x in SpaceGame.getSpritesbyClass(sclass):
            x.destroy()

def EnemySpawn(NumEnemies):
    for x in SpaceGame.getSpritesbyClass(ScoreControl):
        score = x.score
    for x in [1/(NumEnemies-score)*x*2*pi for x in list(range(0,(NumEnemies-score)))]:
        Enemy(((SMALLER_SIDE*-0.4)*sin(x)+SCREEN_WIDTH/2, 
        (SMALLER_SIDE*-0.4)*cos(x)+SCREEN_HEIGHT/2))

class StarBack(Sprite):
    
    if SCREEN_WIDTH >= SCREEN_HEIGHT:
        asset = ImageAsset("images/starfield.jpg", Frame(0,0,512,512*(SMALLER_SIDE/LARGER_SIDE)))
    else:
        asset = ImageAsset("images/starfield.jpg", Frame(0,0,512*(SMALLER_SIDE/LARGER_SIDE),512))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = LARGER_SIDE/512

class SpaceShip(Sprite):
    
    SAsset = SoundAsset("sounds/pew1.mp3")
        
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.ShootSound = Sound(SpaceShip.SAsset)
        self.ShootSound.volume = 10
            
class Player(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,85,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Player.asset, position)
        self.speed = 5
        self.thrust = 0
        self.thrustframe = 0
        self.rotSpd = 0.1
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRight)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeft)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        self.velx = 0
        self.vely = 0
        
    def rotateRight(self, event):
        self.rotation -= self.rotSpd
        
    def rotateLeft(self, event):
        self.rotation += self.rotSpd
        
    def thrustOn(self, event):
        self.thrust = 1
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
        self.x += self.velx
        self.y += self.vely
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def explode(self):
        for x in SpaceGame.getSpritesbyClass(LifeControl):
            x.loseLife()
        PlayerExplosion((self.x, self.y))
        self.destroy()
        return
    
    def shoot(self, event):
        if len(SpaceGame.getSpritesbyClass(PlayerBullet)) < AMMO:
            PlayerBullet((self.x,self.y))
            self.ShootSound.play()
        
    def step(self):
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

class Enemy(SpaceShip):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Enemy.asset, position)
        self.speed = 1
        self.rotation = randint(0,1000)/500*pi
        self.velx = velCalcX(self.speed, self.rotation)
        self.vely = velCalcY(self.speed, self.rotation)
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
            PlayerExplosion((self.x, self.y))
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
        self.speed = 2
        self.scale = 2
        for x in SpaceGame.getSpritesbyClass(Player):
            self.rotation = atan((x.x-self.x)/(x.y-self.y))
            if self.y < x.y:
                self.rotation += pi
            
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
        
class ScoreControl(Sprite):
    
    asset = TextAsset("Score:", fill=white)
    
    def __init__(self, position):
        super().__init__(ScoreControl.asset, position)
        self.score = 0
        Score(TextAsset(str(self.score), fill=white), (65,0))
        
    def scoreChange(self):
        for x in SpaceGame.getSpritesbyClass(Score):
            x.destroy()
        self.score += 1
        Score(TextAsset(str(self.score), fill=white), (65,0))
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
        Lives(TextAsset(str(self.lives), fill=white), (55,20))
        self.RespawnSound = Sound(LifeControl.SAsset)
        self.RespawnSound.volume = 10
        
    def loseLife(self):
        for x in SpaceGame.getSpritesbyClass(Lives):
            x.destroy()
        self.lives -= 1
        Lives(TextAsset(str(self.lives), fill=white), (55,20))
        if self.lives == 0:
            LoseText((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        else:
            RespawnText((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            while len(SpaceGame.getSpritesbyClass(EnemyBullet)):
                for x in SpaceGame.getSpritesbyClass(EnemyBullet):
                    x.destroy()
                
    def respawn(self):
        if len(SpaceGame.getSpritesbyClass(Player)) == 0 and self.lives > 0:
            sleep(1)
            for x in SpaceGame.getSpritesbyClass(RespawnText):
                x.destroy()
            self.RespawnSound.play()
            Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            while len(SpaceGame.getSpritesbyClass(Enemy)) > 0:
                for x in SpaceGame.getSpritesbyClass(Enemy):
                    x.destroy()
            EnemySpawn(NUM_ENEMIES)
        
class Lives(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        
class AmmoControl(Sprite):
    
    asset = TextAsset("Ammo:", fill=white)
    
    def __init__(self, position):
        super().__init__(AmmoControl.asset, position)
        self.ammo = AMMO
        Ammo(TextAsset(str(self.ammo), fill=white), (65,40))
        
    def step(self):
        if AMMO-len(SpaceGame.getSpritesbyClass(PlayerBullet)) != self.ammo:
            self.ammo = AMMO-len(SpaceGame.getSpritesbyClass(PlayerBullet))
            for x in SpaceGame.getSpritesbyClass(Ammo):
                x.destroy()
            Ammo(TextAsset(str(self.ammo), fill=white), (65,40))
            
class Ammo(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        
class RespawnText(Sprite):
    
    asset = TextAsset("Respawning...", fill=white, align='center', width=SCREEN_WIDTH)
    
    def __init__(self, position):
        super().__init__(RespawnText.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class WinText(Sprite):
    
    asset = TextAsset("You Win!", fill=white, align='center', width=SCREEN_WIDTH)
    
    def __init__(self, position):
        super().__init__(WinText.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class LoseText(Sprite):
    
    asset = TextAsset("You Lose...", fill=white, align='center', width=SCREEN_WIDTH)
    
    def __init__(self, position):
        super().__init__(LoseText.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class InstructionText(Sprite):
    
    def __init__(self, asset, position):
        super().__init__(asset, position)
        self.fxcenter = self.fycenter = 0.5

class SpaceGame(App):
        
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        self.listenKeyEvent('keyup', '1', self.easy)
        self.listenKeyEvent('keyup', '2', self.medium)
        self.listenKeyEvent('keyup', '3', self.hard)
        self.instructions = [['Instructions:', 'Left and Right Arrows to Rotate', 
        'Up Arrow to Move', 'Space to Shoot', 'Press the Corresponding Number Keys to Switch Between Difficulties', 
        'Press "0" to Begin'], ['Easy', 'Medium', 'Hard'], ['"1"', '"2"', '"3"']]
        self.placeInstructions()
        self.go = False
        
    def placeInstructions(self):
        for x in self.instructions[0]:
            InstructionText(TextAsset(x, fill=white, align='center', width=SCREEN_WIDTH), 
            (SCREEN_WIDTH/2, SCREEN_HEIGHT/4+30*(self.instructions[0].index(x)-(len(self.instructions[0])-1)/2)))
        def diffInstruction(text, lower):
                InstructionText(TextAsset(text, fill=white, align='center', width=SCREEN_WIDTH),
                (SCREEN_WIDTH/2+SCREEN_WIDTH/5*(self.instructions[1].index(x)-(len(self.instructions[1])-1)/2),
                SCREEN_HEIGHT*3/4+lower))
        for x in self.instructions[1]:
            diffInstruction(x, 0)
            diffInstruction(self.instructions[2][self.instructions[1].index(x)], SCREEN_HEIGHT/10)
            
    def easy(self, event):
        self.difficulty = 1
        self.prepare()
        
    def medium(self, event):
        self.difficulty = 2
        self.prepare()
        
    def hard(self, event):
        self.difficulty = 3
        self.prepare()
        
    def prepare(self):
        classDestroy(Enemy)
        classDestroy(ScoreControl)
        classDestroy(Score)
        classDestroy(LifeControl)
        classDestroy(Lives)
        classDestroy(AmmoControl)
        classDestroy(Ammo)
        classDestroy(InstructionText)
        global NUM_ENEMIES
        global LIVES
        global AMMO
        NUM_ENEMIES = int((SCREEN_WIDTH*SCREEN_HEIGHT)*self.difficulty/300000)
        LIVES = 5-self.difficulty
        AMMO = 8-self.difficulty
        ScoreControl((0,0))
        LifeControl((0,20))
        AmmoControl((0,40))
        EnemySpawn(NUM_ENEMIES)
        self.placeInstructions()
        self.listenKeyEvent('keyup', '0', self.start)
        
    def start(self, event):
        self.go = True
        classDestroy(InstructionText)
        self.unlistenKeyEvent('keyup', '1', self.easy)
        self.unlistenKeyEvent('keyup', '2', self.medium)
        self.unlistenKeyEvent('keyup', '3', self.hard)
        self.unlistenKeyEvent('keyup', '0', self.start)
                
    def classStep(self, sclass):
        for x in self.getSpritesbyClass(sclass):
            x.step()
        
    def step(self):
        if self.go == True:
            self.classStep(Player)
            self.classStep(PlayerBullet)
            self.classStep(Enemy)
            self.classStep(EnemyBullet)
            self.classStep(Explosion)
            self.classStep(PlayerExplosion)
            self.classStep(AmmoControl)
        
SpaceGame().run()

'''
from math import sin, cos, pi

n = 4
r = 5

a = [1/n*x*2*pi for x in list(range(0,n))]
print(a)

for x in a:
    print(int(-1*r*sin(x)),end=', ')
    print(int(r*cos(x)))
'''
