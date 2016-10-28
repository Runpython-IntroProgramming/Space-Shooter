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

class Star(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    
    def _init_ (self, width, height, positioning)
    self.w = width
    self.h = height
