"""
spaceshooter.py
Author: Avery Wallis
Credit: Original Spacewar Code, Daniel

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, ImageAsset, RectangleAsset, SoundAsset, Frame
from ggame import LineStyle, Sprite, Sound, Color

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.visible=True
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.rotation = .05
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.thrustDecel)
        SpaceGame.listenKeyEvent("keyup", "s", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "a" , self.CCOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.CCOff)
        SpaceGame.listenKeyEvent("keydown", "d" , self.CCthing)
        SpaceGame.listenKeyEvent("keyup", "d", self.CCOff)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx += self.rotation
            self.vy += self.rotation
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        if self.thrust == -1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vx=self.vx+.01
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)
        if self.vr==.1:
            self.rotation =self.rotation+.001
        if self.vr==-.1:
            self.rotation =self.rotation-.001
        if self.vr==0:
            self.rotation=self.rotation
            
        col= self.collidingWithSprites(Sunthing)
        if col:
            self.explode
        
    def thrustOn(self, event):
        self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def thrustDecel(self, event):
        self.thrust=-1
        
    def CCOn(self, event):
        self.vr=.1
    def CCOff(self, event):
        self.vr=0
    def CCthing(self, event):
        self.vr=-.1
    
    def explode(self):
        self.visible=False
        self.ExplosionSmall
        
        
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
        self.image += 1
        if self.image == 20:
            self.destroy()
            
class Sunthing(Sprite):
    asset=ImageAsset("images/sun.png")
    width=80
    length=76
    def __init__(self, position):
        super().__init__(Sunthing.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()
        
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        star0 = Sprite(bg_asset, (0,0))
        star1= Sprite(bg_asset, (512,0))
        star2= Sprite(bg_asset, (0,512))
        star3= Sprite(bg_asset, (512, 512))
        Sunthing((500,360))
        SpaceShip((100,100))
        
    def step(self):
            for ship in self.getSpritesbyClass(SpaceShip):
                ship.step() 

myapp = SpaceGame(SCREEN_WIDTH*1.5, SCREEN_HEIGHT*1.5)
myapp.run()
