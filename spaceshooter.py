"""
spaceshooter.py
Author: MaCucyrt07
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
"""
spaceshooter.py
Author: MaCucyrt07
Credit: Katie, Ella, Andrew

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, SoundAsset, Sound, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, TextAsset

class SpaceShip(Sprite):
    
    spaceship_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
   
    shotasset = SoundAsset("sounds/pew1.mp3")
    
    def __init__(self, position):
        super().__init__(SpaceShip.spaceship_asset, position)
        self.x=1
        self.y=1
        self.v=0.01
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
        self.pew=Sound(SpaceShip.shotasset)
        self.pew.volume=5
        
        
    def rightarrowKey(self, event):
        self.x+=.5
        self.pew.play()
        
        
    def leftarrowKey(self, event):
        self.x+=-.5
        self.pew.play()
        
    def uparrowKey(self, event):
        self.y+=-.5
        self.pew.play()
        
    def downarrowKey(self, event):
        self.y+=.5
        self.pew.play()
       
        
    def step(self):
        if self.x>(myapp.width-100) or self.x<0 or self.y>(myapp.height+100) or self.y<0:
            myapp.text.visible = True
        else: 
            self.x+=self.x
            self.y += self.y
            self.rotation += self.v
    
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
          
        if self.visible and self.collidingWithSprites(Asteroid):
            self.visible=False
            Explosion(self.position)
            myapp.text.visible=True
            
        
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
class Asteroid(Sprite):
    
    asteroid_asset = ImageAsset("images/1346943991.png")
    
    def __init__(self, position):
        super().__init__(Asteroid.asteroid_asset, position)
        self.x=1
        self.y=1
        self.v=0.01
        self.scale=0.05
        self.gcenter = self.fcenter = 0.5
        
        
    def step(self):
        if self.x>(myapp.width-100) or self.x<0:
            self.x=self.x*-1
        self.x+=self.x
        
        
        if self.y>myapp.height or self.y<0:
            self.y=self.y*-1
        self.y += self.y
        
        self.rotation += self.v
        
        

class Explosion(Sprite):
    
    image = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
    sound = SoundAsset("sounds/explosion2.mp3")
    
    def __init__(self, position):
        super().__init__(Explosion.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        self.boom = Sound(Explosion.boomasset)
        self.boom.play()
        
    def step(self):
        self.setImage(self.image//2) 
        self.image = self.image + 1
        if self.image == 50:
            self.destroy()

    



class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        
      
        black = Color(0, 1)
        noline = LineStyle(0, black)
        back_asset = ImageAsset("images/e36d28c490fe26653e50fbd17025f3ef.jpg")
        back = Sprite(back_asset, (0,0))
        back.scale=1.4
        
      
        self.text=Sprite(TextAsset("GAME OVER", width=500, align='center',style='60px Arial', fill=Color(0xff2222,1)), (300,350))
        self.text.visible= False
        
      
        SpaceShip((40,100))
        Asteroid((400,400))
        Asteroid((50,30))
        Asteroid((800,300))
        
        
       
        moon_asset=ImageAsset("images/super-moon.png")
        moon= Sprite(moon_asset, (300, 200))
        moon.scale=0.2
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
           ship.step()
    
        for asteroid in self.getSpritesbyClass(Asteroid):
            asteroid.step()
        for explosion in self.getSpritesbyClass(Explosion):
            explosion.step()
    

myapp = SpaceGame()

myapp.run()
