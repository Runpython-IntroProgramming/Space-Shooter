"""
spaceshooter.py
Author: Sam Supattapone
Credit: original code

Assignment: Space Shooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time



asset = ImageAsset("images/starfield.jpg")
width = 512
height = 512

stars = Sprite(asset)
stars.width *= 3
stars.height *= 2

app = App()
app.run()
