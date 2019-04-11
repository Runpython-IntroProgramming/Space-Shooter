"""
spaceshooter.py
Author: Sean
Credit: Tutorials

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""

from ggame import App, RectangleAsset, CircleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math

class Bullet(Sprite):
    
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, red)
    # Red bullets (boring)
    asset = CircleAsset(5, noline, red)
    
    # How to get this frame working?
    #asset = ImageAsset("images/blast.png", Frame(0,0,64,8), 8, 'horizontal')
    
    #asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position, direction):
        super().__init__(Bullet.asset, [position[0] - 50 * math.sin(direction), position[1] - 50 * math.cos(direction)])
        self.vx = -5 * math.sin(direction)
        self.vy = -5 * math.cos(direction)
        self.vr = 0
        self.fxcenter = self.fycenter = 0.5
        self.bulletphase = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
        # manage bullet animation
        #self.setImage(self.bulletphase%7)
        #self.bulletphase += 1
        
        

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        
        # Shoot
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        
        # Rotate right/left
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        #SpaceGame.listenKeyEvent("keyup", "left arrow", self.rotateLeftOff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        #SpaceGame.listenKeyEvent("keyup", "right arrow", self.rotateRightOff)
        
        # Move right/left
        #SpaceGame.listenKeyEvent("keydown", "a", self.moveLeftOn)
        #SpaceGame.listenKeyEvent("keyup", "a", self.moveLeftOff)
        #SpaceGame.listenKeyEvent("keydown", "d", self.moveRightOn)
        #SpaceGame.listenKeyEvent("keyup", "d", self.moveRightOff)
        
        # Move up/down
        #SpaceGame.listenKeyEvent("keydown", "w", self.moveUpOn)
        #SpaceGame.listenKeyEvent("keyup", "w", self.moveUpOff)
        #SpaceGame.listenKeyEvent("keydown", "s", self.moveDownOn)
        #SpaceGame.listenKeyEvent("keyup", "s", self.moveDownOff)
        
        self.fxcenter = self.fycenter = 0.45
        
    def thrustOn(self, event):
        self.thrust = 1
        self.vx += -(math.sin(self.rotation)) *0.05
        self.vy += -(math.cos(self.rotation)) * 0.05
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def rotateLeftOn(self, event):
        if self.vr < 0.1:
            self.vr += 0.01
        
    def rotateLeftOff(self, event):
        self.vr = 0
        
    def rotateRightOn(self, event):
        if self.vr > -0.1:
            self.vr += -0.01
        
    def rotateRightOff(self, event):
        self.vr = 0
        
    def moveLeftOn(self, event):
        self.vx += -1
    
    def moveLeftOff(self, event):
        self.vx = 0
        
    def moveRightOn(self, event):
        self.vx += 1
        
    def moveRightOff(self, event):
        self.vx = 0
        
    def moveUpOn(self, event):
        self.vy += -1
        
    def moveUpOff(self, event):
        self.vy = 0
        
    def moveDownOn(self, event):
        self.vy += 1
        
    def moveDownOff(self, event):
        self.vy = 0
        
    def shoot(self, event):
        Bullet((self.x, self.y), self.rotation)

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #bg_asset = RectangleAsset(self.width, self.height, noline, black)
        #bg = Sprite(bg_asset, (0,0))
        starfield_asset = ImageAsset("images/starfield.jpg")
        starfield_sprite = Sprite(starfield_asset, (0,0))
        # Scale the sprite according to size of screen
        if self.width > self.height:
            starfield_sprite.scale = self.width / starfield_sprite.width
        else:
            starfield_sprite.scale = self.height / starfield_sprite.height
        
        sun_asset = ImageAsset("images/sun.png")
        sun_sprite = Sprite(sun_asset, (self.width / 2, self.height / 2))
        
        player1 = SpaceShip((100,100))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
            # Wrap screen
            # Check to see if ship has moved off-screen and correct
            if ship.x > self.width + 50:
                ship.x = -50
            elif ship.x < -50:
                ship.x = self.width + 50
            if ship.y < -50:
                ship.y = self.height + 50
            elif ship.y > self.height + 50:
                ship.y = -50
                
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()

myapp = SpaceGame()
myapp.run()