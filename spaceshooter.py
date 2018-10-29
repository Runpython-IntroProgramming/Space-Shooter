"""
spaceshooter.py
Author: Katie Naughton
Credit: Tutorials

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


    
'''
class SpaceShip(Sprite):
    
    r_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(SpaceShip.r_asset, position)
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
'''

class Asteroid(Sprite):
    
    a_asset = ImageAsset("images/1346943991.png")
    
    def __init__(self, position):
        super().__init__(Asteroid.a_asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.scale=0.1
        self.fxcenter = self.fycenter = 0.5
        
        
    def step(self):
        self.x+=self.vx
        self.y += self.vy
        self.rotation += self.vr

    
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/e36d28c490fe26653e50fbd17025f3ef.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale=1.4
        #SpaceShip((400,100))
        Asteroid((500, 100))
        Asteroid((40, 100))
        Asteroid((300, 50))
        
        #moon
        mn_asset=ImageAsset("images/super-moon.png")
        mn= Sprite(mn_asset, (300, 200))
        mn.scale=0.2
        
      
        #asteroids
        #coordlist=[(50,0), (500, 350), (300,400), (800, 75)]
        #at_asset=ImageAsset("images/1346943991.png")
        
        #for coord in coordlist:
            #at=Sprite(at_asset, coord)
            #at.scale=0.1
        
    def step(self):
        #for ship in self.getSpritesbyClass(SpaceShip):
        #    ship.step()
        for asteroid in self.getSpritesbyClass(Asteroid):
            asteroid.step()
    
    
    
    

myapp = SpaceGame()

r_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
rocket=Sprite(r_asset, (0,0))
rocket.direction=1
rocket.go=True
def reverse (r):
    r.direction*=-1
def step():
    if rocket.go:
        rocket.x += rocket.direction
        if rocket.x + rocket.width > myapp.width or rocket.x < 0:
            rocket.x -= rocket.direction
            reverse(rocket)
            
def rightarrowKey(event):
    print("right")
    rocket.go = not rocket.go

# Handle the "reverse" key
def leftarrowKey(event):
    print("left")
    reverse(rocket)

# Handle the mouse click
def mouseClick(event):
    rocket.x = event.x
    rocket.y = event.y
myapp.listenKeyEvent('keydown', 'right arrow', rightarrowKey)
myapp.listenKeyEvent('keydown', 'left arrow', leftarrowKey)
myapp.listenMouseEvent('click', mouseClick)


myapp.run()
