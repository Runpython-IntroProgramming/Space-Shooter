"""
spaceshooter.py
Author: Funjando
Credit: Don-the-wott, Payton-man (like....so much)

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
#Imports
import math

from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color


from time import time

#ScreenSize
SCREEN_WIDTH=1400
SCREEN_HEIGHT=850

sun = None
class SpaceShip(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0.0
        self.thrust=0
        self.thrustframe=1
        self.rotation=0
        left_location=1
        eighties.listenKeyEvent("keydown", ",", self.thrustOn)
        eighties.listenKeyEvent("keyup", ",", self.thrustOff)
        eighties.listenKeyEvent("keydown", "e", self.rotationOnLeft)
        eighties.listenKeyEvent("keyup", "e", self.rotationOff)
        eighties.listenKeyEvent("keydown", "a", self.rotationOnRight)
        eighties.listenKeyEvent("keyup", "a", self.rotationOff)
        self.fxcenter=self.fycenter=0.5
        
    def step(self):
        self.x+=self.vx
        self.y+=self.vy
        self.rotation+=self.vr
        if self.thrust==1:
            self.setImage(self.thrustframe)
            self.thrustframe+=1
            self.vx+=.05*math.cos((self.rotation+math.pi/2))
            self.vy+=.05*math.sin((self.rotation-math.pi/2))
            if self.thrustframe==4:
                self.thrustframe=1
            else:
                self.setImage(0)
        if self.vr==.1:
            self.rotation=self.rotation+.0001
        if self.vr==-0.1:
            self.rotation=self.rotation-.0001
        
        col=self.collidingWithSprites(Sun)
        if col:
            self.explode(self)
        
    def rotationOnLeft(self, event):
        self.vr=-.1
        
    def rotationOnRight(self, event):
        self.vr=.1
        
    def rotationOff(self, event):
        self.vr=0
        
    def thrustOn(self, event):
        self.thrust=1
        
    def thrustOff(self, event):
        self.thrust=0
        
    def thrustdecel(self, event):
        self.thrust=0.5
    
    def explode(self, event):
        self.visible=False
        self.vx=0
        self.vy=0
        ExplosionSmall(self.position)
    
    
class SpaceShip2(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')
        
    def __init__(self, position):
        super().__init__(SpaceShip2.asset, position)
        self.vx=0
        self.vy=0
        self.vr=0.0
        self.thrust=0
        self.thrustframe=1
        self.rotation=0
        left_location=1
        eighties.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        eighties.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        eighties.listenKeyEvent("keydown", "right arrow", self.rotationOnLeft)
        eighties.listenKeyEvent("keyup", "right arrow", self.rotationOff)
        eighties.listenKeyEvent("keydown", "left arrow", self.rotationOnRight)
        eighties.listenKeyEvent("keyup", "left arrow", self.rotationOff)
        self.fxcenter=self.fycenter=0.5
        
    def step(self):
        self.x+=self.vx
        self.y+=self.vy
        self.rotation+=self.vr
        if self.thrust==1:
            self.setImage(self.thrustframe)
            self.thrustframe+=1
            self.vx+=.05*math.cos((self.rotation+math.pi/2))
            self.vy+=.05*math.sin((self.rotation-math.pi/2))
            if self.thrustframe==4:
                self.thrustframe=1
            else:
                self.setImage(0)
        if self.vr==.1:
            self.rotation=self.rotation+.0001
        if self.vr==-0.1:
            self.rotation=self.rotation-0.0001
        
        col=self.collidingWithSprites(Sun)
        if col:
            self.explode(self)
        
    def rotationOnLeft(self, event):
        self.vr=-.1
        
    def rotationOnRight(self, event):
        self.vr=.1
        
    def rotationOff(self, event):
        self.vr=0
        
    def thrustOn(self, event):
        self.thrust=1
        
    def thrustOff(self, event):
        self.thrust=0
        
    def thrustdecel(self, event):
        self.thrust=0.5
    
    def explode(self, event):
        self.visible=False
        self.vx=0
        self.vy=0
        ExplosionSmall(self.position)
    
class ExplosionSmall(Sprite):
    
    asset=ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
    boomasset=SoundAsset("sounds/explosion1.mp3")
    
    def __init__(self, position):
        super().__init__(ExplosionSmall.asset, position)
        self.image=0
        self.center=(0.5, 0.5)
        self.boom=Sound(ExplosionSmall.boomasset)
        self.boom.play()
        
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image=self.image + 1
        if self.image==20:
            self.destroy()
            
class Sun(Sprite):
    asset=ImageAsset("images/sun.png")
    width=85 #80
    length=80 #76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.mass=30*1000
        self.fxcenter=.5
        self.fycenter=.5

class eighties(App):
   
    def space(self, evt):
        if self.state in ['instructions', 'gameover']:
            for t in self.tsprites.values():
                t.visible=False
            self.state='playing'
            self.Tlast=time()
            evt.consumed=True
            self.ship1.newgame()
            self.ship2.newgame()
            
    def __init__(self, width, height):
        global sun
        super().__init__(width, height)
        bg_asset=ImageAsset("images/starfield.jpg")
        txt_asset=TextAsset("Blizzard: RnR", width = 9000, align ='center', style='47px Times', fill=Color(0xff2222,1)) 
        bg=Sprite(bg_asset, (0,0))
        bg=Sprite(bg_asset, (0,512))
        bg=Sprite(bg_asset, (512,0))
        bg=Sprite(bg_asset, (512,512))
        txt=Sprite(txt_asset, (0,0))
        sun_asset=ImageAsset("images/sun.png")
        sun=Sun ((400,300))
        left_location=1
        SpaceShip((300,350))
        SpaceShip2((600,350))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(SpaceShip2):
            ship.step()
        explosions=self.getSpritesbyClass(ExplosionSmall)
        for explosion in explosions:
            explosion.step()
            
myapp = eighties(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
