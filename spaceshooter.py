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

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov.png")
    width=100
    height=100
    

class Suns(Sprite):
    image=ImageAsset("images/sun.png")
    width=100
    height=100

class Moving(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png")
    width=100
    height=100
    

class Galaxy(Sprite):
    image=ImageAsset("images/starfield.jpg")
    width=SCREEN_WIDTH
    height=SCREEN_HEIGHT
    
class SpaceGame(App):
    

#Fin
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()