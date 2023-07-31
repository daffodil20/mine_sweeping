import pygame
from random import random
import time
DIMENSION = 300
pygame.init()
running = True
# set up screen
screen = pygame.display.set_mode([DIMENSION,DIMENSION])

def game_over(): 
    font=pygame.font.SysFont("Arial",18)
    # txtsurf=font.render(str("game over"),True,(0,0,255))
    txtsurf=font.render(str("game over").encode("utf-8").decode("utf-8"),True,(0,0,255))

    screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(0, 0))

def click():
    key_x = -1
    key_y = -1
    LEFT = 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            key_x, key_y = pygame.mouse.get_pos()
            print(key_x, key_y)
   
    return (key_x,key_y)

# TODO: add function right click,first add a flag,then add a question mark
def right_click():
    kr_x = -1
    kr_y = -1
    RIGHT = 3
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            kr_x, kr_y = pygame.mouse.get_pos()
            print("right: ",kr_x, kr_y)
    return (kr_x,kr_y)

mine_array = []
rgb = []
# generate random locations
for i in range(10):
    mine_x = int(DIMENSION*random()/20)*20
    mine_y = int(DIMENSION*random()/20)*20
    
    mine_array.append([mine_x,mine_y])
    rgb.append((255,255,255))

is_game_over = False
while running:
    # rgb = []
    screen.fill((255,255,255))

    for i in range(len(mine_array)):
        mine = pygame.Rect(mine_array[i][0],mine_array[i][1],20,20)
        pygame.draw.rect(screen,rgb[i],mine)

    # TODO: add timer
    timer = time.time()
    z = click()
    x = z[0]
    y = z[1]
    right_click()
    # print(x,y)
    for i in range(len(mine_array)):  
        if  mine_array[i][0]<x<mine_array[i][0]+20 and mine_array[i][1]<y<mine_array[i][1]+20:
            # mine = pygame.Rect(mine_array[i][0],mine_array[i][1],20,20)
            rgb[i] = (0,0,0)
            # pygame.display.update()
            print("game over")
            is_game_over = True
    font=pygame.font.SysFont("Arial",6)
    # txtsurf=font.render(str("game over"),True,(255,255,255))
    txtsurf=font.render(str(time.time()).encode("utf-8").decode("utf-8"),True,(0,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    screen.blit(txtsurf,(0, 0))
    if is_game_over == True:
        game_over()

            # pygame.draw.rect(screen,rgb[i],mine)
            # print("game ends")
            # break
            # running = False
        # TODO: if it isn't mine,reveal the sapce
        # else:
        #     block = pygame.Rect(x,y,20,20)
        #     pygame.draw.rect(screen,(85,85,85),block)
        #     # 8 blocks,for loop 
        #     # if there are mines in blocks, label the block with number
        #     # else, reveal the 9 blocks and caculate the farther blocks using for loop
        #     if abs(x-mine_array[i][0]) > 20 and abs(y-mine_array[i][1]) > 20:

            # TODO: add game over
            # running = False
            
            # rgb[i] = (0,0,0)
    #print("game over")
    pygame.display.update()
# pygame.quit()
    
    