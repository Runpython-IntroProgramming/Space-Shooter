"""
spaceshooter.py
Author: Nathan Subrahmanian
Credit: https://stackoverflow.com/questions/8696322/why-does-this-attributeerror-in-python-occur

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
eye = Color(0xdee5ef, 1.0)
sand = Color(0xefe49b, 1.0)
meadowgreen = Color(0x8ed334, 1.0)
orange = Color(0xe59e19, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)



class Rocket(Sprite):
    rocketpic = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Rocket.rocketpic, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.scale=.5
        self.thrust = 0
        self.thrustframe = 1
        self.fxcenter = self.fycenter = 0.5
        SpaceShooter.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        SpaceShooter.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        SpaceShooter.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceShooter.listenKeyEvent("keyup", "space", self.thrustOff)
        
    def rightarrowKey(self, event):
        self.vx+=.5
        
    def leftarrowKey(self, event):
        self.vx+=-.5
        
    def uparrowKey(self, event):
        self.vy+=-.5
        
    def downarrowKey(self, event):
        self.vy+=.5
        
class SpaceShooter(App):
    def __init__(self):
        super().__init__()
        
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale=2

    Rocket((40,100))
    
myapp = SpaceShooter()

myapp.run()