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
    ship=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, "vertical")
    
    
#class Explosions(Sprite):
    
#class Scorekeeping(object):   #maybe
    
#class Projectiles(Sprite):
    

    
class SpaceGame(App):