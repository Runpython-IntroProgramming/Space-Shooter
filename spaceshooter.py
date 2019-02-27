"""
spaceshooter.py
Author: emBrileg08
Credit: Example Spaceshooter

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset

class Background(Sprite):
    def __init__(self):
        super().__init__()
    asset=ImageAsset("images/starfield.jpg")
    width=512
    height=512

class Spacewar(App):
    def __init__(self):
        super().__init__()
        print(self.height)
        print(self.width)

myapp=Spacewar()
myapp.run()