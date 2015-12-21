"""
Space game
Ryan Kynor

Checklist:
fixed star field
~~Sun sprite~~
at least one player
muliple players or multplie inanimate objects to avoid
animated rocket thrust
collisions destroy ship
moving ships
rotating ships

Source:
lines 23 - 27 based off of orininal space game code
lines 123 and 124 taken from idea in original code
"""

#key list starts a line 1067 in ggame.py file

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import cos, sin
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Sun(Sprite):
    """
    The Sun on the Screen
    """
    
    asset =  ImageAsset("images/sun.png")
    height = 80
    width = 80
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.weight = 1
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()
        
        
     
class Starfield(Sprite):
    """
    The Starfield
    """
    
    asset = ImageAsset("images/starfield.jpg")
    #height = SCREEN_HEIGHT
    #width = SCREEN_WIDTH
    
    def __init__(self, position):
        super().__init__(Starfield.asset, position)
        self.weight = 1
        self.fxcenter = 0.5
        self.fycenter = 0.5



class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

#spaceship spawn movement
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.thrust = 0
        self.thrustframe = 1
        self.rotateRight = 0
        self.rotateLeft = 0
        self.forward = 0   # <<<
       
        #Thrust detection
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
       
        #Rotation detection
        
        SpaceGame.listenKeyEvent("keydown", "w", self.moveFowardOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.moveFowardOff)
        """
        SpaceGame.listenKeyEvent("keydown", "s", self.moveBackOn)
        SpaceGame.listenKeyEvent("keyup", "s", self.moveBackOff)
        """
        
        SpaceGame.listenKeyEvent("keydown", "a", self.rotateLeftOn)
        SpaceGame.listenKeyEvent("keyup", "a", self.rotateLeftOff)
        
        SpaceGame.listenKeyEvent("keydown", "d", self.rotateRightOn)
        SpaceGame.listenKeyEvent("keyup", "d", self.rotateRightOff)
        #Rotation animation
       
        #SpaceGame.listenKeyEvent("keydown", "w",
        self.fxcenter = self.fycenter = 0.5

#display of thrust
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            self.vy = self.vy -0.1
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(0)

        #if self.collision(self.app.sun) == true:
        #    self.explode()

#rotation
        if self.rotateRight == 1:
            self.vr = self.vr -0.0001
        if self.rotateLeft == 1:
            self.vr = self.vr +0.0001
        self.rotation += self.vr   # <<<< change rotation!
        if self.forward == 1:  # <<<< forward
            self.y+=(-cos(self.rotation))
            self.x+=(-sin(self.rotation))
        

#thrust
    def thrustOn(self, event):
        self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
#explode
    def explode(self):
        print("explode")
        explosion(self.position)
        self.die()
        
#movement
    def moveFowardOn(self,event):
        self.foward = 1
    def moveFowardOff(self,event):
        self.foward = 0
    
    def moveRightOn(self,event):
        self.right = 1
    def moveRightOff(self,event):
        self.right = 0
        
    def moveLeftOn(self,event):
        self.left = 1
    def moveLeftOff(self,event):
        self.left = 0
        
    def moveBackOn(self,event):
        self.back = 1
    def moveBackOff(self,event):
        self.back = 0
        
#rotation
    def rotateRightOn(self,event):
        self.rotateRight = 1
    def rotateRightOff(self,event):
        self.rotateRight = 0
        
    def rotateLeftOn(self,event):
        self.rotateLeft = 1
    def rotateLeftOff(self,event):
        self.rotateLeft = 0
        
#explosion image
class explosion(Sprite):
    asset = ImageAsset ("images/explosion2.png", Frame(0,0,128,128), 10, "horrizontal")
    def __init__(self,position):
        super().__init__(explosion.asset, position)
        #self.center = (0.5,0.5)
        self.Frame = 0
        self.eSpeed = 0
    def step(self):
        self.setImage(self.Frame)
        self.eSpeed += 0.3
        #self.Frame = init(self.eSpeed)
        self.Frame += 2
        if self.Frame == 10:
            self.destroy()   # <<< self.destroy() ??


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
       
        Starfield((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        Sun((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        SpaceShip((190,240))
        #SpaceShip((150,150))
        #SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explode in self.getSpritesbyClass(explosion):
            explode.step()


#Sun((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()



#self rotation will give you the current angle of rotation in radians