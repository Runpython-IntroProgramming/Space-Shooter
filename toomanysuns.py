    def __init__(self, position):
         super().__init__(SpaceBlasts.blast, position)
         self.vx=1
         self.vy=1
         self.vr=0
         SpaceGame.listenKeyEvent("keydown", "p", self.Blast)
         self.blast=False
    def step(self):
        self.x += self.vx
        self.y += self.vy
    def Blast(self, event):
        self.blast=True
         
"""

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceField((0,0))
        SpaceField((500,0))
        SpaceShip((100,100))
        #SpaceShip((150,150))
        #SpaceShip((200,50))
        Sun((460, 200))
        Bounce((800, 300))
        Bounce((600, 200))
        Bounce((300, 400))
        Bounce((500, 100))
        Bounce((200, 500))
        Bounce((700, 150))
        Bounce((500, 300))
        Bounce((900, 500))
        Bounce((850, 400))
        Bounce((100, 100))
        Bounce((100, 150))
        
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for death in self.getSpritesbyClass(Bounce):
            death.step()

    
    
        


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
