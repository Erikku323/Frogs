from character import Character
import pygame
class Frog(Character):

    def __init__(self,x,y):
        self.isFrogDead = False
        XLim = 800 # Window Size
        YLim = 870
        characterSprites = ["Frog_U.png", "Frog_UJump.png", "Frog_D.png", "Frog_DJump.png", "Frog_R.png","Frog_RJump.png", "Frog_L.png", "Frog_LJump.png","Frog_Dead.png"]
        self.Iskillable = True
        super(Frog, self).__init__(x=x,y=y,XLim=XLim,YLim=YLim,characterSprites=characterSprites,Xmin=0,Ymin=0,rectHSizeOffset=25,rectWSizeOffset=20,rectXPosOffset=8,rectYPosOffset=12)
        self.Speed = 2
        self.rect = self.characterSpriteAnimation[0].get_rect()
        self.isOnPlatform = False
        self.resetHold = False


    def killfrog(self):
        if self.Iskillable != False:
            self.isFrogDead = True

            self.characterSpriteAnimation[0] = pygame.image.load(self.characterSprites[8])
            self.characterSpriteAnimation[1] = pygame.image.load(self.characterSprites[8])


    def resetFrog(self):
        self.Xcor = self.Xorg
        self.Ycor = self.Yorg
        self.isFrogDead = False
        self.heading = 270
        self.move_Up()
        self.resetHold = False



