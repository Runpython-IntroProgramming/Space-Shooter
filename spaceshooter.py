"""
spaceshooter.py
Author: Payton
Credit: Morgan, Avery, Daniel, Original Spacewar Code

Assignment:
Write and submit a program that implements the ControlDwon game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.0
        self.thrust = 0
        self.thrustframe = 1
        self.rotation = 0
        left_location = 1
        ControlDwon.listenKeyEvent("keydown", "w", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "w", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "d", self.rotationOnLeft)
        ControlDwon.listenKeyEvent("keyup", "d", self.rotationOff)
        ControlDwon.listenKeyEvent("keydown", "a", self.rotationOnRight)
        ControlDwon.listenKeyEvent("keyup", "a", self.rotationOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx += .05*math.cos((self.rotation+math.pi/2))
            self.vy += .05*math.sin((self.rotation-math.pi/2))
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        if self.vr == .1:
            self.rotation = self.rotation +.0001
        if self.vr == -0.1:
            self.rotation = self.rotation - 0.0001
        
        col=self.collidingWithSprites(sun)
        if col:
            self.explode()
        
    def rotationOnLeft(self, event):
        self.vr = -.1
    def rotationOnRight(self, event):
        self.vr = .1
    def rotationOff(self, event):
        self.vr = 0

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
        
    def thrustdecel(self, event):
        self.thrust = 0.5
    
    def explode(self, event):
        self.visible = False
        self.vx = 0
        self.vy = 0
        ExplosionSmall(self.position)

class SpaceShip2(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.0
        self.thrust = 0
        self.thrustframe = 1
        self.rotation = 0
        left_location = 1
        ControlDwon.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        ControlDwon.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        ControlDwon.listenKeyEvent("keydown", "right arrow", self.rotationOnLeft)
        ControlDwon.listenKeyEvent("keyup", "right arrow", self.rotationOff)
        ControlDwon.listenKeyEvent("keydown", "left arrow", self.rotationOnRight)
        ControlDwon.listenKeyEvent("keyup", "left arrow", self.rotationOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx += .05*math.cos((self.rotation+math.pi/2))
            self.vy += .05*math.sin((self.rotation-math.pi/2))
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        if self.vr == .1:
            self.rotation = self.rotation +.0001
        if self.vr == -0.1:
            self.rotation = self.rotation - 0.0001
        
        col=self.collidingWithSprites(sun)
        if col:
            self.explode()
        
    def rotationOnLeft(self, event):
        self.vr = -.1
    def rotationOnRight(self, event):
        self.vr = .1
    def rotationOff(self, event):
        self.vr = 0

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0
        
    def thrustdecel(self, event):
        self.thrust = 0.5
    
    def explode(self, event):
        self.visible = False
        self.vx = 0
        self.vy = 0
        ExplosionSmall(self.position)
    

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
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 20:
            self.destroy()

class sun(Sprite):
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(sun.png, position)
        self.image = 0
        self.center = (1, 1)

class ControlDwon(App):
    """
    Tutorial4 space game example.
    """
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

    def __init__(self, width, height):
        super().__init__(width, height)
        bg_asset = ImageAsset("images/starfield.jpg")
        txt_asset = TextAsset("Control Dwon: Drift Mode", width = 300, align ='center', style='40px Times', fill=Color(0xff2222,1)) 
        bg = Sprite(bg_asset, (0,0))
        bg = Sprite(bg_asset, (0,512))
        bg = Sprite(bg_asset, (512,0))
        bg = Sprite(bg_asset, (512,512))
        txt=Sprite(txt_asset, (0,0))
        sun_asset = ImageAsset("images/sun.png")
        sun = Sprite(sun_asset, (400,300))
        left_location = 1
        SpaceShip((300,350))
        SpaceShip2((600,350))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(SpaceShip2):
            ship.step()


myapp = ControlDwon(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
