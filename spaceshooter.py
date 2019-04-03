"""
spaceshooter.py
Author: maBottnn14
Credit: Andrew

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


myapp = App()
#StarField:
class Stars(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512
    
    def __init__(self, position):
        super().__init__(Stars.asset, position)

#Monster
class monster(Sprite):
    op = ImageAsset("images/OGChungus.png")
    width = 50
    height = 50
    
    def __init__(self, position):
        super().__init__(monster.op, position)
        self.scale = 1


   


monster((1000,0))
Stars((512,0))
Stars((0,0))
Stars((1024,0))
Stars((0, 512))
Stars((512, 512))
Stars((1024, 512))

myapp = App()
myapp.run()