import pygame


class FrogHome():

    def __init__(self,x,y):
        self.Xcor = x
        self.Ycor = y
        self.sprites = [pygame.image.load("FrogHome.png"),pygame.image.load("Frog_D.png")]
        self.rect = self.sprites[0].get_rect()
        self.isFrogHome = False


    def drawFrogHome(self, screen):

        if self.isFrogHome == True:
            screen.blit(self.sprites[0], (self.Xcor, self.Ycor))
            screen.blit(self.sprites[1], (self.Xcor + 12, self.Ycor + 13 ))
        else:
            screen.blit(self.sprites[0], (self.Xcor, self.Ycor))

    def get_HitBox(self, screen):

        self.rect = self.sprites[0].get_rect()
        self.rect.x = self.Xcor + 10
        self.rect.y = self.Ycor + 20
        self.rect.width =self.rect.width - 20
        self.rect.height = self.rect.height - 20
      #  pygame.draw.rect(screen, (255, 0, 0), self.rect, 4)
        return self.rect

