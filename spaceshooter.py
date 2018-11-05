"""
spaceshooter.py
Author: Katie Naughton
Credit: Tutorials

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

#spaceship
class SpaceShip(Sprite):
    
    r_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
    
    pewasset = SoundAsset("sounds/pew1.mp3")
    
    def __init__(self, position):
        super().__init__(SpaceShip.r_asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.scale=.5
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        SpaceGame.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        SpaceGame.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        SpaceGame.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5
        self.pew=Sound(SpaceShip.pewasset)
        self.pew.volume=5
        
        
    def rightarrowKey(self, event):
        self.vx+=.5
        self.pew.play()
        
        
    def leftarrowKey(self, event):
        self.vx+=-.5
        self.pew.play()
        
    def uparrowKey(self, event):
        self.vy+=-.5
        self.pew.play()
        
    def downarrowKey(self, event):
        self.vy+=.5
        self.pew.play()
       
        
        
    def step(self):
        self.x+=self.vx
        self.y += self.vy
        self.rotation += self.vr
        collision=(self.collidingWithSprites(Asteroid))
        if collision:
            print("colliding")
            self.visible=False
        
        
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
        
#asteroid
class Asteroid(Sprite):
    
    a_asset = ImageAsset("images/1346943991.png")
    
    def __init__(self, position):
        super().__init__(Asteroid.a_asset, position)
        self.vx=1
        self.vy=1
        self.vr=0.01
        self.scale=0.05
        self.fxcenter = self.fycenter = 0.5
        
        
    def step(self):
        self.x+=self.vx
        self.y += self.vy
        self.rotation += self.vr
        
#explosion
class Explosion(Sprite):
    ex_asset = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
    boomasset = SoundAsset("sounds/explosion2.mp3")

    def __init__(self):
        super().__init__()
        
    
        
#spacegame
class SpaceGame(App):
    def __init__(self):
        super().__init__()
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/e36d28c490fe26653e50fbd17025f3ef.jpg")
        width=500
        height=500
        bg = Sprite(bg_asset)
        bg.scale=1.4
        SpaceShip((40,100))
        Asteroid((400, 100))
        Asteroid((600, 30))
        Asteroid((800, 300))
        
        #moon
        mn_asset=ImageAsset("images/super-moon.png")
        mn= Sprite(mn_asset, (300, 200))
        mn.scale=0.2
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
           ship.step()
        for asteroid in self.getSpritesbyClass(Asteroid):
            asteroid.step()
    

myapp = SpaceGame()

myapp.run()
