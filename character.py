import pygame

class Character():

    def __init__(self,x,y,XLim,YLim,Xmin,Ymin,characterSprites,rectXPosOffset,rectYPosOffset,rectWSizeOffset,rectHSizeOffset):

        super(Character, self).__init__()
        # setup Frog
        self.characterSprites = characterSprites
        #[charUp0,charUp1,charDown0,charDown1,charRight0,charRight1,charLeft0,charLeft1]
        self.characterSprite = pygame.image.load(self.characterSprites[0])
        self.Xcor = x
        self.Ycor = y
        self.Speed = 0.08
        self.Xlim = XLim -50
        self.Ylim = YLim - 50
        self.Ymin = Ymin
        self.Xmin = Xmin
        self.Yorg = y # origin points
        self.Xorg = x
        self.rectXPosOffset = rectXPosOffset
        self.rectYPosOffset = rectYPosOffset
        self.rectHSizeOffset = rectHSizeOffset
        self.rectWSizeOffset = rectWSizeOffset




        self.heading = 90
        self.characterSprite1 = pygame.image.load(self.characterSprites[1])
        self.characterSpriteAnimation = [self.characterSprite,self.characterSprite1]
        self.spriteIndex = 0
        self.frameCount = 0


    def drawChar(self,screen):
        screen.blit(self.characterSpriteAnimation[self.spriteIndex], (self.Xcor, self.Ycor))

    def get_Pos(self):
        return [self.Xcor, self.Ycor]

    def set_Pos(self, x, y):
        self.Xcor = x
        self.Ycor = y

    def move_Up(self):
        if self.heading != 90:
            self.characterSprite = pygame.image.load(self.characterSprites[0])
            self.characterSprite1 = pygame.image.load(self.characterSprites[1])
            self.characterSpriteAnimation = [self.characterSprite, self.characterSprite1]
            self.heading = 90
        elif (self.Ycor - self.Speed) >= self.Ymin :
            self.Ycor -=self.Speed
            self.countFrames()
        else:
            self.Ycor = self.Ymin - 0.1
            self.stopped()

    def move_Down(self):
        if self.heading != 270:
            self.characterSprite = pygame.image.load(self.characterSprites[2])
            self.characterSprite1 = pygame.image.load(self.characterSprites[3])
            self.heading = 270
            self.characterSpriteAnimation =[self.characterSprite,self.characterSprite1]
        elif (self.Ycor + self.Speed) >= self.Ylim:
            pass
            self.Ycor = self.Ylim - 0.1
            self.stopped()
        else:
            self.Ycor += self.Speed
            self.countFrames()

    def move_Left(self):
        if self.heading != 180:
            self.heading = 180
            self.characterSprite = pygame.image.load(self.characterSprites[6])
            self.characterSprite1 = pygame.image.load(self.characterSprites[7])
            self.characterSpriteAnimation = [self.characterSprite, self.characterSprite1]


        elif (self.Xcor - self.Speed) >= self.Xmin :
            self.Xcor -= self.Speed
            self.countFrames()
        else:
            self.Xcor = self.Xmin - 0.1
            self.stopped()

    def move_Right(self):
        if self.heading != 0:

            self.heading = 0
            self.characterSprite = pygame.image.load(self.characterSprites[4])
            self.characterSprite1 = pygame.image.load(self.characterSprites[5])
            self.characterSpriteAnimation = [self.characterSprite, self.characterSprite1]


        elif (self.Xcor + self.Speed) >= self.Xlim:
            self.Xcor = self.Xlim - 0.1
            self.stopped()


        else:
            self.Xcor += self.Speed
            self.countFrames()

    def countFrames(self):
        frameSlow = 15
        if self.frameCount >= frameSlow:
            if self.spriteIndex >= 1:
                self.frameCount = 0
                self.spriteIndex = 0
            else:
                self.frameCount = 0
                self.spriteIndex = self.spriteIndex + 1
        else:
            self.frameCount = self.frameCount + 1

    def stopped(self):

        self.spriteIndex = 0
        self.frameCount = 0
        # if self.heading == 90:
        #     self.characterSprite = pygame.image.load(self.characterSprites[0])
        # elif self.heading == 0:
        #     self.characterSprite = pygame.image.load(self.characterSprites[4])
        # elif self.heading == 180:
        #     self.characterSprite = pygame.image.load(self.characterSprites[6])
        # elif self.heading == 270:
        #     self.characterSprite = pygame.image.load(self.characterSprites[2])

    def get_HitBox(self,screen):
        self.rect = self.characterSpriteAnimation[self.spriteIndex].get_rect()
        self.rect.x = self.Xcor + self.rectXPosOffset
        self.rect.y = self.Ycor + self.rectYPosOffset
        self.rect.width = self.rect.width - self.rectWSizeOffset
        self.rect.height = self.rect.height - self.rectHSizeOffset
       # pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)
        return self.rect

