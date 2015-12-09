from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class SpaceShip(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.turn = 0
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        #self.x += self.vx
        #self.y += self.vy
        self.rotation += self.turn/75
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
    
    def turnleftOn(self, event):
        self.turn = 1
    
    def turnleftOff(self, event):
        self.turn = 0
    
    def turnrightOn(self, event):
        self.turn = -1
    
    def turnrightOff(self, event):
        self.turn = 0



class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        self.ship = SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', myapp.ship.thrustOn)
myapp.listenKeyEvent('keyup', 'space', myapp.ship.thrustOff)
myapp.listenKeyEvent('keydown', 'a', myapp.ship.turnleftOn)
myapp.listenKeyEvent('keyup', 'a', myapp.ship.turnleftOff)
myapp.listenKeyEvent('keydown', 'd', myapp.ship.turnrightOn)
myapp.listenKeyEvent('keyup', 'd', myapp.ship.turnrightOff)
myapp.run()