"""
spaceshooter.py
Author: Nathan Subrahmanian
Credit: https://stackoverflow.com/questions/8696322/why-does-this-attributeerror-in-python-occur

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
eye = Color(0xdee5ef, 1.0)
sand = Color(0xefe49b, 1.0)
meadowgreen = Color(0x8ed334, 1.0)
orange = Color(0xe59e19, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)

class Background(App):
    bg_asset = ImageAsset("images/starfield.jpg",
        Frame(227,0,1000,1250), 4, 'vertical')
    bg = Sprite(bg_asset, (150,150))
    def __init__(self):
        super().__init__()


myapp = Background()

myapp.run()