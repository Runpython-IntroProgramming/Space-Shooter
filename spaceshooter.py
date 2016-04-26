"""
spaceshooter.py
Author: Hagin
Credit: myself

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, Color, TextAsset, SoundAsset, Sound
from math import sqrt, sin, cos, radians, degrees, pi, atan
from random import randint
from time import sleep

SCREEN_WIDTH = 1000 #1200
SCREEN_HEIGHT = 600 #700
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)