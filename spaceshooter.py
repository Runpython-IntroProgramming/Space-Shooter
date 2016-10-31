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

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Background(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    height=280
    width=240
    
    def __init__(self, position):
        super().__init__(Background.asset, position)

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Background((0, 0))

app = SpaceGame(0,0)
app.run()
"""
def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))

super().__init__(width, height)
    for x in range(self.width//Background.width + 1):
        for y in range(self.height//Background.height + 1):
            Background((x*Background.width, y*Background.height))
"""