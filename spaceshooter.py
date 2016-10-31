"""
spaceshooter.py
Author: Liam
Credit: http://stackoverflow.com/questions/16442923/how-to-insert-an-image-in-python,
http://stackoverflow.com/questions/28553439/python-pygame-how-would-i-get-my-sprite-to-rotate-in-the-direction-its-moving

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900


class SpaceShip(Sprite):
    #Animated space ship
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.rx = 1
        self.ry = -1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.moveL)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.moveR)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.nMoveL) #stop moving to the left
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.nMoveR) #stop moving to the right
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.x += self.vx
        self.y += self.vy
        #self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        while self.rx == -5:
            self.x=self.x-10
        while self.rx == 5:
            self.x=self.x+10
        #else self.x=self
    def thrustOn(self, event):
        self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def moveL(self,event):
        self.rx = -5
    def moveR(self,event):
        self.rx = 5
    def nMoveL(self,event):
        self.rx = -2
    def nMoveR(self,event):
        self.rx = 2
    

class SpaceGame(App):
    #Tutorial4 space game example.
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/kSQdCxM.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale = 0.6
        SpaceShip((100,100))
        #Spaceship((300,200))
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()