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
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

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
    
    asset1 = ImageAsset("images/starfield.png")
    height = SCREEN_HEIGHT
    width = SCREEN_WIDTH
    
    def __init__(self, position):
        super().__init__(Starfield.asset1, position)
        self.weight = 1
        self.fxcenter = 0.5
        self.fycenter = 0.5



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
        #Thrust animation
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        #Rotation animation
        #SpaceGame.listenKeyEvent("keydown", "w",
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
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
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Starfield((0,0))
        Sun((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        SpaceShip((100,100))
        #SpaceShip((150,150))
        #SpaceShip((200,50))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


#Sun((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))

myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()



#self rotation will give you the current angle of rotation in radians