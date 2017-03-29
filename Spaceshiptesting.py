from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400


class SpaceField(Sprite):
    field=ImageAsset("images/starfield.jpg")
    
    
    
    def __init__(self, position):
         super().__init__(SpaceField.field, position)
         self.vx=1
         self.vy=1
         self.vr=0


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
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.Rotate)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.RotateOpposite)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.Stop)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.Stop)
        SpaceGame.listenKeyEvent("keydown", "w", self.Up)
        SpaceGame.listenKeyEvent("keydown", "s", self.Down)
        SpaceGame.listenKeyEvent("keydown", "a", self.Left)
        SpaceGame.listenKeyEvent("keydown", "d", self.Right)
       
        
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
    def Rotate(self, event):
        self.vr += 0.1
    def RotateOpposite(self, event):
        self.vr -=0.1
    def Stop(self, event):
        self.vr = 0.0
    def Up(self, event):
        self.vy -= 0.5
    def Down(self, event):
        self.vy += 0.5
    def Left(self, event):
        self.vx -= 0.5
    def Right(self, event):
        self.vx += 0.5
"""
class SpaceBlasts(Sprite):
    blast=ImageAsset("images/bunny.png")
    
    
    def __init__(self, position):
         super().__init__(SpaceBlasts.blast, position)
         self.vx=1
         self.vy=1
         self.vr=0
         SpaceGame.listenKeyEvent("keydown", "p", self.Blast)
         self.blast=False
    def step(self):
        self.x += self.vx
        self.y += self.vy
    def Blast(self, event):
        self.blast=True
         
"""
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceField((0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

    
    
        


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
