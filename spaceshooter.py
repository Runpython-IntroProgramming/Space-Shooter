"""
spaceshooter.py
Author: Daniel Wilson
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Stars(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Sun(Sprite):
    asset = ImageAsset("images/sun.png")
    width = 90
    height = 90
    def __init__(self, position):
        super().__init__(Sun.asset, position)

class Spaceship(Sprite):
    SpaceShip((100,100))
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png"),
    Frame((227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)




myapp = SpaceGame(SCREEN_WIDTH*1.5, SCREEN_WIDTH*1.5)
myapp.run()