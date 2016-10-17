"""
spaceshooter.py
Author: vinzentmoesch
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
#import the stuff
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time


#background
class background(Sprite):

    asset = ImageAsset("images/Stars, background.jpg")
    width = 1024
    height = 1024

    def __init__(self, position):
        super().__init__(Stars.asset, position)