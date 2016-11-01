"""
spaceshooter.py
Author: Bauti Gallino
Credit: none

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

class Background(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    height= 512
    width= 512
    
    def __init__(self, position):
        super().__init__(Background.asset, position)

class Spaceship(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
            
    def __init__(self, position):
        super().__init__(Spaceship.asset, position)

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Background.width + 1):
            for y in range(self.height//Background.height + 1):
                Background((x*Background.width, y*Background.height))
        Background((0, 0))
        Spaceship((0, 0))

app = SpaceGame(1897, 935)
app.run()
"""
super().__init__(width, height)
    for x in range(self.width//Background.width + 1):
        for y in range(self.height//Background.height + 1):
            Background((x*Background.width, y*Background.height))
"""