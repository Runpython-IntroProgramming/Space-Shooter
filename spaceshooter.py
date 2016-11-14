"""
spaceshooter.py
Author: Wilson
Credit: Rimberg

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
asteroid_asset=ImageAsset("images/asteroid_for_program.png",)
asteroid1=Sprite(asteroid_asset, (300,300))
asteroid2=Sprite(asteroid_asset, (1120,300))
asteroid1.scale=.5
asteroid1.xmov=10
asteroid1.ymov=10
asteroid2.scale=.5
asteroid2.x2mov=-10
asteroid2.y2mov=-10

spaceship = Sprite(spaceship_asset, (740, 405))
spaceship.fxcenter = spaceship.fycenter = 0.5
# Movement
spaceship.dir = 3
spaceship.bob=3
spaceship.go = False
spaceship.ygo= False
spaceship.thrust = 0
spaceship.thrustframe = 1
def reverse(b):
    b.dir *= -1
    b.bob *= -1

def astryturn1(b):
    asteroid1.ymov *= -1

def astrxturn1(b):
    asteroid1.xmov *= -1

def astryturn2(b):
    asteroid1.x2mov *= -1

def astrxturn2(b):
    asteroid2.x2mov *= -1
    
    
def left(b):
    spaceship.dir=-4
def right(b):
    spaceship.dir=4
def up(b):
    spaceship.bob=-4
def down(b):
    spaceship.bob=4
    
def astr():
    asteroid1.x+=asteroid1.xmov
    asteroid1.y+=asteroid1.ymov
    if asteroid1.x + asteroid1.width > SCREEN_WIDTH:
        asteroid1.x -= asteroid1.xmov
        astrxturn1(asteroid1)
    if asteroid1.x < 0:
        asteroid1.x -= asteroid1.xmov
        astrxturn1(asteroid1)
    if asteroid1.y + asteroid1.height > SCREEN_HEIGHT:
        asteroid1.y -= asteroid1.ymov
        astryturn1(asteroid1)
    if asteroid1.y < 0:
        asteroid1.y-= asteroid1.ymov
        astryturn1(asteroid1)
    step()
    astr2()
    
    
def astr2():
    asteroid2.x+=asteroid2.x2mov
    asteroid2.y+=asteroid2.y2mov
    if asteroid2.x + asteroid2.width > SCREEN_WIDTH:
        asteroid2.x -= asteroid2.x2mov
        astrxturn1(asteroid1)
    if asteroid2.x < 0:
        asteroid2.x -= asteroid2.x2mov
        astrxturn2(asteroid1)
    if asteroid2.y + asteroid2.height > SCREEN_HEIGHT:
        asteroid2.y -= asteroid2.y2mov
        astryturn2(asteroid1)
    if asteroid2.y < 0:
        asteroid2.y-= asteroid2.y2mov
        astryturn2(asteroid1)
# Step
def step():
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > SCREEN_WIDTH:
            spaceship.x -= spaceship.dir
            spaceship.rotation=(3.141592653589793238462643383/2)
            reverse(spaceship)
        if spaceship.x < 60:
            spaceship.x -= spaceship.dir
            spaceship.rotation=((3*3.141592653589793238462643383)/2)
            reverse(spaceship)
        if spaceship.thrust == 1:
            spaceship.setImage(spaceship.thrustframe)
            spaceship.thrustframe += 1
            if spaceship.thrustframe == 4:
                spaceship.thrustframe = 1
        if spaceship.thrust == 0:
            spaceship.setImage(0)
    ystep()
    
def ystep():
    if spaceship.ygo:
        spaceship.y += spaceship.bob
        if spaceship.y +spaceship.height > SCREEN_HEIGHT+60:
            spaceship.y -= spaceship.bob
            spaceship.rotation=0
            reverse(spaceship)
        if spaceship.y < 60:
            spaceship.y -= spaceship.bob
            spaceship.rotation=3.141592653589793238462643383
            reverse(spaceship)
        if spaceship.thrust == 1:
            spaceship.setImage(spaceship.thrustframe)
            spaceship.thrustframe += 1
            if spaceship.thrustframe == 4:
                spaceship.thrustframe = 1
        if spaceship.thrust == 0:
            spaceship.setImage(0)

# Handle the space key
def spaceKey(event):
    spaceship.thrust = 0
    spaceship.thrustframe=1
    spaceship.setImage(0)
    if spaceship.go==True:
        spaceship.go=not spaceship.go
        if spaceship.ygo==True:
            spaceship.ygp=not spaceship.ygo
    if spaceship.ygo==True:
        spaceship.ygo=not spaceship.ygo

# Handle Keys
def leftKey(event):
    spaceship.go = True
    spaceship.ygo= False
    spaceship.thrust = 1
    spaceship.rotation=(3.141592653589793238462643383/2)
    left(spaceship)

def rightKey(event):
    spaceship.go = True
    spaceship.ygo=False
    spaceship.thrust = 1
    spaceship.rotation=(3.141592653589793238462643383*3)/2
    right(spaceship)
    
def upKey(event):
    spaceship.ygo = True
    spaceship.go=False
    spaceship.thrust = 1
    spaceship.rotation=0
    up(spaceship)
    
def downKey (event):
    spaceship.ygo = True
    spaceship.go = False
    spaceship.thrust = 1
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
myapp.run(astr)
