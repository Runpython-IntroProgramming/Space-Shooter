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
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))
ball_asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
spaceship = Sprite(ball_asset, (0, 0))
# Movement
spaceship.dir = 1
spaceship.go = False
spaceship.ygo= False
def reverse(b):
    b.dir *= -1
def left(b):
    spaceship.dir=-1
def right(b):
    spaceship.dir=1
def up(b):
    spaceship.dir=1
def down(b):
    spaceship.dir=-1
# Step
def step():
    if spaceship.go:
        spaceship.x += spaceship.dir
        if spaceship.x + spaceship.width > SCREEN_WIDTH or spaceship.x < 0:
            spaceship.x -= spaceship.dir
            reverse(spaceship)
def ystep():
    if spaceship.ygo:
        spaceship.y += spaceship.dir
        if spaceship.y +spaceship.height > SCREEN_HEIGHT or spaceship.y < 0:
            spaceship.y -= spaceship.dir
            reverse(spaceship)
# Handle the space key
def spaceKey(event):
    spaceship.go = spaceship.go

# Handle the "reverse" key
def reverseKey(event):
    spaceship.go = not spaceship.go
    reverse(spaceship)
    
def leftKey(event):
    spaceship.go = not spaceship.go
    left(spaceship)
    
def rightKey(event):
    spaceship.go = not spaceship.go
    right(spaceship)
    
def upKey(event):
    spaceship.ygo = not spaceship.ygo
    up(spaceship)
    
def downKey (event):
    spaceship.ygo = not spaceship.ygo
    down(spaceship)

# Handle the mouse click
def mouseClick(event):
    spaceship.x = event.x
    spaceship.y = event.y
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)
myapp.listenKeyEvent('keydown', 'a', leftKey)
myapp.listenKeyEvent('keydown', 'd', rightKey)
myapp.listenKeyEvent('keydown', 'w', upKey)
myapp.listenKeyEvent('keydown', 's', downKey)
myapp.run(ystep)
myapp.run(step)