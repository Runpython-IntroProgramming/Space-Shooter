"""
spaceshooter.py
Author: Nils Kingston
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600

class SpaceShip(Sprite):
  
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr


class SpaceGame(App):
 
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        asset = ImageAsset("Space-Shooter/images/starfield.jpg" 
        #bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()