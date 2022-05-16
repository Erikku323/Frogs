class Platforms():

    def __init__(self):

        self.platformList = []

    def addPlatform(self, platform):
        self.platformList.append(platform)

    def movePlatforms(self):
        for i in range(len(self.platformList)):
            self.platformList[i].move_Platform()

    def drawPlatforms(self, screen):
        for i in range(len(self.platformList)):
            self.platformList[i].drawPlatform(screen)





