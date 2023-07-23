import pygame
from random import random

DIMENSION = 600
pygame.init()
# running = True
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
def click():#(key,key_x,key_y):
# key = pygame.Rect(key_x,key_y,20,20)
    key = pygame.event.get_grab()
    block = list(key)
    key_x = block[0]
    key_y = block[1]
    return block
while True:
# set up screen
    
# define the location of mines, fill screen,draw the mine
    screen.fill((100,100,100))
    mine_x = int(DIMENSION*random()/20)*20
    mine_y = int(DIMENSION*random()/20)*20
    mine = pygame.Rect(mine_x,mine_y,20,20)
    pygame.draw.rect(screen,(255,255,255),mine)

# define a function click (use in the )
# def click(key,key_x,key_y):
    # key = pygame.Rect(key_x,key_y,20,20)
    # key = pygame.event.get_grab()
    # block = list(key)
    # key_x = block[0]
    # key_y = block[1]
    # key_x = pygame.event.get_grab()
#events triggered by keyboard
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            if key_x == mine_x and key_y == mine_y:
                key.clear()
                print("game ends")
                False
            else:
                True
    # return block

click(key,block)
