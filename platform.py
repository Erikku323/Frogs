import pygame

class Platform():

    def __init__(self,x,y,speed,sprite,rectXPosOffset,rectYPosOffset,rectWSizeOffset,rectHSizeOffset,LeftOrRight):
        self.Xcor = x
        self.Ycor = y
        self.speed = speed
        self.sprite = sprite
        self.Xmin = -150
        self.XLim = 950
        self.LeftOrRight = LeftOrRight
        self.rectXPosOffset = rectXPosOffset
        self.rectYPosOffset = rectYPosOffset
        self.rectWSizeOffset =rectWSizeOffset
        self.rectHSizeOffset = rectHSizeOffset



    def move_Right(self):

        if (self.Xcor + self.Speed) >= self.Xlim:
            self.Xcor = self.Xlim - 0.1
            #reset

        else:
            self.Xcor += self.Speed

    def get_Pos(self):
        return [self.Xcor,self.Ycor]

    def drawPlatform(self, screen):
        screen.blit(self.sprite, (self.Xcor, self.Ycor))

    def scalePlatform(self,scale):
        width = self.sprite.get_width()
        length = self.sprite.get_height()

        self.sprite = pygame.transform.scale(self.sprite,(width * scale, length * scale))

    def get_HitBox(self,screen):

        self.rect = self.sprite.get_rect()
        self.rect.x = self.Xcor + self.rectXPosOffset
        self.rect.y = self.Ycor + self.rectYPosOffset
        self.rect.width = self.rect.width - self.rectWSizeOffset
        self.rect.height = self.rect.height - self.rectHSizeOffset
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)
        return self.rect

    def move_Platform(self):
        if self.LeftOrRight == 0:
            if (self.Xcor - self.speed) >= self.Xmin:
                self.Xcor -= self.speed

            else:
                self.Xcor = self.XLim - 100

        else:
            if (self.Xcor + self.speed) >= self.XLim:
                self.Xcor = self.Xmin + 10
                # reset

            else:
                self.Xcor += self.speed

