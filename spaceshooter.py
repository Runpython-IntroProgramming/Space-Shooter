"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
"""
Plan:
Create a Space Shooter game.
How:
Include these sprites:
    Background
    Sun
    Rocket 1
    Rocket 2
    Thruster Sprite - with noise (I think)
    Explosion Sprite - with noise (I think)

Have movement:
    Control the rockets with arrow/WASD keys
    Make the bullets move in an arbitrary curve
    Make the rockets move, always
    
Have collisions:
    When the bullet enters a certain area around the rocket sprite, make the rocket explode.
    When the rocket enters a certain area around the center, make the rocket explode.
    When the rockets enter a certain area around another rocket, they both explode.
    Basically, make it so that IF a sprite has the same (X, Y) as another sprite, what has been hit explodes.
    
Start!
    Structure of code:
        Code Sprites:
        Rocket 1
            Explosions
            Fake Gravity
            Movement
            Collisions
        Rocket 2
            Explosions
            Fake Gravity
            Movement
            Collisions
        Background
        Sun
        Code App.Run() stuff
        Refer to reference if code doesn't work well.
    
"""
app = SpaceShootOut()
app.run()