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
    rocketasset = ImageAsset("four_spaceship_by_albertov_with_thrust.png")
    Frame((227,0,65,125), 4, 'vertical')
    
class SpaceGame(App):
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
    black = Color(0, 1)
    noline = LineStyle(0, black)
    bg_asset = RectangleAsset(self.width, self.height, noline, black)
    bg = Sprite(bg_asset, (0,0))
    SpaceShip((100,100))
    SpaceShip((150,150))
    SpaceShip((200,50))

myapp = SpaceGame()

myapp.run()
