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
    def __init__(self, position):
        super().__init__(Sun.asset, position)

class Suns(Sprite):
    image=ImageAsset("images/sun.png")
    width=100
    height=100

    def __init__(self, position):
        super().__init__(Sun.asset, position)

class Moving(Sprite):
    image=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png")
    width=100
    height=100
    def __init__(self, position):
        super().__init__(Sun.asset, position)
class Galaxy(Sprite):
    image=ImageAsset("images/starfield.jpg")
    width=1000
    height=600
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
    


#Fin
myapp = SpaceGame(0,0)
myapp.run()