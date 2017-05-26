 from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

 
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

#SUNBRUH
 
class sun(Sprite):
   asset = ImageAsset("images/sun.png")
   width = 69
   height = 70
  
   def __init__(self, position):
       super().__init__(sun.asset, position)
   def step(self):
       i

#background starfield
class starfield(Sprite):
    asset=ImageAsset("Space-Shooter/images/starfield.jpg")
    width = 512
    height = 512
    def __init__(self,position):
        super().__init__(Stars.asset,position)
#ship
class Ship(Sprite):
    
    asset = ImageAsset("Space-Shooter/images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,86,125), 4, 'vertical')

        
myapp = App()
myapp.run()