"""
spaceshooter.py
Author: emBrileg08
Credit: Example Spaceshooter code

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
        z=0
        while z<self.width:
            Sprite(Background.asset,(z,0))
            z+=Background.width
    
myapp=Spacewar()
myapp.run()