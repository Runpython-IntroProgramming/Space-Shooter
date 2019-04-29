"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, CircleAsset, EllipseAsset, PolygonAsset


class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.up)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.down)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.left)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.right)
        SpaceGame.listenKeyEvent("keydown", "space", self.move)

        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.x == 400 and self.y == 400:
            self.destroy()
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def up(self, event):
        self.rotation = 90
    
    def down(self, event):
        self.rotation = 270
    
    def left(self, event):
        self.rotation = 180
    
    def right(self, event):
        self.rotation = 0
        
    def move(self, event):
        self.x += 5
        self.y += 5
        

class SpaceShip2(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip2.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1

        self.fxcenter = self.fycenter = 0.5


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip2((400, 400))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()





        
myapp = SpaceGame()
myapp.run()
