from platform import Platform
import pygame

class Turtle(Platform):
    def __init__(self,x,y,speed,moveCount):
        super(Turtle, self).__init__(x=x,y=y,speed=speed,rectYPosOffset=16,rectXPosOffset=16,rectHSizeOffset=30,rectWSizeOffset=30,sprite= pygame.image.load("Turtle1.png"),LeftOrRight=1)
        self.scalePlatform(0.9)



        self.turtleSprites =["Turtle1.png","Turtle2.png","Turtle3.png","Turtle4.png","Turtle5.png","Turtle6.png","Turtle7.png","Turtle8.png"]


        self.spriteIndex = 0
        self.frameCount = 0
        self.moveCount = 0
        self.isTurtleDiving = False
        self.isTurtleSurfacing = True
        self.isTurtleUnderwater = False

        self.moveCount = moveCount
        self.countMove()

    def setHitbox(self):
        if self.spriteIndex < 5:
            self.rectXPosOffset = 10
            self.rectYPosOffset = 17
            self.rectHSizeOffset = 30
            self.rectWSizeOffset = 25
        elif self.spriteIndex == 5:
            self.rectXPosOffset = 15
            self.rectYPosOffset = 25
            self.rectHSizeOffset = 45
            self.rectWSizeOffset = 30
        elif self.spriteIndex == 6:
            self.rectXPosOffset = 25
            self.rectYPosOffset = 32
            self.rectHSizeOffset = 60
            self.rectWSizeOffset = 45
        elif self.spriteIndex == 7:
            self.rectXPosOffset = 32
            self.rectYPosOffset = 35
            self.rectHSizeOffset = 65
            self.rectWSizeOffset = 58



    def setNextSurfacingSprite(self):
        startIndex = 7
        stopIndex = 5
        delay = 40

        if self.frameCount > delay:
            self.frameCount = 0
            if self.spriteIndex <= stopIndex:
                self.spriteIndex = startIndex
            else:
                self.spriteIndex = self.spriteIndex - 1

            self.sprite = pygame.image.load(self.turtleSprites[self.spriteIndex])
        else:
            self.frameCount = self.frameCount + 0.5

    def setNextDiveSprite(self):


        startIndex = 5
        stopIndex = len(self.turtleSprites) - 1
        delay = 40
        if self.spriteIndex < startIndex:
            self.spriteIndex = startIndex

        if self.frameCount > delay:
            self.frameCount = 0
            if self.spriteIndex >= stopIndex:

                self.spriteIndex = startIndex
            else:
                self.spriteIndex = self.spriteIndex + 1

            self.sprite = pygame.image.load(self.turtleSprites[self.spriteIndex])
        else:
            self.frameCount = self.frameCount + 0.5

    def setNextSprite(self):

        # Sets animation cycles speed and which animation Diving or swimming
        startIndex = 0
        stopIndex = 4
        delay = 5

        if self.spriteIndex < startIndex :
            self.spriteIndex = startIndex

        if self.frameCount > delay:
            self.frameCount = 0
            if self.spriteIndex >= stopIndex:

                    self.spriteIndex = startIndex
            else:
                self.spriteIndex = self.spriteIndex +1

            self.sprite = pygame.image.load(self.turtleSprites[self.spriteIndex])
        else:
            self.frameCount = self.frameCount + 0.5


        #################################################


    def countMove(self):





        if self.moveCount < 30:
            # Turtle swimming normal
            self.isTurtleDiving = False
            self.isTurtleSurfacing = False
            self.isTurtleUnderwater = False
        elif self.moveCount > 30 and self.moveCount < 50:
            #Diving
            self.isTurtleDiving = True
        elif self.moveCount > 50 and self.moveCount < 90:
            #Underwater
            self.isTurtleUnderwater = True
            self.isTurtleDiving = False
        elif self.moveCount > 90  and self.moveCount < 110:
            #Turtle Surfacing
            self.isTurtleSurfacing = True
            self.isTurtleUnderwater = False
        elif self.moveCount > 110 and self.moveCount < 150:
            #normal
            self.isTurtleSurfacing = False
            self.isTurtleDiving = False
            self.isTurtleUnderwater = False

            self.moveCount = 0
        self.moveCount =  self.moveCount + 0.1

