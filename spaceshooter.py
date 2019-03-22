"""
spaceshooter.py
Author: Andrew 
Credit: Matt

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xFFFF00, 1.0)
skyblue = Color(0x87CEEB, 1.0)
grey = Color(0x696969, 1.0)
brick = Color(0xA52A2A, 1.0)
khaki = Color(0xF0E68C, 1.0)


thinline = LineStyle(1, black)

space = RectangleAsset(1500, 1000, thinline, black)

star = PolygonAsset([(0,10), (14,0), (28,10), (22,30), (6, 30)], thinline, yellow)




Sprite(space, (0, 0))

Sprite(star, (200, 200))

myapp = App()
myapp.width = 1600
myapp.height = 900
myapp.run()