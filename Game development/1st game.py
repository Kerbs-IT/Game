import pygame
import random
import math
from pygame import mixer
pygame.init()

# create a display
screen = pygame.display.set_mode((800, 600))
# title and icon
pygame.display.set_caption("Space Game")
icon = pygame.image.load("1.png")
pygame.display.set_icon(icon)
# Background
Background = pygame.image.load('BG.png')

# player1
playerImg = pygame.image.load('rocket.png')
playerx = 370
playery = 480
x_change = 0
y_change = 0

# enemy
enemyImg = []
enemyx = []
enemyy = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 750))
    enemyy.append(random.randint(50, 200))
    enemyX_change.append(1.50)
    enemyY_change.append(40)

#   bullet
BulletImg = pygame.image.load('bullet.png')
Bulletx = 0
Bullety = 480
BulletX_change = 0
BulletY_change = 10
Bullet_state = 'ready'

# rocks
rock_Img = []
rock_x = []
rock_y = []
rock_x_change = []
rock_y_change = []
num_of_rocks = 50
for k in range(num_of_rocks):
    rock_Img.append(pygame.image.load('meteor.png'))
    rock_x.append(random.randint(0, 750))
    rock_y.append(random.randint(0,600))
    rock_x_change.append(0.5)
    rock_y_change.append(0.5)


def rocks_load(rockx,rocky,k):
    screen.blit(rock_Img[k], (rockx,rocky))



def bullet_fire(x, y):
    global Bullet_state
    Bullet_state = 'Fire'
    screen.blit(BulletImg, (x+16, y+10))


# GAME OVER
Gameover_font = pygame.font.SysFont('Font/Pixel_font.TTF', 60, bold= pygame.font.Font.bold)


def gameover_over_text():
    gameover_text = Gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (230, 300))

# image of the spaceship in the screen
def character(x, y):
    screen.blit(playerImg, (x, y))

# show the enemy in the screen
def Enemy(enemyx, enemyy, i):
    screen.blit(enemyImg[i], (enemyx, enemyy))

# collision
def iscollision(enemyx,enemyy,Bulletx,Bullety):
    distance = math.sqrt((math.pow(enemyx-Bulletx,2)) + (math.pow(enemyy - Bullety, 2)))
    if distance < 27:
        return True
    else:
        return False
#score value
count = int(0)
font = pygame.font.SysFont('Font/Pixel_font.TTF', 24, bold= pygame.font.Font.bold)
ScoreX = 10
ScoreY = 10


def score(x, y):
    score = font.render("SCORE: "+str(count), True, (255, 255, 255))
    screen.blit(score, (x, y))
# round system
roundone = pygame.font.SysFont('Font/Pixel_font.TTF', 24, bold= pygame.font.Font.bold)
def game_round_one():
    round_one = roundone.render('ROUND 1', True, (255, 255, 255))
    screen.blit(round_one, (340, 20))

# game over text
gameX = 370
gameY = 300


# Background music
mixer.music.load('Background.ogg')
mixer.music.play(-1)

run = True


while run:
    # RGB - fill of the display screen
    screen.fill((0, 0, 0))
    # background
    screen.blit(Background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = 3.0
            if event.key == pygame.K_LEFT:
                x_change = -3.0
            if event.key == pygame.K_UP:
                y_change = -3.0
            if event.key == pygame.K_DOWN:
                y_change = 3.0
            if event.key == pygame.K_SPACE:
                if Bullet_state == 'ready':
                    Bullet_Sound = mixer.Sound('bullet.wav')
                    Bullet_Sound.play()
                    Bulletx = playerx
                    bullet_fire(Bulletx, Bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0

    playery += y_change
    playerx += x_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx= 736
    if playery <= 0:
        playery = 0
    if playery >= 536:
        playery = 536

    #rocks

    for i in range(num_of_rocks):

        rock_y[i] += rock_y_change[i]
        if  rock_x[i] <= 0 or rock_x[i] >= 800 or rock_y[i] <= 0 or rock_y[i] >= 600 :
            rock_y[i] = random.randint(0, 5)
            rock_x[i] += rock_x_change[i]
            rock_y[i] += rock_y_change[i]
        rocks_load(rock_x[i], rock_y[i], i)


    # enemy
    for i in range(num_of_enemy):
        # if the enemy hits the radius of the space ship means that game over
        #Enemy_distance = math.sqrt((math.pow(enemyx[i]-playerx,2)) + (math.pow(enemyy[i]-playery,2)))
        if enemyy[i] > 450:
            for j in range(num_of_enemy):
                enemyy[j] = 2000
            gameover_over_text()
            break

        enemyx[i] += enemyX_change[i]
        if enemyx[i] <= 0:
            enemyX_change[i] = 1.50
            enemyy[i] += enemyY_change[i]
            if count >= 25:
                enemyX_change[i] = 2.00
                enemyy[i] += enemyY_change[i]
            elif count >= 25 and count <= 50:
                enemyX_change[i] = 2.50
                enemyy[i] += enemyY_change[i]
            elif count >= 50 and count <= 100:
                enemyX_change[i] = 3.00
                enemyy[i] += enemyY_change[i]
        elif enemyx[i] >= 736:
            enemyX_change[i] = -1.50
            enemyy[i] += enemyY_change[i]
            if count >= 25:
                enemyX_change[i] = -2.00
                enemyy[i] += enemyY_change[i]
            elif count >= 25 and count <50:
                enemyX_change[i] = -2.50
                enemyy[i] += enemyY_change[i]
            elif count >= 50 and count <= 100:
                enemyX_change[i] = -3.00
                enemyy[i] += enemyY_change[i]


        Collision = iscollision(enemyx[i], enemyy[i], Bulletx, Bullety)
        # if collision is true count +1 and move the enemy to another location
        if Collision:
            Bullety = 480
            Bullet_state = 'ready'
            enemyx[i] = random.randint(0, 750)
            enemyy[i] = random.randint(50, 150)
            count += 1
            Collision_Sound = mixer.Sound('HIT.mp3')
            Collision_Sound.play()
        Enemy(enemyx[i], enemyy[i], i)

    # bullet action
    if Bullety <= 0:
        Bullety = 480
        Bullet_state = 'ready'

    if 'Fire' in Bullet_state:
        bullet_fire(Bulletx, Bullety)
        Bullety -= BulletY_change
    # print rounds
    if count >= 0 and count <= 25 :
        roundone = pygame.font.Font('Font/Pixel_font.TTF', 30)
        round_one = roundone.render('Round 1', True, (255, 255, 255))
        screen.blit(round_one, (340, 20))
    elif count > 25 and count <= 50:
        roundone = pygame.font.Font('Font/Pixel_font.TTF', 30)
        round_one = roundone.render('Round 2', True, (255, 255, 255))
        screen.blit(round_one, (340, 20))
    elif count > 50 and count < 100:
        roundone = pygame.font.Font('Font/Pixel_font.TTF', 30)
        round_one = roundone.render('Round 3', True, (255, 255, 255))
        screen.blit(round_one, (340, 20))
    # player dead or not
    character(playerx, playery)  # call the spaceship image in the screen
    score(ScoreX, ScoreY)  # call out the score text
    pygame.display.update()  # to update all that's happening inside the game

