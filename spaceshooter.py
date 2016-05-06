"""
spaceshooter.py
Author: Hagin
Credit: myself

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, Sprite, ImageAsset, Frame, Color, TextAsset, SoundAsset, Sound
from math import sqrt, sin, cos, radians, degrees, pi, atan
from random import randint
from time import sleep

SCREEN_WIDTH = 1000 #1200
SCREEN_HEIGHT = 600 #700
SCREEN_DIAG = sqrt(SCREEN_WIDTH**2+SCREEN_HEIGHT**2)


if SCREEN_WIDTH >= SCREEN_HEIGHT:
    LARGER_SIDE = SCREEN_WIDTH
    SMALLER_SIDE = SCREEN_HEIGHT
else:
    LARGER_SIDE = SCREEN_HEIGHT
    SMALLER_SIDE = SCREEN_WIDTH
    
white = Color (0xffffff, 1.0) 

velocityOfX = lambda rotation, speed: -1*speed*sin(rotation)
velocityOfY = lambda rotation, speed: -1*speed*cos(rotation)

def Destroy(Dclass):
    while len(SpaceGame.getSpritesbyClass(Dclass)) > 0:
        for foo in SpaceGame.getSpritesbyClass(Dclass):
            foo.destroy()
def Opponent(EnemyCount):
    for foo in SpaceGame.getSpritesbyClass(ScoreMain):
        score = foo.score
    for bar in [1/(EnemyCount-score)*bar*2*pi for foo in list(range(0,(EmenyCount-score)))]:
        Enemy(SMALLER_SIDE*-0.4)*sin(foo)+SCREEN_WIDTH/2,
        (SMALLER_SIDE*-0.4)*cos(x)+SCORE
