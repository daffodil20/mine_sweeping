import pygame
from random import random
import time
DIMENSION = 300
pygame.init()
running = True
# set up screen
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
# r = int(DIMENSION*random()/20)*8
# g = int(DIMENSION*random()/20)*8
# b = int(DIMENSION*random()/20)*8
    
#     # define the location of mines, fill screen,draw the mine
# screen.fill((r,g,b))
# # mine_timer += 0.001
# pygame.display.update()
# screen.fill((100,100,100))
# mine_x = int(DIMENSION*random()/20)*20
# mine_y = int(DIMENSION*random()/20)*20
# mine = pygame.Rect(mine_x,mine_y,20,20)
# pygame.draw.rect(screen,(0,255,255),mine)
# print(mine_x,mine_y)
def click():#(key,key_x,key_y):
# key = pygame.Rect(key_x,key_y,20,20)
    # key_x, key_y = pygame.mouse.get_pos()
    key_x = -1
    key_y = -1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            key_x, key_y = pygame.mouse.get_pos()
            print(key_x, key_y)
    # key = pygame.event.get_grab()
    # block = list(key)
    # key_x = block[0]
    # key_y = block[1]
    return (key_x,key_y)

mine_array = []
# generate random locations
for i in range(10):
    mine_x = int(DIMENSION*random()/20)*20
    mine_y = int(DIMENSION*random()/20)*20
    
    mine_array.append([mine_x,mine_y])
# print(mine_array)
# mine_timer = time.time()

while running:
    screen.fill((255,255,255))
# 
    # if time.time()-mine_timer > 1:
        # r = int(DIMENSION*random()/20)*8
        # g = int(DIMENSION*random()/20)*8
        # b = int(DIMENSION*random()/20)*8
    
#     # define the location of mines, fill screen,draw the mine
        # screen.fill((r,g,b))
        # mine_x = int(DIMENSION*random()/20)*20
        # mine_y = int(DIMENSION*random()/20)*20
        # mine_array.append([mine_x,mine_y])
    # draw mines
    for i in range(len(mine_array)):
        mine = pygame.Rect(mine_array[i][0],mine_array[i][1],20,20)
        pygame.draw.rect(screen,(255,255,255),mine)

    # pygame.display.update()
        # mine_timer += 1
    z = click()
    x = z[0]
    y = z[1]
    # print(x,y)
    for i in range(len(mine_array)):  # 
        if  mine_array[i][0]<x<mine_array[i][0]+20 and mine_array[i][1]<y<mine_array[i][1]+20:
            mine = pygame.Rect(mine_array[i][0],mine_array[i][1],20,20)
            pygame.draw.rect(screen,(0,0,0),mine)
            print("game ends")
            running = False
            break
    pygame.display.update()
pygame.quit()
    
    # pygame.display.update()
        
        # pygame.draw.rect(screen,(255,255,255),mine)

    # define a function click (use in the )
    # def click(key,key_x,key_y):
        # key = pygame.Rect(key_x,key_y,20,20)
        # key = pygame.event.get_grab()
        # block = list(key)
        # key_x = block[0]
        # key_y = block[1]
        # key_x = pygame.event.get_grab()
    #events triggered by keyboard
        # for event in pygame.event.get():
        #     if event.type == pygame.K_SPACE:
        #         if key_x == mine_x and key_y == mine_y:
        #             key.clear()
        #             print("game ends")
        #             False
        #         else:
        #             True
        # return block
        
    # click(key,block)
