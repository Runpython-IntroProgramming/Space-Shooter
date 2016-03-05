"""
spaceshooter.py
Author: David Wilson
Credit: Mr. Dennison ("Space War Source Code" and "Advanced Graphics with Classes")

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Sprite, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class StarBack(Sprite):
    
    asset = ImageAsset("images/starfield.jpg", Frame(0,0,SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    
    def __init__(self, position):
        super().__init__(StarBack.asset, position)
        self.scale = 2
        
class SpaceShip(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
        
    self.fxcenter = self.fycenter = 0.5
        
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)

class SpaceGame(App):
    def __init__(self):
        super().__init__()
        StarBack((0,0))
        SpaceShip((0,0))
        
        
myapp = SpaceGame()
myapp.run()

'''
from ggame import App, Sprite, ImageAsset, Frame

class starback(Sprite):
    starback_asset = ImageAsset("images/starfield.jpg")
    starback = Sprite(starback_asset, (0,0))
    
class ship1(Sprite):
    ship1_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(0,0,85,125))
    def __init__(self, position):
        super().__init__(ship1.ship1_asset, position)
        ship1 = Sprite(ship1_asset, (0,0))

myapp = App()
myapp.run()
'''
