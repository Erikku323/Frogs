from car import Car
import random
class Road():

    def __init__(self):
        #self.carPos = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
        self.carList = []



    def addCar(self,car):
        self.carList.append(car)

    def getCar(self,car):
        return self.carList[car]

    def moveCars(self):
        for i in range(len(self.carList)):
            if self.carList[i].moveCar() == True:



                 self.carList[i].placeCar()

    def drawCars(self,screen):
        for i in range(len(self.carList)):
            self.carList[i].drawChar(screen=screen)



