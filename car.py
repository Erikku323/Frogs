from character import Character
import random

class Car(Character):

    def __init__(self,LeftOrRight,y):
        characterSprites = ["CarL.png", "Frog_UJump.png", "Frog_D.png", "Frog_DJump.png", "CarR.png",
                            "CarR.png", "CarL.png", "CarL.png"]
        XLim = 900
        YLim = 700
        Xmin = -200
        Ymin = -100
        self.LeftOrRight = LeftOrRight


        super(Car, self).__init__(characterSprites=characterSprites,x=-500,y=y,XLim=XLim,YLim=YLim,Ymin=Ymin,Xmin=Xmin,rectHSizeOffset=25,rectWSizeOffset=10,rectYPosOffset=10,rectXPosOffset=5)
        self.placeCar()
        self.Speed = 4


    def placeCar(self):

        # ABS XLim is -100 , 800
        ### code needs to be reworked
        #inputs
        # #isLeft
        # pos
        # Xcor and Speed will be Randomized
        if self.LeftOrRight == 0:
            xpos = random.uniform(self.Xlim - 50, 800)
            self.Xcor = xpos
           # self.startPos = 0
        else:
            xpos = random.uniform(-200,self.Xmin + 50)
            self.Xcor = xpos

        self.Speed = random.uniform(4,8)
           # self.startPos = 1
        #pos = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
        #self.Ycor = random.randint(10, self.Ylim - 200)
        #self.Ycor = random.choice(pos)


    def moveCar(self):
        if self.LeftOrRight == 0:
            self.move_Left()
            if self.Xcor <= self.Xmin + 5:
                return True
        else:
            self.move_Right()
            if self.Xcor >= self.Xlim - 5:
                return True

        return False
