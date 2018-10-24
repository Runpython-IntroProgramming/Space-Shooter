"""
spaceshooter.py
Author: Katie Naughton
Credit: Tutorials

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class SpaceShip(Sprite):
    
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x+=self.vx
        self.y += self.vy
        self.rotation += self.vr
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
    
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/e36d28c490fe26653e50fbd17025f3ef.jpg")
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
        mn_asset=ImageAsset("images/moon-1859616_960_720.jpg")
        mn= Sprite(mn_asset, (0, 0))

        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
    
    

myapp = SpaceGame()

myapp.run()
