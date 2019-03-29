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

Space((0,0))
myapp = App()
myapp.run()
