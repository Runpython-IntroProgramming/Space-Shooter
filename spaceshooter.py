 from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

 SCREEN_WIDTH = 0
 SCREEN_HEIGHT = 0
 #sunobstacle
 class sun(Sprite):
   asset = ImageAsset("images/sun.png")
   width = 100
   height = 100
   
   def __init__(self, position):
       super().__init__(sun.asset, position)
 
   def step(self):
 
       i
 #Ship 
 #ship Movement and directionals
 class SpaceShip(Sprite):
   asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
       Frame(227,0,292-227,125), 4, 'vertical')
   def __init__(self, position):
       super().__init__(SpaceShip.asset, position)
 
      
 
       self.rotation = 4.7
 
       self.vr = 0.01
 
       self.thrust = 0
 
       self.thrustframe = 1
 
       SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
 
       SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
 
       SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
 
       SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
 
       SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
 
       SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
 
       SpaceGame.listenKeyEvent("keyup", "d", self.thrustOff)
 
       SpaceGame.listenKeyEvent("keydown", "r", self.upKey)
 
       SpaceGame.listenKeyEvent("keydown", "q", self.downKey)
 
       self.fxcenter = self.fycenter = 0.7
 
 #other stuff and events that needs to work
   def step(self):
       if self.thrust == 1:
           self.setImage(self.thrustframe)
           self.thrustframe += 1
           if self.thrustframe == 4:
               self.thrustframe = 1
       lit = self.collidingWithSprites(sun)
       if len(lit) > 0:
           self.visible = True
   def thrustOn(self, event):
       self.thrust = 1
   def wKey(self,event):
       self.y-=10
   def sKey(self,event):
       self.y+=10
   def dKey(self,event):
       self.x+=15
       self.thrust = 1
   def aKey(self,event):
       self.x-=10
   def thrustOff(self, event):
       self.thrust = 0
   def upKey(self, event):
       self.rotation+=3/2
   def downKey(self, event):
       self.rotation-=3/2
 class SpaceGame(App):
   def __init__(self, width, height):
       super().__init__(width, height)
       black = Color(0, 1)
       noline = LineStyle(0, black)
       asset = ImageAsset("images/starfield.jpg")
       for x in range(self.width//500 + 1):
           for y in range(self.height//500 + 1):
               Sprite(asset,(x*500, y*500))
       SpaceShip((90,200))
       SpaceShip((90,300))
       SpaceShip((90,400))
       sun((600,250))
   def step(self):
       for ship in self.getSpritesbyClass(SpaceShip):
           ship.step()
           
 myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
 myapp.run()