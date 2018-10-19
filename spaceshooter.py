"""
spaceshooter.py
Author: Katie Naughton
Credit: Tutorials

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

    class SpaceShip(Sprite):
        rocket_asset = ImageAsset("four_spaceship_by_albertov_with_thrust.png")
        Frame(227,0,65,125), 4, 'vertical')
    
    class SpaceGame(App):
        def __init__(self, position):
            super().__init__(SpaceShip.asset, position)
myapp = SpaceGame()

myapp.run()