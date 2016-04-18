from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 1000
    height = 600

    def __init__(self, position):
        super().__init__(Stars.asset, position)
        
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = self.fycenter = 0.5
        

class SpaceGame(App):
    
    def __init__(self):
        super().__init__()
        Stars((0,0))
        Sun((256,256))
    
SpaceGame().run()

