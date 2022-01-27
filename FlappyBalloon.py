import pgzrun
from random import randint
import pygame
from pygame import gfxdraw, key
from pygame.locals import K_SPACE, K_s
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

surface = pygame.display.set_mode((800,600))
color = (255,255,0)
ballon = Actor("balloon")
bird = Actor("bird-up")
house = Actor("house")
egg1 = Actor("one-egg")
egg2 = Actor("one-egg")

score = 0
start_game = False
game_over = False

wallleft = Rect(0,0,0,600)
wallbottom = Rect(0,600,800,0)
walltop = Rect(0,0,800,0)

def botOn():
    #Ausweichen House
    distanceWallleft = ballon.x
    distanceHouseX = (800- ballon.x) - (800- house.x)
    heightHouse = 600- house.y
    
    if ballon.y < 252:
        ballon.y = 245
    if distanceHouseX < 242.0 and ballon.y > 252:
        ballon.y = 245
    #Ausweichen Bird
    distanceBirdX = (800- ballon.x) - (800- bird.x)
    
    if ballon.y < 165:
        ballon.y = 245
    #Ausweichen Egg1
    distanceEgg1 = (800- ballon.x) - (800- egg1.x)
    
    if distanceEgg1 > 0:
        if (ballon.x +75) >= (egg1.x- 20):
            ballon.x = ballon.x- 50
    elif distanceEgg1 < 0:
        if (ballon.x -75) <= (egg1.x+ 20):
            ballon.x = ballon.x+ 50
    #Ausweichen Egg2
    distanceEgg2 = (800- ballon.x) - (800- egg2.x)
    
    if distanceEgg2 > 0:
        if (ballon.x +75) >= (egg2.x- 20):
            ballon.x = ballon.x- 50
    elif distanceEgg2 < 0:
        if (ballon.x -75) <= (egg2.x+ 20):
            ballon.x = ballon.x+ 50
            
def place_actors():
    ballon.x = 400
    ballon.y = 300
    bird.x = 800 
    bird.y = randint(0,100)
    house.x = 800 
    house.y = 460
    egg1.x = randint(0,800)
    egg1.y = 1
    egg2.x = randint(0,800)
    egg2.y = 1

def draw():
    global game_over
    global start_game
    mouse = pygame.mouse.get_pos()
    
    if game_over:
        screen.fill("pink")
        screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=60)
        stop()
    else:
        game_over = False
        screen.blit("background", (0,0))
        screen.draw.text("Score: " + str(score), topleft=(10,10))
        ballon.draw()
        bird.draw()
        house.draw()
        egg1.draw()
        egg2.draw()
                
        pygame.gfxdraw.rectangle(surface, wallleft, color)
        pygame.gfxdraw.rectangle(surface, wallbottom, color)
        pygame.gfxdraw.rectangle(surface, walltop, color)
        pygame.display.flip()
        
def update():
    global score
    global game_over
    global start_game
    global startTimer

    pressed_keys = pygame.key.get_pressed()
    
    if game_over:
        return

    if keyboard.left:
        ballon.x = ballon.x - 3
    elif keyboard.right:
        ballon.x = ballon.x + 3
    elif keyboard.up:
        ballon.y = ballon.y - 2
    elif keyboard.down:
        ballon.y = ballon.y + 2

    if bird.colliderect(wallleft):
        bird.x = randint(500,800)
        bird.y = randint(0,100)
        score = score + 1
    elif house.colliderect(wallleft):
        house.x = randint(700,800)
        house.y = 460
        score = score + 1
    elif egg1.colliderect(wallbottom):
        egg1.x = randint(0,800)
        egg1.y = 0
        score = score + 1
    elif egg2.colliderect(wallbottom):
        egg2.x = randint(0,800)
        egg2.y = 0
        score = score + 1

    if ballon.colliderect(bird):
        game_over = True
    elif ballon.colliderect(house):
        game_over = True
    elif ballon.colliderect(egg1):
        game_over = True
    elif ballon.colliderect(egg2):
        game_over = True

    #Für den Bot
    if pressed_keys[K_SPACE]:
        botOn()
    
def movement():
    bird.x = bird.x - 2
    house.x = house.x - 2
    egg1.y = egg1.y + 3
    egg2.y = egg2.y + 2

def stop():
    global score
    bird.x = 0
    house.x = 0
    egg1.x = 0
    egg2.x = 0
    
    if keyboard.left:
        ballon.x = ballon.x
    elif keyboard.right:
        ballon.x = ballon.x
    elif keyboard.up:
        ballon.y = ballon.y
    elif keyboard.down:
        ballon.y = ballon.y



clock.schedule_interval(movement, 0.01)
place_actors()

pgzrun.go()
