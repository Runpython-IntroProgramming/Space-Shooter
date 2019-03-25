"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame
import math, random
from time import time
class Background(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        for i in range (1,100):
            white=Color(0xbbbb00,1)
            starline=LineStyle(2,white)
            star_asset =RectangleAsset(10, 10, starline, white)
            star = Sprite(star_asset, ((random.randint(0,1000)),(random.randint(0,1000))))
class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,65,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
myapp = Background()
myapp.run()

