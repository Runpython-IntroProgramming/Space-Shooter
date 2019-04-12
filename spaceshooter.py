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
import random

speed_limit = 10

class Bullet(Sprite):
    
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, red)
    # Red bullets (boring)
    #asset = CircleAsset(5, noline, red)
    
    # How to get this frame working?
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8, 'horizontal')
    
    #asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position, direction):
        super().__init__(Bullet.asset, [position[0] - 50 * math.sin(direction), position[1] - 50 * math.cos(direction)])
        self.vx = -2.5 * speed_limit * math.sin(direction)
        self.vy = -2.5 * speed_limit * math.cos(direction)
        self.vr = 0
        self.fxcenter = self.fycenter = 0.5
        self.bulletphase = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
        # manage bullet animation
        self.setImage(self.bulletphase%7)
        self.bulletphase += 1

# General SpaceShip Class        
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227-65,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        
        # Spaceship thrust on/off
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        
        # Rotate right/left
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotateLeftOn)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotateRightOn)
        
        # Shoot
        SpaceGame.listenKeyEvent("keydown", "space", self.shoot)
        
        self.fxcenter = self.fycenter = 0.45
        
    def thrustOn(self, event):
        self.thrust = 1
        deltavx = -(math.sin(self.rotation)) *0.05
        deltavy = -(math.cos(self.rotation)) * 0.05
        self.vx += deltavx
        self.vy += deltavy
        speed = (self.vx**2+ self.vy**2)**0.5
        if speed > speed_limit:
            self.vx += -deltavx
            self.vy += -deltavy
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def rotateLeftOn(self, event):
        if self.vr < 0.05:
            self.vr += 0.01
        
    def rotateRightOn(self, event):
        if self.vr > -0.05:
            self.vr += -0.01
        
    def rotateRightOff(self, event):
        self.vr = 0
        
    def shoot(self, event):
        Bullet((self.x, self.y), self.rotation)

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        # Randomly execute events
        #self.thrust = random.randint(0,1)
        
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

# Player SpaceShip            
#class Player(SpaceShip):
    
    
# Enemy SpaceShip
    

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
            if bullet.x < -10 or bullet.x > self.width + 10 or bullet.y < -10 or bullet.y > self.height + 10:
                bullet.destroy()

myapp = SpaceGame()
myapp.run()