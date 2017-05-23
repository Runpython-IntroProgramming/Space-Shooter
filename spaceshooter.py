from ggame import App, Sprite, ImageAsset, Frame, RectangleAsset
from ggame import SoundAsset, Sound, TextAsset, Color, LineStyle
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#background starfield
class starfield(Sprite):
    asset=ImageAsset("Space-Shooter/images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self,position):
        super().__init__(Stars.asset,position)
#ship
class Ship(Sprite):
    
    asset = ImageAsset("Space-Shooter/images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')

        
myapp = App()
myapp.run()