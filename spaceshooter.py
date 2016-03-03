"""
spaceshooter.py
Author: David Wilson
Credit: Space War Source Code (by Mr. Dennsion)

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset

starback_asset = ImageAsset("images/starfield.jpg")

starback = Sprite(starback_asset, (0, 0))

myapp = App()
myapp.run()