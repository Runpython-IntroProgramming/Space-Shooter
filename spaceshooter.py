"""
spaceshooter.py
Author: Suhan Gui
Credit:
Assignment: Spaceshooter
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
#Colors
black
#Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#Fin
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()