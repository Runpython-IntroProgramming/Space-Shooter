"""
spaceshooter.py
Author: Suhan Gui
Credit: Spacewar
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Galaxy(Sprite):
    image=ImageAsset
class Meteors(Sprite):
    image=ImageAsset

#Fin
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()