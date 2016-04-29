from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos

class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 1000
    height = 600

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = self.fycenter = 0.5
        
class Ship(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.fxcenter = self.fycenter = 0.5
        SpaceGame.listenKeyEvent('keydown', 'right arrow', self.rotateRight)
        SpaceGame.listenKeyEvent('keydown', 'left arrow', self.rotateLeft)
        SpaceGame.listenKeyEvent('keydown', 'up arrow', self.moveUp)
        SpaceGame.listenKeyEvent('keydown', 'down arrow', self.moveDown)
        SpaceGame.listenKeyEvent('keyup', 'up arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keyup', 'down arrow', self.thrustoff)
        SpaceGame.listenKeyEvent('keydown', 'space', self.fire)
        self.thrust = 0
        self.thrustframe = 0
    def rotateRight(self, event):
        self.rotation -= 0.1
    def rotateLeft(self, event):
        self.rotation += 0.1
    def moveUp(self, event):
        self.x += -5*sin(self.rotation)
        self.y += -5*cos(self.rotation)
        self.thrust = 1
    def moveDown(self, event):
        self.x += 5*sin(self.rotation)
        self.y += 5*cos(self.rotation)
        self.thrust = 1
    def thrustoff(self, event):
        self.thrust = 0
    def fire(self, event):
        Bullet((self.x,self.y))
        
    def step(self):
        if len(self.collidingWithSprites(Sun)) > 0:
            self.destroy()
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

        
class Bullet(Sprite):
     asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8)
     def __init__(self, position):
         super().__init__(Bullet.asset, position)
         
     
    
class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Stars((0,0))
        Sun((256,256))
        Ship((100,100))
        
    def step(self):
        for x in self.getSpritesbyClass(Ship):
            x.step()
        

        
        
        
        
    
SpaceGame().run()

