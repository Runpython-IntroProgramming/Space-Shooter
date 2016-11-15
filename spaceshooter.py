def __init__(self, position):
          super().__init__(astroid.asset, position)    
 -        self.avx = 0
 +        self.avx = 1
          self.avy = 0
 -        self.avr = 1
 +        self.avr = 0.05
          self.random1 = round((random.random())*100)
 -        self.ranom2 = round((random.random())*10)
 +        self.random2 = round((random.random())*10)
          number = 0
 +        self.fxcenter = self.fycenter = 0.5
 +        
      def step(self):
 -        if number >= random1:
 -            self.avx = random1
 -            number = 0
 -        number += 12
 +       # if number <= random1:
 +       #     self.avx = random2
 +       #     number = 0
 +      #  number += 11
 +
          
 +        self.rotation += self.avr
 +        self.x += self.avx
 +        self.y += self.avy
  class SpaceShip(Sprite):
      """
      Animated space ship
 @@ -153,15 +159,14 @@ def __init__(self, width, height):
          super().__init__(width, height)
          Stars((0,0))
          SpaceShip((500,500))
 -        astroid((0,0))
 +        astroid((200,150))
  
  
      def step(self):
          for ship in self.getSpritesbyClass(SpaceShip):
              ship.step()
          for Bstroid in self.getSpritesbyClass(astroid):
              Bstroid.step()
 -
 -
 +            
  myapp = SpaceGame(1900, 950)
  myapp.run() 
  