"""
spaceshooter.py
Author: Liam S
Credit: Mr. Dennison's Spacewar source code Vinzent for Photoshop Help

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Moon(Sprite):

    asset = ImageAsset("images/Le_Voyage_dans_la_lune_Transparent.png")
    def __init__(self, position):
        super().__init__(Moon.asset, position)
        self.counter = 0
        self.vx = 0
        self.vy = 0
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        if self.counter >= 0 and self.counter <= 25:
            self.vx = 1
            self.vy = 0
        if self.counter >= 25 and self.counter <= 40:
            self.vx = 0
            self.vy = 1
        if self.counter >= 40 and self.counter <= 65:
            self.vx = -1
            self.vy = 0
        if self.counter >= 65 and self.counter <= 80:
            self.vx = 0
            self.vy = -1
        if self.counter == 81:
            self.counter = 0
        self.counter += 1
        self.x += self.vx
        self.y += self.vy
class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,230,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vAddedx = 0
        self.vAddedy = 0
        self.vAddedr = 0
        self.sideThrust = 0
        self.vertThrust = 0
        self.RotThrust = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)
        
        
        SpaceGame.listenKeyEvent("keydown", "i", self.thrustCounterClock)
        SpaceGame.listenKeyEvent("keyup", "p", self.thrustClockoff)
        SpaceGame.listenKeyEvent("keyup", "i", self.thrustCounterClockoff)
        SpaceGame.listenKeyEvent("keydown", "p", self.thrustClock)
        
        
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        if self.sideThrust == 1:
            self.vAddedx += 0.05
        if self.sideThrust == -1:
            self.vAddedx -= 0.05
        if self.sideThrust == 0:
            self.vAddedx += 0
        if self.vertThrust == 1:
            self.vAddedy += 0.05
        if self.vertThrust == -1:
            self.vAddedy -= 0.05
        if self.vertThrust == 0:
            self.vAddedy += 0
        if self.RotThrust == 1:
            self.vAddedr = -0.03
        if self.RotThrust == -1:
            self.vAddedr = 0.03
        if self.RotThrust == 0:
            self.vAddedr = 0
        self.x += self.vAddedx
        self.y += self.vAddedy
        self.rotation += self.vAddedr
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
        
    def thrustLeft(self, event):
        self.sideThrust = -1

    def thrustRight(self, event):
        self.sideThrust = 1
    
    def thrustRightoff(self, event):
        self.sideThrust = 0
    
    def thrustLeftoff(self, event):
        self.sideThrust = 0
        
    
    def thrustUp(self, event):
        self.vertThrust = -1

    def thrustDown(self, event):
        self.vertThrust = 1
    
    def thrustDownoff(self, event):
        self.vertThrust = 0
    
    def thrustUpoff(self, event):
        self.vertThrust = 0

    def thrustCounterClock(self, event):
        self.RotThrust = -1

    def thrustClock(self, event):
        self.RotThrust = 1
    
    def thrustClockoff(self, event):
        self.RotThrust = 0
    
    def thrustCounterClockoff(self, event):
        self.RotThrust = 0

class SpaceShip2(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,230,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip2.asset, position)
        self.vx = 1
        self.vy = 1
        self.vAddedx = 0
        self.vAddedy = 0
        self.vAddedr = 0
        self.sideThrust = 0
        self.vertThrust = 0
        self.RotThrust = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)
        
        
        SpaceGame.listenKeyEvent("keydown", "i", self.thrustCounterClock)
        SpaceGame.listenKeyEvent("keyup", "p", self.thrustClockoff)
        SpaceGame.listenKeyEvent("keyup", "i", self.thrustCounterClockoff)
        SpaceGame.listenKeyEvent("keydown", "p", self.thrustClock)
        
        
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        if self.sideThrust == 1:
            self.vAddedx += 0.05
        if self.sideThrust == -1:
            self.vAddedx -= 0.05
        if self.sideThrust == 0:
            self.vAddedx += 0
        if self.vertThrust == 1:
            self.vAddedy += 0.05
        if self.vertThrust == -1:
            self.vAddedy -= 0.05
        if self.vertThrust == 0:
            self.vAddedy += 0
        if self.RotThrust == 1:
            self.vAddedr = -0.03
        if self.RotThrust == -1:
            self.vAddedr = 0.03
        if self.RotThrust == 0:
            self.vAddedr = 0
        self.x += self.vAddedx
        self.y += self.vAddedy
        self.rotation += self.vAddedr
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
        
    def thrustLeft(self, event):
        self.sideThrust = -1

    def thrustRight(self, event):
        self.sideThrust = 1
    
    def thrustRightoff(self, event):
        self.sideThrust = 0
    
    def thrustLeftoff(self, event):
        self.sideThrust = 0
        
    
    def thrustUp(self, event):
        self.vertThrust = -1

    def thrustDown(self, event):
        self.vertThrust = 1
    
    def thrustDownoff(self, event):
        self.vertThrust = 0
    
    def thrustUpoff(self, event):
        self.vertThrust = 0

    def thrustCounterClock(self, event):
        self.RotThrust = -1

    def thrustClock(self, event):
        self.RotThrust = 1
    
    def thrustClockoff(self, event):
        self.RotThrust = 0
    
    def thrustCounterClockoff(self, event):
        self.RotThrust = 0

class SpaceShip3(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,230,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip3.asset, position)
        self.vx = 1
        self.vy = 1
        self.vAddedx = 0
        self.vAddedy = 0
        self.vAddedr = 0
        self.sideThrust = 0
        self.vertThrust = 0
        self.RotThrust = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)
        
        
        SpaceGame.listenKeyEvent("keydown", "i", self.thrustCounterClock)
        SpaceGame.listenKeyEvent("keyup", "p", self.thrustClockoff)
        SpaceGame.listenKeyEvent("keyup", "i", self.thrustCounterClockoff)
        SpaceGame.listenKeyEvent("keydown", "p", self.thrustClock)
        
        
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        if self.sideThrust == 1:
            self.vAddedx += 0.05
        if self.sideThrust == -1:
            self.vAddedx -= 0.05
        if self.sideThrust == 0:
            self.vAddedx += 0
        if self.vertThrust == 1:
            self.vAddedy += 0.05
        if self.vertThrust == -1:
            self.vAddedy -= 0.05
        if self.vertThrust == 0:
            self.vAddedy += 0
        if self.RotThrust == 1:
            self.vAddedr = -0.03
        if self.RotThrust == -1:
            self.vAddedr = 0.03
        if self.RotThrust == 0:
            self.vAddedr = 0
        self.x += self.vAddedx
        self.y += self.vAddedy
        self.rotation += self.vAddedr
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
        
    def thrustLeft(self, event):
        self.sideThrust = -1

    def thrustRight(self, event):
        self.sideThrust = 1
    
    def thrustRightoff(self, event):
        self.sideThrust = 0
    
    def thrustLeftoff(self, event):
        self.sideThrust = 0
        
    
    def thrustUp(self, event):
        self.vertThrust = -1

    def thrustDown(self, event):
        self.vertThrust = 1
    
    def thrustDownoff(self, event):
        self.vertThrust = 0
    
    def thrustUpoff(self, event):
        self.vertThrust = 0

    def thrustCounterClock(self, event):
        self.RotThrust = -1

    def thrustClock(self, event):
        self.RotThrust = 1
    
    def thrustClockoff(self, event):
        self.RotThrust = 0
    
    def thrustCounterClockoff(self, event):
        self.RotThrust = 0

class SpaceGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))
        Moon((400,400))
        SpaceShip((400,400))
        SpaceShip2((630,400))
        SpaceShip3((860,400))
        
                    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for ship in self.getSpritesbyClass(SpaceShip2):
            ship.step()
        for ship in self.getSpritesbyClass(SpaceShip3):
            ship.step()
            
app = SpaceGame(1900,935)
app.run()
    

