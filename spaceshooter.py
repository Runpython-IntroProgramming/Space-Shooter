"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
"""
Plan:
Create a Space Shooter game.
How:
Include these sprites:
    Background
    Sun
    Rocket 1
    Rocket 2
    Bullet Sprite - with noise
    Thruster Sprite - with noise (I think)
    Explosion Sprite - with noise (I think)

Have movement:
    Control the rockets with arrow/WASD keys
    Make the bullets move in an arbitrary curve
    Make the rockets move, always
    
Have collisions:
    When the bullet enters a certain area around the rocket sprite, make the rocket explode.
    When the rocket enters a certain area around the center, make the rocket explode.
    When the rockets enter a certain area around another rocket, they both explode.
    Basically, make it so that IF a sprite has the same (X, Y) as another sprite, what has been hit explodes.
    
Start!
"""
#Image assets
class Background(Sprite):
    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512
class Sun(Sprite):
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
"""
class R1(Sprite):
    
class R2(Sprite):
    
class Bullet(Sprite):
    
"""