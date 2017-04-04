"""
spaceshooter.py
Author: Sam Pych
Credit: source code for space shhooter

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar

Your game must include the following:

A fixed star field background.
At least one player.
Either multiple playes, or some (in)animate object(s) to avoid.
Animated rocket thrust for the ship sprites.
Collisions destroy ships.
Moving and rotating ships - physics realism at your discretion.
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    