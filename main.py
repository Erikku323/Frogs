import pygame
import time
import math

from frog import Frog
from car import Car
from road import Road
from lillypad import LillyPad
from platforms import Platforms
from turtlePlatform import Turtle
from frogHome import FrogHome
from frogHomes import FrogHomes

def genPlatforms(offset,startX,y,speed,platform,platforms,num):
    for i in range(1, num+1):
        x = startX + (offset * i)
        platforms.addPlatform(platform(x=x, y=y, speed=speed))

def genTurtlePlatform(offset,startX,y,speed,turtles,num,moveCount):
    for i in range(1, num+1):
        x = startX + (offset * i)
        turtles.addPlatform(Turtle(x=x, y=y, speed=speed,moveCount=moveCount))

def genFrogHomes(startx,frogHomes,num,offset):
    x = startx
    for i in range(1,num +1):
        frogHomes.addHome(FrogHome(x=x,y=64))
        x = x + offset

def displayScore(score_Value,screen,highscore_Value):
    if  highscore_Value < score_Value:
        highscore = score_Value
    x = 10
    y = 10
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score : " + str(score_Value),True,(255,255,255))
    screen.blit(score, (x, y))
    x = 300
    highscore = font.render("HighScore : " + str(highscore_Value),True,(255,255,255))
    screen.blit(highscore, (x, y))

def drawLives(lives, screen):
    life = pygame.image.load("Frog_D.png")
    x =620
    offset = 0
    for i in range(0,lives):
        screen.blit(life,(x + offset,0))
        offset =  offset + 50

score_Value = 0
highScore_Value = 0
lives = 3
gameOver = False


windowX = 800
windowY = 865
r = 255
g = 255
b = 255


background = pygame.image.load('Road.png')

# Needs to do this first
pygame.init()

icon = "Frog_U.png"
#Setup the Screen
screen = pygame.display.set_mode((windowX,windowY))
pygame.display.set_caption("Frogs")
frogIcon = pygame.image.load(icon)
pygame.display.set_icon(frogIcon)





####
#630
player = Frog(x=(windowX / 2 - 50) ,y=windowY - 50)
road = Road()
leftcarPos =[185,255]

road.addCar(Car(LeftOrRight=0,y=750))
road.addCar(Car(LeftOrRight=0,y=680))

road.addCar(Car(LeftOrRight=1,y=500))
road.addCar(Car(LeftOrRight=1,y=565))

platforms = Platforms()
turtles = Platforms()





####################################
#Add Water Platforms
#####################################
speed = 0.5
y = 405
genPlatforms(offset=60,startX=0,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=250,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=500,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=750,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)

speed = 0.5
y= 330
genTurtlePlatform(offset=70,startX=0,y=y,speed=speed,turtles=turtles,num=3,moveCount = 0)
genTurtlePlatform(offset=70,startX=250,y=y,speed=speed,turtles=turtles,num=3,moveCount = 30)
genTurtlePlatform(offset=70,startX=500,y=y,speed=speed,turtles=turtles,num=3,moveCount = 0)

speed = 0.5
y = 280
genPlatforms(offset=60,startX=100,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=350,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=600,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=850,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
speed = 0.5
y= 205
#genTurtlePlatform(offset=150,startX=0,y=y,speed=speed,turtles=turtles,num=6,moveCount = 50)
turtles.addPlatform(Turtle(x=0, y=y, speed=speed, moveCount=0))
turtles.addPlatform(Turtle(x=100, y=y, speed=speed, moveCount=50))
turtles.addPlatform(Turtle(x=200, y=y, speed=speed, moveCount=0))
turtles.addPlatform(Turtle(x=300, y=y, speed=speed, moveCount=50))
turtles.addPlatform(Turtle(x=400, y=y, speed=speed, moveCount=0))
turtles.addPlatform(Turtle(x=500, y=y, speed=speed, moveCount=50))
turtles.addPlatform(Turtle(x=600, y=y, speed=speed, moveCount=0))
turtles.addPlatform(Turtle(x=700, y=y, speed=speed, moveCount=50))
turtles.addPlatform(Turtle(x=800, y=y, speed=speed, moveCount=0))


speed = 0.5
y = 150
genPlatforms(offset=60,startX=100,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=350,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=600,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)
genPlatforms(offset=60,startX=850,y=y,speed=speed,platform=LillyPad,platforms=platforms,num=3)

##################
#Add Frog Homes
##################
frogHomes = FrogHomes()
genFrogHomes(offset=200,startx=70,frogHomes=frogHomes,num=4)




resetCount = 0 #Count for frog animations



#####################################################

def getDist(obj1,obj2,):
    x1 = obj1.Xcor
    y1 = obj1.Ycor
    x2 = obj2.Xcor
    y2 = obj2.Ycor

    dist = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
    return dist

def getDistCenter(obj1,obj2,):
    x1 = obj1.Xcor
    y1 = obj1.Ycor
    x2 = obj2.Xmid
    y2 = obj2.Ymid

    dist = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))
    return dist

def reset():
    player.resetFrog()

i = 0
#Main Game Loop
gameQuit = False
img = 0
while gameQuit == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit = True
    # Keyboard inputs
        if lives < 0:
            score_Value = 0

            frogHomes.reset()

        if player.isFrogDead == False and  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_Up()
                elif event.key == pygame.K_DOWN:
                    player.move_Down()
                elif event.key == pygame.K_LEFT:
                    player.move_Left()
                elif event.key == pygame.K_RIGHT:
                    player.move_Right()
        elif player.isFrogDead == True and resetCount < 200:
                resetCount = resetCount + 1
        elif resetCount >= 200:
            resetCount = 0
            reset()
        else:
            player.stopped()


        road.moveCars()
        #
        platforms.movePlatforms()

        turtles.movePlatforms()

        screen.fill((r, g, b))
        screen.blit(background,(0,0))
        displayScore(score_Value=score_Value,screen=screen,highscore_Value=highScore_Value)
        drawLives(lives,screen)

        for platform in platforms.platformList:
            platform.drawPlatform(screen=screen)

        road.drawCars(screen=screen)

        #######################################`
        ### Draw Turtles
        ###################################
        for turtle in turtles.platformList:

            if turtle.isTurtleUnderwater != True:


                #Check turtle Status and correct the animation
                if turtle.isTurtleSurfacing == False and turtle.isTurtleDiving == False:
                    turtle.setNextSprite()
                elif turtle.isTurtleSurfacing == True:
                    turtle.setNextSurfacingSprite()
                elif turtle.isTurtleDiving == True:
                    turtle.setNextDiveSprite()
                turtle.drawPlatform(screen)

            turtle.setHitbox()
            turtle.countMove()

# Draw Frog Homes
        frogHomes.drawHomes(screen)




# Draw Player
        player.drawChar(screen=screen)

      #Is Player in Water Area?
        if player.Ycor < 430:
            isinWaterArea = True

        else: isinWaterArea = False
###########################################
##### Check for collisions
###########################################
        frogRect = player.get_HitBox(screen)

        #########################################
        # Does Frog hit home
        #####################################

        for frogHome in frogHomes.HomeList:
            frogHomeRect = frogHome.get_HitBox(screen)
            if frogRect.colliderect(frogHomeRect) and frogHome.isFrogHome == False:
                frogHome.isFrogHome = True
                frogHome.drawFrogHome(screen)
                score_Value = score_Value + 50
                player.resetFrog()

        if frogHomes.areHomesFull() == True:
            frogHomes.reset()







        platformRect = turtle.get_HitBox(screen)
        if frogRect.colliderect(platformRect):
            pass
          #pygame.draw.rect(screen, (255, 255, 255), frogRect, 4)

        for car in road.carList:
            carRect = car.get_HitBox(screen)

            if frogRect.colliderect(carRect):
               player.killfrog()


        for platform in platforms.platformList:
            platformRect = platform.get_HitBox(screen)
            if frogRect.colliderect(platformRect):
               # pygame.draw.rect(screen, (255, 255, 255), frogRect, 4)
               # pygame.draw.rect(screen,(0,0,255),platformRect,4)
                player.isOnPlatform = True
                if platform.LeftOrRight == 0:
                    player.Xcor -= platform.speed
                else:
                    player.Xcor += platform.speed


        for turtle in turtles.platformList:

            turtleRect = turtle.get_HitBox(screen)
            if frogRect.colliderect(turtleRect) and turtle.isTurtleUnderwater == False:
               # pygame.draw.rect(screen, (0, 0, 255), frogRect, 4)
              #  pygame.draw.rect(screen, (0, 0, 255), turtleRect, 4)
                player.isOnPlatform = True

                if turtle.LeftOrRight == 0:
                    player.Xcor -= turtle.speed
                else:
                    player.Xcor += turtle.speed
                    #pygame.draw.rect(screen, (255, 0, 0), frogRect, 4)
        if player.isOnPlatform == False and isinWaterArea == True:
            player.killfrog()


        #################################



        if player.isFrogDead == True and player.resetHold == False:
            lives = lives - 1
            player.resetHold = True





            
###########################################################################
        #time.sleep(0.1)
        if img == 0:
            img = 1
        else:
            img = 0
            i = i + 1


            player.isOnPlatform = False
        pygame.display.update()

