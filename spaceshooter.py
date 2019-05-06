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

class Explosion(Sprite):
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10, 'horizontal')
    
    def __init__(self, position):
        super().__init__(Explosion.asset, position)
        self.fxcenter = self.fycenter = 0.5
        self.countup = 0
        self.countdown = 10
        
    def step(self):
        # Manage explosion animation
        if self.countup < 10:
            self.setImage(self.countup%10)
            self.countup += 1
        else:
            self.setImage(self.countdown%10)
            self.countdown -= 1
            if self.countdown == 0:
                self.destroy()

class Bullet(Sprite):
    asset = ImageAsset("images/blast.png", Frame(0,0,8,8), 8, 'horizontal')
    
    def __init__(self, position, direction):
        super().__init__(Bullet.asset, [position[0] - 50 * math.sin(direction), position[1] - 50 * math.cos(direction)])
        self.vx = -2.5 * speed_limit * math.sin(direction)
        self.vy = -2.5 * speed_limit * math.cos(direction)
        self.vr = 0
        self.fxcenter = self.fycenter = 0.5
        self.bulletphase = 0
        self.collisions = []
        
    def collision(self):
        [self.collisions.append(x) for x in self.collidingWithSprites(PlayerShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(EnemyShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(Bullet)]
        if collisions:
            self.destroy()
            [Explosion((x.x, x.y)) for x in self.collisions]
            [x.destroy() for x in self.collisions]
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
        # manage bullet animation
        self.setImage(self.bulletphase%7)
        self.bulletphase += 1

# General SpaceShip Class        
class PlayerShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227-65,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(PlayerShip.asset, position, CircleAsset(32.5))
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        
        self.collisions = []
        
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
        
    def collision(self):
        [self.collisions.append(x) for x in self.collidingWithSprites(PlayerShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(EnemyShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(Bullet)]
        if self.collisions:
            Explosion((self.x, self.y))
            self.destroy()
            [Explosion((x.x, x.y)) for x in self.collisions]
            [x.destroy() for x in self.collisions]

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
    
# Enemy Ship
class EnemyShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position, challenge):
        super().__init__(EnemyShip.asset, position, CircleAsset(32.5))
        self.vx = 0
        self.vy = 0
        self.vr = 0.00
        self.fxcenter = self.fycenter = 0.45
        
        # Counter used for random movements
        self.count = 0
        self.difficulty = challenge
        print(self.difficulty)
        
        self.collisions = []
        
        # Spaceship thrust on/off
        self.thrust = 0
        self.thrustframe = 1
        
    def thrustOn(self):
        self.thrust = 1
        deltavx = -(math.sin(self.rotation)) * 0.05
        deltavy = -(math.cos(self.rotation)) * 0.05
        self.vx += deltavx
        self.vy += deltavy
        speed = (self.vx**2+ self.vy**2)**0.5
        if speed > speed_limit:
            self.vx += -deltavx
            self.vy += -deltavy
        
    def thrustOff(self):
        self.thrust = 0
        
    def rotateLeftOn(self):
        if self.vr < 0.05:
            self.vr += 0.01
        
    def rotateRightOn(self):
        if self.vr > -0.05:
            self.vr += -0.01
        
    def rotateRightOff(self):
        self.vr = 0
        
    def shoot(self):
        Bullet((self.x, self.y), self.rotation)
        
    def collision(self):
        [self.collisions.append(x) for x in self.collidingWithSprites(PlayerShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(EnemyShip)]
        [self.collisions.append(x) for x in self.collidingWithSprites(Bullet)]
        if self.collisions:
            Explosion((self.x, self.y))
            self.destroy()
            [Explosion((x.x, x.y)) for x in self.collisions]
            [x.destroy() for x in self.collisions]
        return self.collisions
        
    def turnTowardsPlayer(self, playerx, playery):
        #if 
            
    def step(self):
        # Randomly move
        if self.count%self.difficulty == 0:
            if random.randint(0,1) == 1:
                self.thrustOn()
            if random.randint(0,1) == 1:
                self.thrustOff()
            #if random.randint(0,1) == 1:
                #self.rotateRightOn()
            #if random.randint(0,1) == 1:
                #self.rotateLeftOn()
            if random.randint(0,1) == 1:
                self.shoot()
        self.count += 1
        
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
        
        #sun_asset = ImageAsset("images/sun.png")
        #sun_sprite = Sprite(sun_asset, (self.width / 2, self.height / 2))
        
        # Start Player1 in center of screen
        self.player1 = PlayerShip((self.width/2,self.height/2))
        # Start enemy ship @ random location on screen
        self.safex = 0
        self.safey = 0
        self.safeRespawn()
        # Sets difficulty level of enemy ship (frequency of which it makes movements)
        self.challenge = 100
        EnemyShip((self.safex,self.safey), self.challenge)
        

        
    def safeRespawn(self):
        self.safex = random.randint(0,self.width)
        self.safey = random.randint(0,self.height)
        while abs(self.safex - self.player1.x) < 100 and abs(self.safey - self.player1.y) < 100:
            self.safex = random.randint(0,self.width)
            self.safey = random.randint(0,self.height)
        
    def step(self):
        for ship in self.getSpritesbyClass(PlayerShip):
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
            # Check to see if ship has collided with anything
            ship.collision()
        
        for ship in self.getSpritesbyClass(EnemyShip):
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
            
            # Check to see if ship has collided with anything
            if ship.collision():
                # Increases frequency of enemy movements
                if self.challenge > 10:
                    self.challenge -= 5
                EnemyShip((random.randint(0,self.width),random.randint(0,self.height)), self.challenge)
                # Spawns multiple enemy ships each time one is killed.  Still need to work out the bugs...
                #if random.randint(0,1) == 1:
                    #EnemyShip((random.randint(0,self.width),random.randint(0,self.height)))
                
        for bullet in self.getSpritesbyClass(Bullet):
            bullet.step()
            if bullet.x < -10 or bullet.x > self.width + 10 or bullet.y < -10 or bullet.y > self.height + 10:
                bullet.destroy()
                
        for explosion in self.getSpritesbyClass(Explosion):
            explosion.step()

myapp = SpaceGame()
myapp.run()