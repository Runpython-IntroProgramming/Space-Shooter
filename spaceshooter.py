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
    def __init__(self,position):
        asset=ImageAsset("images/starfield.jpg")
        super().__init__(asset,position)
    width=512
    height=512
    
class Spaceship(Sprite):
    asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame((227,0,65,125), 4, 'vertical')
    def__init__(self,position):
        super().__init__(asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01

class Spacewar(App):
    def __init__(self):
        super().__init__()
        z=0
        a=0
        while z<self.width:
            Background((z,0))
            while a<self.height:
                Background((z,a))
                a+=Background.height
            a=0
            z+=Background.width
    
myapp=Spacewar()
myapp.run()