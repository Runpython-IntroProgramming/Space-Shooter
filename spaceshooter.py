"""
spaceshooter.py
Author: Andrew 
Credit: Matt

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Space(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self, position):
        super().__init__(Space.asset, position)
        
class Sun(Sprite):
    
    width = 80
    height = 76
    asset = ImageAsset("images/sun.png", Frame(0, 0, width, height))
    
    def __init__(self, position):
        super().__init__(Sun.asset, position, CircleAsset(32))
        
class Ship(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(0,0,86,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        
class Alien(Sprite):
    
    width = 148
    height = 150
    asset = ImageAsset("images/alien-in-spaceship-cartoon-sticker-1539712327.219355.png")
    def __init__(self, position):
        super().__init__(Alien.asset, position)
        self.scale = .5

class Chungus(Sprite):
    
    width = 148
    height = 150
    asset = ImageAsset("images/Chungus.png")
    def __init__(self, position):
        super().__init__(Chungus.asset, position)
        self.scale = .05

Space((0,0))
Space((512,0))
Space((1024,0))
Space((0,512))
Space((512,512))
Space((1024,512))
Sun((300,150))
Sun((100, 400))
Sun((700, 500))
Ship((200,200))
Alien((300, 300))
Chungus((750,0))

myapp = App()
myapp.run()
