"""
spaceshooter.py
Author: Nils Kingston
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, SoundAsset
import math

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600

class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()

class SpaceShip(Sprite):
  
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position, app):
        # vr is change of rotation
        super().__init__(SpaceShip.asset, position)
        self.velocity = 0
        self.rotation = 0
        self.vr = 0
        self.app = app
        self.registerKeys(["a", "d", "w"])
        
    def step(self):
        self.y -= math.cos(self.rotation) * self.velocity
        self.x -= math.sin(self.rotation) * self.velocity
        self.rotation += self.vr
        
    def registerKeys(self, keys):
        commands = ["left", "right", "forward"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]

    def controldown(self, event):
        command = self.keymap[event.key]
        if command == "left":
            self.vr = 0.1
        elif command == "right":
            self.vr = -0.1
        elif command == "forward":
            self.velocity = 7
        while command == "left" or "right" or "forward":
            asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
                Frame(0,0,86,125), 4, 'vertical')
    

    def controlup(self, event):
        command = self.keymap[event.key]
        if command in ["left", "right"]:
            self.vr = 0
        elif command == "forward":
            self.velocity = 0


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
        self.setImage(self.image//2)  # slow it down
        self.image = self.image + 1
        if self.image == 50:
            self.destroy()

class SpaceGame(App):
 
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 2.75
        SpaceShip((100,100), self)
        Sun((600,260))
       
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
    
 

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()