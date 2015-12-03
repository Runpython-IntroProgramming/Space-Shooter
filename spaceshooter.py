"""
spaceshooter.py
Author: James Napier
Credit: Space War Source Code. Mr. Dennison


Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1665
SCREEN_HEIGHT = 945

class background(Sprite):
    def __init__(self, asset, position):
        super().__init__(asset, position)

class Sun(background):
    
    asset = ImageAsset("images/sun.png")
    width = 100
    height = 100
"""
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()
"""
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x #+= self.vx
        self.y #+= self.vy
        self.rotation #+= self.vr
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
    
    def Collision(self, event):
        if Ship.collidingwithsprites(Sun) == True:
            


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    
    def __init__(self, width, height):
        super().__init__(width, height)
        BG = ImageAsset("images/starfield.jpg")
        BGS = ImageAsset("images/sun.png")
        bgsprite = background(BG, (0,0))
        bgsprite.width = SCREEN_WIDTH
        bgsprite.height = SCREEN_HEIGHT
        bgs_sprite = Sun(BGS, (800, 450))
        self.ship = SpaceShip((400,450))
        
        
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'w', myapp.ship.thrustOn)
myapp.listenKeyEvent('keyup', 'w', myapp.ship.thrustOff)
"""
myapp.listenKeyEvent('keydown', 'a', TurnLOn)
myapp.listenKeyEvent('keyup', 'space', TurnLOff)
myapp.listenKeyEvent('keydown', 'd', TurnROn)
myapp.listenKeyEvent('keyup', 'space', TurnROff)
"""
myapp.run()