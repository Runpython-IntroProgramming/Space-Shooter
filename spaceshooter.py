"""
spaceshooter.py
Author: Nils Kingston
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600

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

    def controlup(self, event):
        command = self.keymap[event.key]
        if command in ["left", "right"]:
            self.vr = 0
        elif command == "forward":
            self.velocity = 0


class SpaceGame(App):
 
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100), self)
       
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()