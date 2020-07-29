import pygame
import random
import math
import winsound

pygame.init()




########################################
win = pygame.display.set_mode((1920, 1050), pygame.DOUBLEBUF, 32)








pygame.display.set_caption("QUARK")
# scoreboard
font = pygame.font.Font(pygame.font.get_default_font(), 28)
gameOverText = font.render('Game Over', True, (255, 0, 0))

inMenu = True

def startMenu():
    win.blit(pygame.image.load('startMenu.png'), (780, 550))
isPaused = False
def menu():

    win.blit(pygame.image.load('menu.png'), (780, 150))




#ART#
starX = 0
starY = 0
starPos = (starX, starY)
def star():


        win.blit(pygame.image.load('distantstar.png'), (starPos))



starPositions = [
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],
    [100, 100],

]

def playerImage():
    win.blit(pygame.image.load('player.png'), (x-98, y-100))
def foodImage():
    win.blit(pygame.image.load('food.png'), (foodPos[0] - 100, foodPos[1] -100))

def superfoodImage():
    win.blit(pygame.image.load('superfood.png'), (sfoodPos[0]-100, sfoodPos[1]-100))
def shieldAni():
    if (enemyRad % 2) == 0:
        win.blit(pygame.image.load('shield1.png'), (x - 100, y - 100))
    else:
        win.blit(pygame.image.load('shield2.png'), (x - 100, y - 100))
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('shield3.png'), (x - 100, y - 100))
def dmgImage():
    win.blit(pygame.image.load('dmg.png'), (x-100, y-100))

# food stuff
foodColor = (255, 255, 255)
foodX = random.randint(0, 970)
foodY = random.randint(0, 970)
foodPos = (foodX, foodY)
sfoodX = 0
sfoodY = 0
sfoodPos = (sfoodX, sfoodY)
#Energy
energyCount = 0

sfoodPositions = [
    [2000, 500],
    [500, 800]
]
# food movement
randX = random.randint(0, 1000)
randY = random.randint(0, 1000)
rand1X = random.randint(0, 1000)
rand1Y = random.randint(0, 1000)
rand2X = random.randint(0, 1000)
rand2Y = random.randint(0, 1000)
rand3X = random.randint(0, 1000)
rand3Y = random.randint(0, 1000)
rand4X = random.randint(0, 1000)
rand4Y = random.randint(0, 1000)


foodPositions = [

    [2200, 500],
    [2100, 300],
    [2150, 800],
    [400, 400],
    [600, 600]
]



def superfood():
    superfoodImage()




levelNumber = 1
foodCount = 0
#####BAD GUYS#####
badMax = 100 + round(foodCount / 1000)
badHealth = badMax






#########################

print(foodCount)
foodVel = 1
foodRange = 50
###########
hitRange = 120
x = 640
y = 500
width = 5
radius = 20
enemyRad = 50
buffer = range(-10, 10)
vel = 6
Rect = 50, 100
defColor = (0, 0, 255)
pColor = 0, 0, 255
playerHealth = 100
# ENEMY STUFF
enemyColor = 0, 255, 0
enemyX = 0
enemyY = 0
enemyPos = (enemyX, enemyY)
enemyVel = 100

enemyColor2 = 200, 0, 200
enemyColor3 = 0, 200, 200



enemyDotRad = 10
dotPosX = 500
dotPosY = 100
dotPos = (dotPosX, dotPosY)
dotDown = False
dotLeft = False
dotRight = False
dotUp = False


firingDown = False
firingUp = False
firingRight = False
firingLeft = False
firingDownRight = False
firingUpRight = False
firingDownLeft = False
firingUpLeft = False
invincible = False
isGameOver = False
run = True
beamHit = False
gameStill = False
goingRight = True



#### BAD GUYS ####

def enemyDot():
    pygame.draw.circle(win, (255, 0, 0), enemyDotPos, enemyDotRad, 0)
    win.blit(pygame.image.load('projectile.png'), (enemyDotPos[0] - 25, enemyDotPos[1] - 25))









######






def badGuy():
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('badGuy2.png'), (badPos[0] - 100, badPos[1] - 100))
    else:
        win.blit(pygame.image.load('badGuy1.png'), (badPos[0] - 100, badPos[1] - 100))








def enemyImage():


    win.blit(pygame.image.load('deathring.png'), (enemyPos[0] - 250, enemyPos[1] - 250))


def player():
    #pygame.draw.circle(win, pColor, (x, y,), radius, width)
    playerImage()




def food(foodX, foodY):
    pygame.draw.circle(win, foodColor, (foodPos[0], foodPos[1]), 13, 10)
    foodImage()




def controlPlayerPosition(x, y):
    if  keys[pygame.K_a] and x > vel:
        x -= vel

    if  keys[pygame.K_d] and x < 1980 - vel:
        x += vel

    if  keys[pygame.K_w] and y > vel:
        y -= vel

    if  keys[pygame.K_s] and y < 1000 - vel:
        y += vel
    return [x, y]
#player decoration


# Davila incircle code and Rekow changes
def isInCircle(enemyX, enemyY, playerX, playerY, radius):
    pDistance = math.sqrt(pow(enemyX - playerX, 2) + pow(enemyY - playerY, 2)) - enemyRad
    if (pDistance <= pow(radius, 2)): #and pDistance >= -1:
        return True
    return False

def isInRange(badPosX, badPosY, playerX, playerY, radius):
    dotDistance = math.sqrt(pow(badPosX - playerX, 2) + pow(badPosY -playerY, 2))
    if (dotDistance <= pow(radius, 2)):
        return True
    return False

def inSuperFoodRange(sfoodX, sfoodY, playerX, playerY, radius):
    sfoodDistance = math.sqrt(pow(sfoodX - playerX, 2) + pow(sfoodY -playerY, 2))
    if (sfoodDistance <= pow(radius, 2)):
        return True
    return False
def inFoodRange(foodX, foodY, playerX, playerY, radius):
    foodDistance = math.sqrt(pow(foodX - playerX, 2) + pow(foodY -playerY, 2))
    if (foodDistance <= pow(radius, 2)):
        return True
    return False

def forcebeam():

    if (enemyRad % 2) == 0:
        win.blit(pygame.image.load('beamcolor1.png'), (x + 30, y - 25))
    else:
        win.blit(pygame.image.load('beamcolor2.png'), (x + 30, y - 25))
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('beam1.png'), (x + 30 , y - 150))
    else:
        win.blit(pygame.image.load('beam2.png'), (x + 30, y - 25))

def forcebeamUpR():

    if (y % 2) == 0:
        win.blit(pygame.image.load('beamU1.png'), (x + 30, y - 500))
    else:
        win.blit(pygame.image.load('beamU2.png'), (x + 30, y - 500))


    if (ticks % 2) == 0:
       win.blit(pygame.image.load('beamU3.png'), (x + 30 , y - 500))
    else:
        win.blit(pygame.image.load('beamU4.png'), (x + 30, y - 500))

def forcebeamUp():

    if (y % 2) == 0:
        win.blit(pygame.image.load('beamUp1.png'), (x - 25, y - 1000))
    else:
        win.blit(pygame.image.load('beamUp2.png'), (x - 25, y - 1000))


    if (ticks % 2) == 0:
       win.blit(pygame.image.load('beamUp3.png'), (x - 25 , y - 1000))
    else:
        win.blit(pygame.image.load('beamUp4.png'), (x - 150, y - 1000))

def forcebeamDown():

    if (y % 2) == 0:
        win.blit(pygame.image.load('beamDown1.png'), (x - 25, y - 0))
    else:
        win.blit(pygame.image.load('beamDown2.png'), (x - 25, y - 0))


    if (ticks % 2) == 0:
       win.blit(pygame.image.load('beamDown3.png'), (x - 25 , y - 0))
    else:
        win.blit(pygame.image.load('beamDown4.png'), (x - 150, y - 0))




def forcebeamDownR():

    if (y % 2) == 0:
        win.blit(pygame.image.load('beamD1.png'), (x + 30, y + 0))
    else:
        win.blit(pygame.image.load('beamD2.png'), (x + 30, y + 0))


    if (ticks % 2) == 0:
       win.blit(pygame.image.load('beamD3.png'), (x + 30 , y + 0))
    else:
        win.blit(pygame.image.load('beamD4.png'), (x + 30, y + 0))

def forcebeamBack():

    if (enemyRad % 2) == 0:
        win.blit(pygame.image.load('beamBack1.png'), (x - 1030, y - 30))
    else:
        win.blit(pygame.image.load('beamBack2.png'), (x - 1030, y - 30))
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('beamBack3.png'), (x - 1030 , y - 30))
    else:
        win.blit(pygame.image.load('beamBack4.png'), (x - 1030, y - 150))

def forcebeamBackUp():

    if (enemyRad % 2) == 0:
        win.blit(pygame.image.load('beamBackUp1.png'), (x - 830, y - 500))
    else:
        win.blit(pygame.image.load('beamBackUp2.png'), (x - 830, y - 500))
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('beamBackUp3.png'), (x - 830 , y - 500))
    else:
        win.blit(pygame.image.load('beamBackUp4.png'), (x - 830, y - 500))
def forcebeamBackDown():

    if (enemyRad % 2) == 0:
        win.blit(pygame.image.load('beamBackDown.png'), (x - 830, y - 0))
    else:
        win.blit(pygame.image.load('beamBackDown2.png'), (x - 830, y - 0))
    if (ticks % 2) == 0:
        win.blit(pygame.image.load('beamBackDown3.png'), (x - 830 , y - 0))
    else:
        win.blit(pygame.image.load('beamBackDown4.png'), (x - 830, y - 0))
def playerHealthBar():


    healthBarSize = round(playerHealth * 3)
    pygame.draw.rect(win, (0, 0, 150), (0, 1050, 20, -healthBarSize), 0)

def energyBar():

    energyBarSize = round(energyCount * 5)
    pygame.draw.rect(win, (50, 200, 50), (16, 1050, 20, -energyBarSize), 0)



def enemyCircle():

    pygame.draw.circle(win, (20, 20, 20), enemyPos, enemyRad, 2)
    if enemyRad < 100:
        win.blit(pygame.image.load('fire1.png'), (enemyPos[0] - 300, enemyPos[1] - 300))
    if enemyRad > 100 and enemyRad < 150:
        win.blit(pygame.image.load('fire2.png'), (enemyPos[0] - 300, enemyPos[1] - 300))
    if enemyRad > 150 and enemyRad < 200:
        win.blit(pygame.image.load('fire3.png'), (enemyPos[0] - 300, enemyPos[1] - 300))

    if enemyRad > 200 and enemyRad < 250:
        win.blit(pygame.image.load('fire4.png'), (enemyPos[0] - 300, enemyPos[1] - 300))
    if enemyRad > 250:
        win.blit(pygame.image.load('fire5.png'), (enemyPos[0] - 300, enemyPos[1] - 300))


#random enemy

randomRad = random.randint(100, 300)

enemyPositions = [
    [500, 300],
    [2100, 600],
    [2500, 900],

    [2200, 0]
]
enemyDotPositions = [
    [0, 100],
    [1000, 200],
    [1900, 300],
    [2100, 500],
    [0, 0],
    [10, 10],
    [100, 1000]
]

j = 1200
badPosX = 0
badPosY = 0

badPos = (badPosX, badPosY)

badPositions = [
    [2000, 500],

]

while run:





    ticks = pygame.time.get_ticks()
    f = random.randint(1, 2)
    if f == 1:
        g = random.randint(-900, -800)
    else:
        g = random.randint(800, 900)

    win.fill((0, 0, 0))

    for starPos in starPositions:
        star()

        if starPos[0] > 0:
            starPos[0] -= 21
        else:
            starPos[0] = random.randint(2000, 4000)
            starPos[1] = random.randint(10, 990)

    for badPos in badPositions:
        badGuy()

        if gameStill == True:
            if badPos[0] >= x + random.randint(-50, 50):
                badPos[0] -= 1 + round(foodCount / 3000)
            if badPos[1] >= y + random.randint(-50, 50):
                badPos[1] -= 1 + round(foodCount / 3000)
            if badPos[0] <= x + random.randint(-50, 50):
                badPos[0] += 1 + round(foodCount / 3000)
            if badPos[1] <= y + random.randint(-50, 50):
                badPos[1] += 1 + round(foodCount / 3000)

        if goingRight == True:
            if badPos[0] > 0:
                badPos[0] -= 11
            else:
                badPos[0] = random.randint(2000, 2300)
                badPos[1] = random.randint(-1200, 1200)
            if badPos[1] > y - 400:
                badPos[1] -= 3
            else:
                badPos[1] += 3


        if x - badPos[0] < 50 and x - badPos[0] > -50 and (y <= badPos[1] and firingDown == True):
            print('BadGuy Hit')
            badHealth -= 20
            print(badHealth)
        if x - badPos[0] < 50 and x - badPos[0] > -50 and (y >= badPos[1] and firingUp == True):
            print('BadGuy Hit')
            badHealth -= 20
            print(badHealth)
        if y - badPos[1] < 50 and y - badPos[1] > -50 and (x >= badPos[0] and firingLeft == True):
            print('BadGuy Hit')
            badHealth -= 20
            print(badHealth)
        if y - badPos[1] < 50 and y - badPos[1] > -50 and (x <= badPos[0] and firingRight == True):
            print('BadGuy Hit')
            badHealth -= 20
            print(badHealth)
        try:
            r = (x - badPos[0]) / (y - badPos[1])
        except:
            ZeroDivisionError
        if r > 1.5 and r < 2.5 and x > badPos[0]:
            # print('beam')
            if firingUpLeft:
                # print('BEAM')
                beamHit = True
        else:
            beamHit = False

        if r < 2.5 and r > 1.5 and x < badPos[0] and firingDownRight == True:
            beamHit = True
        if r > -2.5 and r < -1.5 and y > badPos[1] and firingUpRight == True:
            beamHit = True
        if r > -2.5 and r < -1.5 and y < badPos[1] and firingDownLeft == True:
            beamHit = True

        if beamHit == True:
            print('beam')
            badHealth -= 20

        if badPos[0] > x -50 and y >= badPos[1] and badPos[1] > 0:
            if (ticks % 2) == 0:
                win.blit(pygame.image.load('enemyLaser.png'), (badPos[0] -10, badPos[1]))
            else:
                win.blit(pygame.image.load('enemyLaser1.png'), (badPos[0] - 10, badPos[1]))
            if badPos[0] > x -50 and badPos[0] < x +50:
                playerHealth -= 5

        if badPos[0] > x -50 and y <= badPos[1] and badPos[1] < 1000:
            if (ticks % 2) == 0:
                win.blit(pygame.image.load('enemyLaserUp.png'), (badPos[0] -10, badPos[1] - 1000))
            else:
                win.blit(pygame.image.load('enemyLaser1.png'), (badPos[0] - 10, badPos[1] - 1000))
            if badPos[0] > x -50 and badPos[0] < x +50:
                playerHealth -= 5


        if x >= badPos[0] and x <= badPos[0] + hitRange and y >= badPos[1] and y <= badPos[1] + hitRange:
            # print("in range")
            if invincible == True:
                badHealth -= 20
            else:
                playerHealth -= 1
        h = random.randint(1, 2)
        if badHealth <= 0:
            badHealth = badHealth + badMax
            badPos[0] = x + g
            if h == 1:
                g = random.randint(-900, -900)
            else:
                g = random.randint(800, 900)
            badPos[1] = y + g
            winsound.Beep(300, 50)
            foodCount += 33
            energyCount += 5
            playerHealth += 10

    if foodCount >= 100 and foodCount < 200:
        enemyColor = randColor

        badPositions = [
            [2000, -100],
            [2000, 1500],
            [2300, 600]
        ]



    if foodCount > 1000 and foodCount < 1100:

        badPositions = [
            [2400, 200],
            [2300, 100],
            [2200, 9],
            [2100, 2]
        ]


    if foodCount > 3000 and foodCount < 3100:
        enemyColor2 = 255, 0, 0
        badPositions = [
            [2200, 1000],
            [2200, -50],
            [2200, 800],
            [2200, 1200],
            [2200, -59]

        ]






    for foodPos in foodPositions:
        foodImage()
        if foodPos[0] > 0:
            foodPos[0] -= 20
        else:
            foodPos[0] = x + random.randint(2000, 2400)
        if (inFoodRange(foodPos[0], foodPos[1], x, y, 10)):
            print("you ate food")
            foodPos[0] = x + random.randint(2000, 2400)
            winsound.Beep(random.randint(330, 440), 50)


            foodCount += 33 - round(foodCount / 666)
            playerHealth += 3 - round(foodCount / 3333)
            energyCount += 3 - (foodCount / 10000)

    for sfoodPos in sfoodPositions:
        superfoodImage()
        if sfoodPos[0] > 0:
            sfoodPos[0] -= 5
        else:
            sfoodPos[0] = x + random.randint(2000, 2400)
        if (inSuperFoodRange(sfoodPos[0], sfoodPos[1], x, y, 10)):
            print("you ate super food")
            sfoodPos[0] = x + random.randint(2000, 2400)
            winsound.Beep(random.randint(330, 440), 50)


            foodCount += 99 - round(foodCount / 666)
            playerHealth += 9 - round(foodCount / 3333)
            energyCount += 12 - (foodCount / 10000)


        maxRad = 500 + round(foodCount / 100)





    for enemyPos in enemyPositions:

        enemyCircle()

        if enemyPos[0] > -50:
            enemyPos[0] -= 14 + round(foodCount / 1000)
        else:
            enemyPos[0] = random.randint(2000, 2500)

        if (isInCircle(enemyPos[0], enemyPos[1], x, y, 6)):
            playerHealth = playerHealth - 2
            dmgImage()

            pColor = (255, 0, 0)
            if (playerHealth <= 0):
                isGameOver = True

#####
    for enemyDotPos in enemyDotPositions:

        enemyDot()
        if enemyDotPos[0] > 0:
            enemyDotPos[0] -= 22  + round(foodCount / 1000)
        else:
            enemyDotPos[0] = random.randint(2000,2300)
            enemyDotPos[1] = random.randint(10, 1000)

        if (isInRange(enemyDotPos[0], enemyDotPos[1], x, y, 6)):


            if invincible == False:
                playerHealth = playerHealth - 3
                dmgImage()




    keys = pygame.key.get_pressed()
#### TELEPORT ####
    if keys[pygame.K_a] and keys[pygame.K_f] and energyCount > 1:
        energyCount -= 0.2
        if x < 100:
            x = 0
        if x > 100:
            x = x - 25
    if keys[pygame.K_d] and keys[pygame.K_f] and energyCount > 0.2:
        energyCount -= 0.2
        if x > 1900:
            x = 1900
        if x < 1900:
            x = x + 25
    if keys[pygame.K_s] and keys[pygame.K_f] and energyCount > 0.2:
        energyCount -= 0.2
        if y > 900:
            y = 1000
        if y < 900:
             y = y + 25

    if keys[pygame.K_w] and keys[pygame.K_f] and energyCount > 0.2:
        energyCount -= 0.2
        if y < 100:
            y = 0
        if y > 100:
            y = y - 25
        #### FORCE BEAM #######
    if keys[pygame.K_RIGHT] and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and energyCount > 0.05:
        forcebeam()
        energyCount -= 0.1
        firingRight = True
    else:
        firingRight = False
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]  and energyCount > 0.05:
        forcebeamUpR()
        energyCount -= 0.1
        firingUpRight = True
    else:
        firingUpright = False
    if keys[pygame.K_RIGHT] and keys [pygame.K_DOWN] and energyCount > 0.05:
        forcebeamDownR()
        energyCount -= 0.1
        firingDownRight = True
    else:
        firingDownRight = False
    if keys[pygame.K_UP] and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and energyCount > 0.05:
        forcebeamUp()
        energyCount -= 0.1
        firingUp = True
    else:
        firingUp = False
    if keys[pygame.K_DOWN] and not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and energyCount > 0.05:
        forcebeamDown()
       # energyCount -= 0.1
        firingDown = True
    else:
        firingDown = False
    if keys[pygame.K_LEFT] and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and energyCount > 0.05:
        forcebeamBack()
        energyCount -= 0.1
        firingLeft = True
    else:
        firingLeft = False
    if keys[pygame.K_LEFT] and keys[pygame.K_UP] and energyCount > 0.05:
        forcebeamBackUp()
        firingUpLeft = True
    else:
        firingUpLeft = False
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        forcebeamBackDown()
        firingDownLeft = True
    else:
        firingDownLeft = False

    maxHealth = 100 + round(foodCount / 1000)
    badDmg = maxHealth / (20 - foodCount / 1000)
    maxRad = round(foodCount / 100) + 300
    player()
    randColor = (random.randint(50, 255), random.randint(0, 255), random.randint(0, 255))
    enemyColor = randColor
    ranSound = random.randint(440, 880)
    if enemyRad >= maxRad:
        randX = random.randint(0, 1000)
        randY = random.randint(0, 1000)
        rand1X = random.randint(0, 1000)
        rand1Y = random.randint(0, 1000)
        rand2X = random.randint(0, 1000)
        rand2Y = random.randint(0, 1000)
        rand3X = random.randint(0, 1000)
        rand3Y = random.randint(0, 1000)
        rand4X = random.randint(0, 1000)
        rand4Y = random.randint(0, 1000)



 #######   #pause menu    #######
    keys = pygame.key.get_pressed()

    playerCoordinates = controlPlayerPosition(x, y)
    x = playerCoordinates[0]
    y = playerCoordinates[1]
    # davila enemy damage shit

    pygame.time.get_ticks()
    ticks = pygame.time.get_ticks()


   # print(pygame.time.get_ticks())
    pygame.time.delay(10)
    if (isGameOver == False):
        playerHealthText = font.render(str(round(playerHealth)), True, (255, 255, 255))

        playerScoreText = font.render(str(foodCount * 9), True, (0, 255, 0))
        playerEnergyText = font.render('ENERGY: ' + str(round(energyCount)), True, (0, 255, 255))
        levelText = font.render(str(levelNumber), True, (255, 255, 255))
        win.blit(levelText, (1800, 980))

        win.blit(playerScoreText, (1600, 980))
        #win.blit(playerEnergyText, (0, 100))
    else:
        pColor = (0, 0, 0)
        win.blit(playerHealthText, (-100, -100))
        win.blit(pygame.image.load('gameOver.png'), (600, 300))


    #max health

    if playerHealth > maxHealth:
        playerHealth = maxHealth
    keys = pygame.key.get_pressed()



######  ENERGY SHIELD



    if keys[pygame.K_SPACE] and energyCount > 0.05:
        shieldAni()

        playerHealth += foodCount / 10000
        enemyRad -= 3
        energyCount -= 0.05
        pColor = (0, 255, 0)

        if radius <= 100 and foodRange <= 120:
            radius += 1
            foodRange += 1
        else:
            radius = 100
            foodRange = 120

    else:
        radius = 20
        foodRange = 50
        pColor = defColor


    levelNumber = round(foodCount / 666)

    # consuming food

    if enemyRad < maxRad:
        enemyRad += 1 + round(foodCount / 10000)

    else:

        enemyRad -= maxRad - 30

    if enemyRad < 30:
        enemyRad = + (maxRad - 30)


    random.randint(-50, 50)


    if energyCount < 25:
        energyCount += 0.05





    energyBar()
    playerHealthBar()
    if playerHealth <= 0:
        win.blit(pygame.image.load('gameOver.png'), (600, 300))
        isGameOver = True
        pygame.time.delay(30)
    #win.blit(playerHealthText, (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_ESCAPE]:
        isPaused = True

    if inMenu == True:
        keys = pygame.key.get_pressed()
        startMenu()
        playerHealth += 100






        if keys[pygame.K_RETURN]:
            inMenu = False


    if isPaused == True:
        menu()
        pygame.time.delay(300)




        if keys[pygame.K_RETURN]:
            isPaused = False

    pygame.display.update()
pygame.quit()
