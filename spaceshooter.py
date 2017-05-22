from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class starfield(Sprite):
    asset=ImageAsset("Space-Shooter/images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self,position):
        super().__init__(Stars.asset,position)

class Ship(Sprite):
    
    asset = ImageAsset("Space-Shooter/images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')

app = spacegame(0,0)
app.run()