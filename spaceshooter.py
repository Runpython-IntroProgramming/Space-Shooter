"""
spaceshooter.py
Author: Suhan Gui
Credit: Spacewar
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ship(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov.png")
    width=100
    height=100
    def

class Suns(Sprite):
    image=ImageAsset("images/sun.png")
    width=100
    height=100
    def

class Moving(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png")
    width=100
    height=100
    def

class Galaxy(Sprite):
    image=ImageAsset("images/starfield.jpg")
    width=1300
    height=900
    
    def __init__(self, position):
        super().__init__(Galaxy.asset, position)
    
class SpaceGame(App):
    strings={'fail':'You fail :(',
    'win':'YOU WON!!'
    'bottom':'Press ENTER to begin!',
    'left':'Get the square without dying!"
    'right':'Arrow keys to move',
    }


#Fin
myapp = SpaceGame(0,0)