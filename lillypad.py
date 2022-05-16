import pygame
from platform import Platform

class LillyPad(Platform):

    def __init__(self,x,y,speed):

        super(LillyPad, self).__init__(x=x,y=y,speed=speed,rectXPosOffset=16,rectYPosOffset=16,rectHSizeOffset=30,rectWSizeOffset=30,sprite= pygame.image.load("lilypad_teal.png"),LeftOrRight=0)
        self.scalePlatform(0.5)