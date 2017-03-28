"""
spaceshooter.py
Author: Kyle Postans
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH=2000
SCREEN_HEIGHT=500

class StarField(Sprite):
    field=ImageAsset("images/starfield.jpg")

class SpaceShip(Sprite):
    ship=ImageAsset
    
#class Explosions(Sprite):
    
#class Scorekeeping(object):   #maybe
    
#class Projectiles(Sprite):
    

    
class SpaceGame(App):