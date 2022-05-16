from frogHome import FrogHome
import pygame

class FrogHomes():
    def __init__(self):

        self.HomeList = []

    def addHome(self, home):
        self.HomeList.append(home)

    def drawHomes(self, screen):
        for i in range(len(self.HomeList)):
            self.HomeList[i].drawFrogHome(screen)

    def reset(self):
        for frogHome in self.HomeList:
            frogHome.isFrogHome = False

    def areHomesFull(self):
        homeStatus = []
        for frogHome in self.HomeList:
            homeStatus.append(frogHome.isFrogHome)
        if homeStatus.count(False) > 0 :
            return False
        else:
            return True
