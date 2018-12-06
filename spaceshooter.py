"""
spaceshooter.py
Author: Nathan Subrahmanian
Credit: https://stackoverflow.com/questions/8696322/why-does-this-attributeerror-in-python-occur
https://stackoverflow.com/questions/78799/is-there-a-benefit-to-defining-a-class-inside-another-class-in-python
Example Space Shooters
Space Shooters Source Code
Ggame Read the Docs Website

https://ggame-dev.readthedocs.io/en/latest/ggameapi.html

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
eye = Color(0xdee5ef, 1.0)
sand = Color(0xefe49b, 1.0)
meadowgreen = Color(0x8ed334, 1.0)
orange = Color(0xe59e19, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)


class Rocket(Sprite):
    rocketpic = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
    Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Rocket.rocketpic, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1

        SpaceShooter.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        SpaceShooter.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
                
    def rightarrowKey(self, event):
        self.vx+=.2
        
    def leftarrowKey(self, event):
        self.vx+=-.2
        
    def uparrowKey(self, event):
        self.vy+=-.2
        
    def downarrowKey(self, event):
        self.vy+=.2


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr

        if self.thrust == 5:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
            
    
    def collidingWithSprites(self, sclass = None):
        """
        Determine if this sprite is colliding with any other sprites
        of a certain class.
        
        :param class sclass: A class identifier that is either :class:`Sprite`
            or a subclass of it that identifies the class of sprites to check
            for collisions. If `None` then all objects that are subclassed from
            the :class:`Sprite` class are checked.
            
        :rtype: list
        
        :returns: A (potentially empty) list of sprite objects of the given
            class that are overlapping with this sprite.
        """
        if sclass is None:
            slist = App.spritelist
        else:
            slist = App.getSpritesbyClass(sclass)
        return list(filter(self.collidingWith, slist))        
            
    def destroy(self):
        App._remove(self)
        self.GFX.destroy()
            
            
            
    '''        
            
    def collidingWith(self, obj):
        if self is obj:
            return False
        else:
            self._setExtents()
            obj._setExtents()
            # Gross check for overlap will usually rule out a collision
            if (self.xmin > obj.xmax
                or self.xmax < obj.xmin
                or self.ymin > obj.ymax
                or self.ymax < obj.ymin):
                    return False
            # Otherwise, perform a careful overlap determination
            elif type(self.asset) is CircleAsset:
                if type(obj.asset) is CircleAsset:
                    # two circles .. check distance between
                    sx = (self.xmin + self.xmax) / 2
                    sy = (self.ymin + self.ymax) / 2
                    ox = (obj.xmin + obj.xmax) / 2
                    oy = (obj.ymin + obj.ymax) / 2
                    d = math.sqrt((sx-ox)**2 + (sy-oy)**2)
                    return d <= self.width/2 + obj.width/2
                else:
                    return self.collidingCircleWithPoly(self, obj)
            else:
                if type(obj.asset) is CircleAsset:
                    return self.collidingCircleWithPoly(obj, self)
                else:
                    return self.collidingPolyWithPoly(obj)
            '''
class sun(Sprite):
    asset = ImageAsset("images/sun.png")
    
    def __init__(self, position):
        super().__init__(sun.asset, position)
        self.mass = 30*1000
        self.fxcenter = 0.5
        self.fycenter = 0.5            

class SpaceShooter(App):
  
    def __init__(self):
        super().__init__()
        
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0,0))
        bg.scale=2

        self.gravity = Rocket((500,100))
        
        self.sun = sun((500,250))


    def step(self):
        for ship in self.getSpritesbyClass(Rocket):
            ship.step()
            

myapp = SpaceShooter()

myapp.run()