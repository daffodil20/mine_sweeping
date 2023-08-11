import pygame
from random import random
import time
DIMENSION = 300
LEFT = 1

pygame.init()
# running = True
# set up screen
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
class Mine:
    i_j = [0,0]
    is_reveal = False
    rgb = [255,255,255]
    def __init__(self,i,j) -> None:
        self.i_j = [i,j]
    
    
mine_array = []
# rgb = []
# exclude same positions
# n = 0
# while n<10:
#     mine_i = int(random()*15)
#     mine_j = int(random()*15)
#     # mine_array.append([mine_i,mine_j])
#     m = Mine(mine_i,mine_j) # store x_y not i_j
#     mine_array.append(m)
#     n+=1
#     if n>1:
#         for t in mine_array:
#             if t.i_j != [mine_i, mine_j]:
#                 m = Mine(mine_i,mine_j) # store x_y not i_j
#                 mine_array.append(m)
# print(mine_array)


n = 0
while n<11:
    mine_i = int(random()*15)
    mine_j = int(random()*15)
    # mine_array.append([mine_i,mine_j])
    m = Mine(mine_i,mine_j) # store x_y not i_j
    mine_array.append(m)
    n+=1
    a=0
    if n>=1:
        for t in mine_array:
            if t.i_j != [mine_i, mine_j]:
                a+=0
            if t.i_j == [mine_i, mine_j]:
                a+=1
        if a == 0:
            m = Mine(mine_i,mine_j) # store x_y not i_j
            mine_array.append(m)
            n+=1
print(mine_array)
                # print("mineList: ",mine_array)
            
def game_over():
    mine_rgb = [255,255,255]
    for m in mine_array:
        rm = pygame.Rect(m.i_j[0]*20,m.i_j[1]*20,20,20)
        pygame.draw.rect(screen,mine_rgb,rm)
    print("show me game over")

def reveal_mine(key_i,key_j,mn):
    for i in range(len(mn)):  
        if  mn[i].i_j[0] == key_i and mn[i].i_j[1] == key_j:
# mine = pygame.Rect(mine_array[i][0],mine_array[i][1],20,20)
            mn[i].rgb = [255,255,255]
            # pygame.display.update()
            # is_game_over = False
            # for j in range(len(mine_array)):
            mine = pygame.Rect(mn[i].i_j[0]*20,mn[i].i_j[1]*20,20,20)
            pygame.draw.rect(screen,mn[i].rgb,mine)

            # print("game over")
            print(key_i,key_j)
            print(mn[i].i_j[0],mn[i].i_j[1])
            game_over()
            # return()
    draw_numbers(key_i,key_j)        
                
class Block:
    x_y = [0,0]
    is_reveal = False
    is_mine = False
    # m_list = [] # [0,0,1,1,0,0,1,0]
    total = 0
    def __init__(self, i,j,nm) -> None:
        i_j = [i,j]
        # x = 0
        # y = 0
        # x,y = reveal_mine(x,y)
        # record the number of mines around one block
        for m in nm:
            for p in [-1,0,1]:
                for q in [-1,0,1]: # nm=mine_array
                    if m.i_j[0]== i_j[0]+p and m.i_j[1] == i_j[1]+q:
                        # m_list.append(1)
                        # is_mine = True
                        # 15*(y-1)+x+p+15*q
                        self.total += 1
                    if m.i_j[0]== i_j[0]+p and m.i_j[1] == i_j[1]+q and p == 0 and q == 0:
                        self.total += 0
                        # if p == 0 and q == 0::
                        #     self.total += 0
                    else:
                        self.total += 0
                # m_list.append(0)

    
blocks = []
for i in range(15):
    for j in range(15):
        b = Block(i, j, mine_array)
        # b.click()
        blocks.append(b)



# TODO: def draw_blocks
# TODO: if the block doesn't have a mine, reveal the block and label number of mines surrounding it; else, only reveal the block and game over
# TODO: condition1: reveal the mine and game over condition2: reveal the block and label numvers
def draw_numbers(key_i, key_j):
    # for i in range(len(mn)):  
        # if  mn[i].x_y[0] != key_i or mn[i].x_y[1] !=key_j:
            # for p in [-1,0,1]:
            #     for q in [-1,0,1]:# label numbers
                    # x,y = 0
                    # x,y = click_draw_block(x,y)
    blank = pygame.Rect(20*key_i,20*key_j,20,20)
    rgb = [170,170,170]
    pygame.draw.rect(screen,rgb,blank)
    # if blocks[(click_draw_block(key_x)+p)*(click_draw_block(key_y)+q)].total != 0:
    numbers = blocks[15*(key_j-1)+key_i].total
    if numbers != 0:
        font=pygame.font.SysFont("Arial",18)
        # txtsurf=font.render(str("game over"),True,(0,0,255))
        # numbers = blocks[15*(key_y-1)+key_x].total
        # text = 1
        txtsurf=font.render(str(numbers).encode("utf-8").decode("utf-8"),True,(0,0,255))
        
        screen.blit(txtsurf,(20*key_i,20*key_j))
        # n+=1

    # if len(mine_array) == 10: 
    # for a in range(10):
    #     for b in range(10):
    #         if mine_array[a] == mine_array[b] and a != b:
    #             mine_array.clear()
    #         else:
    #             # print("mineList: ",m.i_j)
    #             generating = False
    # rgb.append((0,0,0))
# print("mineList: ",mine_array)
        # print(numbers)
        # pygame.display.update()

is_game_over = True
while is_game_over:
    # for a in range(10):
    for event in pygame.event.get():
        key_x, key_y = pygame.mouse.get_pos()
        key_i = int(key_x/20)
        key_j = int(key_y/20)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            reveal_mine(key_i, key_j, mine_array)
            print(key_i,key_j)
    pygame.display.update()

    
    