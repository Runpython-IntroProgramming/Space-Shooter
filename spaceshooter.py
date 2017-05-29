 from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
 
 SCREEN_WIDTH = 0
 SCREEN_HEIGHT = 0

#SUNBRUH
 
 class sun(Sprite):
   asset = ImageAsset("images/sun.png")
   width = 100
   height = 100
  
   def __init__(self, position):
       super().__init__(sun.asset, position)
   def step(self):
       i

#Ship
 
 class SpaceShip(Sprite):
 
 
 
   asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
       Frame(227,0,292-227,125), 4, 'vertical')



   def __init__(self, position):
       super().__init__(SpaceShip.asset, position)
      
       self.rotation = 4.7
       self.vr = 0.01
       self.thrust = 0
       self.thrustframe = 1



#background starfield

 class starfield(Sprite):
    asset=ImageAsset("Space-Shooter/images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self,position):
        super().__init__(Stars.asset,position)

 class SpaceGame(App):
 
 
 
   def __init__(self, width, height):
       super().__init__(width, height)
       black = Color(0, 1)
       noline = LineStyle(0, black)
       asset = ImageAsset("images/starfield.jpg")
       for x in range(self.width//512 + 1):
           for y in range(self.height//512 + 1):
               Sprite(asset,(x*512, y*512))
       SpaceShip((50,550))
       SpaceShip((50,450))
       SpaceShip((50,650))
       sun((500,600))
   def step(self):
       for ship in self.getSpritesbyClass(SpaceShip):
           ship.step()

 myapp = App()
 myapp.run()