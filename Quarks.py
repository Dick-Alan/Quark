import pygame
import random
import math
import winsound

pygame.init()

win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("QUARK")
# scoreboard
font = pygame.font.Font(pygame.font.get_default_font(), 36)
gameOverText = font.render('Game Over', True, (255, 0, 0))

# food stuff
foodColor = (0, 0, 255)
foodX = random.randint(0, 970)
foodY = random.randint(0, 970)
sfoodX = random.randint(0, 970)
sfoodY = random.randint(0, 970)


# food movement


def food(foodX, foodY):
    pygame.draw.circle(win, foodColor, (foodX, foodY), 13, 10)


def superfood(sfoodX, sfoodY):
    pygame.draw.circle(win, (200, 0, 100), (sfoodX, sfoodY), 13, 10)


foodCount = 0

print(foodCount)
foodVel = 1
foodRange = 50
###########
x = 500
y = 750
width = 5
radius = 20
buffer = range(-10, 10)
vel = 3
Rect = 50, 100
defColor = (0, 0, 255)
pColor = 0, 0, 255
playerHealth = 100
# ENEMY STUFF
enemyColor = 0, 255, 0
enemyX = 500
enemyY = 500
enemyPos = (enemyX, enemyY)
enemyVel = 100
enemyRad = 2
enemyColor2 = 200, 0, 200
enemyColor3 = 0, 200, 200
isGameOver = False
run = True


def controlPlayerPosition(x, y):
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1000 - vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < 1000 - vel:
        y += vel
    return [x, y]


# Davila incircle code and Rekow changes
def isInCircle(enemyX, enemyY, playerX, playerY, radius):
    pDistance = math.sqrt(pow(enemyX - playerX, 2) + pow(enemyY - playerY, 2)) - enemyRad
    if (pDistance <= pow(radius, 2)) and pDistance >= -1:
        return True
    return False


enemyPositions = [
    [500, 500],
    #    [100, 100],
    #    [900, 900],
    #    [100, 900],
    #    [900, 100],
    #    [100, 500],
    #    [500, 100],
    #    [900, 500],
    #    [500, 900],
    #    [300, 300],
    #    [700, 700],
    #    [300, 700],
    #    [700, 300],
    #    [158, 300],
    #    [600, 257]
]
while run:

    win.fill((0, 0, 0))

    pygame.draw.circle(win, pColor, (x, y,), radius, width)

    pygame.time.delay(10)
    if (isGameOver == False):
        playerHealthText = font.render('HEALTH: ' + str(playerHealth), True, (0, 100, 200))
        playerScoreText = font.render('SCORE: ' + str(foodCount), True, (0, 255, 0))
        win.blit(playerHealthText, (0, 0))
        win.blit(playerScoreText, (0, 50))
    else:
        pColor = (0, 0, 0)
        win.blit(playerHealthText, (-100, -100))
        win.blit(gameOverText, (700, 500))

    # enemy radius control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] or keys[pygame.K_UP]:

        pColor = (0, 255, 0)
        enemyRad -= 2
    else:
        pColor = defColor
    if enemyRad < 500:
        enemyRad += 1

    else:
        enemyRad -= 477

    if enemyRad < 13:
        enemyRad = + 477
    # spawning in food
    food(foodX, foodY)
    superfood(sfoodX, sfoodY)

    # moving the food
    if foodX >= 400 and foodX <= 950:
        foodX += random.randint(-2, 1)
    if foodY >= 400 and foodY <= 950:
        foodY += random.randint(-2, 1)
    if foodX <= 400 and foodX >= 50:
        foodX -= random.randint(-2, 1)
    if foodY <= 400 and foodY >= 50:
        foodY -= random.randint(-2, 1)

    # superfood movement
    #    if sfoodX >= 500 and sfoodX <= 950:
    #        sfoodX += random.randint(-3, 3)
    #    if sfoodY >= 500 and sfoodY <= 950:
    #       sfoodY += random.randint(-3, 3)
    #   if sfoodX <= 500 and sfoodX >= 50:
    #       sfoodX -= random.randint(-3, 3)
    #   if sfoodY <= 500 and foodY >=50:
    #       sfoodY -= random.randint(-3, 3)
    # consuming food
    if x >= foodX and x <= foodX + foodRange and y >= foodY and y <= foodY + foodRange:
        print("you ate food")
        winsound.Beep(600, 50)
        winsound.Beep(750, 50)

        if foodX <= 500:
            foodX += random.randint(0, 450)
        if foodX >= 500:
            foodX -= random.randint(0, 450)
        if foodY <= 500:
            foodY += random.randint(0, 450)
        if foodY >= 500:
            foodY -= random.randint(0, 450)
        pColor = (0, 0, 0)
        foodCount += 100
        playerHealth += 3
        print(foodCount)

    # consuming superfood

    if x >= sfoodX and x <= sfoodX + foodRange and y >= sfoodY and y <= sfoodY + foodRange:
        print("you ate super food")
        winsound.Beep(660, 50)
        winsound.Beep(820, 50)

        if sfoodX <= 500:
            sfoodX += random.randint(0, 450)
        if sfoodX >= 500:
            sfoodX -= random.randint(0, 450)
        if sfoodY <= 500:
            sfoodY += random.randint(0, 450)
        if sfoodY >= 500:
            sfoodY -= random.randint(0, 450)
        pColor = (0, 0, 0)
        foodCount += 200
        playerHealth += 10
        print(foodCount)

    # velocity progression

    if foodCount > 2000 and foodCount < 3000:
        vel == 6

        enemyColor2 = 255, 0, 0
        enemyPositions = [
            [500, 250],
            [750, 750],
            [250, 750],
        ]
    if foodCount > 3000 and foodCount < 4000:
        vel == 7
        enemyColor2 = 255, 100, 0
        enemyPositions = [
            [500, 500],
            [100, 100],
            [900, 900],
            [900, 100],
            [100, 900],
        ]
        
    if foodCount > 5000 and foodCount < 6000:
        vel == 8

        enemyColor2 = 255, 0, 0
        enemyPositions = [
            [500, 500],
            [100, 100],
            [900, 900],
            [900, 100],
            [100, 900],
            [500, 900],
            [900, 500],
            [100, 500],
            [500, 100]
        ]

    keys = pygame.key.get_pressed()

    playerCoordinates = controlPlayerPosition(x, y)
    x = playerCoordinates[0]
    y = playerCoordinates[1]
    # davila enemy damage shit
    for enemyPos in enemyPositions:
        # enemyPos[1] = enemyPos[1] + 10
        # if (enemyPos[1] >= 1000):
        # enemyPos[0] = random.randint(0, 1000)
        # enemyPos[1] = random.randint(0, 100)
        pygame.draw.circle(win, enemyColor2, enemyPos, enemyRad, 2)
        if (isInCircle(enemyPos[0], enemyPos[1], x, y, 5)):
            playerHealth = playerHealth - 1
            winsound.Beep(500, 5)
            pColor = (255, 0, 0)
            if (playerHealth <= 0):
                isGameOver = True

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
