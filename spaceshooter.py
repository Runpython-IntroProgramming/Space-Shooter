"""
spaceshooter.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound, Frame
SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 810

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
space_asset= ImageAsset("images/starfield.jpg",)
space_asset2=ImageAsset("images/starfield.jpg",)
space=Sprite(space_asset, (0,0))
space2=Sprite(space_asset, (512,0))
space3=Sprite(space_asset,(1024,0))
space4=Sprite(space_asset, (0,512))
space5=Sprite(space_asset, (512,512))
space6=Sprite(space_asset, (1024, 512))
spaceship_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

spaceship = Sprite(spaceship_asset, (0, 0))
spaceship.fxcenter = spaceship.fycenter = 0.5
# Movement
spaceship.dir = 1
spaceship.bob=1
spaceship.go = False
spaceship.ygo= False
def reverse(b):
    b.dir *= -1
def left(b):
    spaceship.dir=-1
def right(b):
    spaceship.dir=1
def up(b):
    spaceship.bob=-1
def down(b):
    spaceship.bob=1
    


# Step
def step():
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > SCREEN_WIDTH or spaceship.x < 0:
            spaceship.x -= spaceship.dir
            reverse(spaceship)
    ystep()
    
def ystep():
    if spaceship.ygo:
        spaceship.y += spaceship.bob
        if spaceship.y +spaceship.height > SCREEN_HEIGHT or spaceship.y < 0:
            spaceship.y -= spaceship.bob
            reverse(spaceship)
# Handle the space key
def spaceKey(event):
    if spaceship.go==True:
        spaceship.go=not spaceship.go
        if spaceship.ygo==True:
            spaceship.ygp=not spaceship.ygo
    if spaceship.ygo==True:
        spaceship.ygo=not spaceship.ygo

# Handle Keys
def leftKey(event):
    spaceship.go = True
    if spaceship.up==True:
        spaceship.rotation=3.141592653589793238462643383/4
    else: 
        if  spaceship.up==False:
            spaceship.rotation=(3.141592653589793238462643383*3)/4
        else:
            spaceship.rotation=3.141592653589793238462643383/2
    left(spaceship)
def rightKey(event):
    spaceship.go = True
    spaceship.rotation=(3.141592653589793238462643383*3)/2
    right(spaceship)
    
def upKey(event):
    spaceship.ygo = True
    spaceship.up=True
    spaceship.rotation=0
    up(spaceship)
    
def downKey (event):
    spaceship.ygo = True
    spaceship.up=False
    spaceship.rotation=3.141592653589793238462643383
    down(spaceship)



# Handle the mouse click
def mouseClick(event):
    spaceship.x = event.x
    spaceship.y = event.y
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenMouseEvent('click', mouseClick)
myapp.listenKeyEvent('keydown', 'a', leftKey)
myapp.listenKeyEvent('keydown', 'd', rightKey)
myapp.listenKeyEvent('keydown', 'w', upKey)
myapp.listenKeyEvent('keydown', 's', downKey)
#myapp.run(ystep)
myapp.run(step)
