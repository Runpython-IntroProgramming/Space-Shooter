"""
spaceshooter.py
Author: David Wilson
Credit: Space War Source Code (by Mr. Dennsion)

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset, Frame

starback_asset = ImageAsset("images/starfield.jpg")
ship1_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(0,0,85,125))#227

starback = Sprite(starback_asset, (0,0))
ship1 = Sprite(ship1_asset, (0,0))

myapp = App()
myapp.run()