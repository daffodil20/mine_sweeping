import pygame
from random import random
import time
DIMENSION = 300
LEFT = 1

pygame.init()
# running = True
# set up screen
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
screen.fill((55,0,0))
class Mine:
    i_j = [0,0]
    is_reveal = False
    rgb = [255,255,255]
    def __init__(self,i,j) -> None:
        self.i_j = [i,j]
    
    
mine_array = []
n = 1
m_i = int(random()*15)
m_j = int(random()*15)
# mine_array.append([mine_i,mine_j])
mm = Mine(m_i,m_j) # store x_y not i_j
mine_array.append(mm)
while n<10:
    mine_i = int(random()*15)
    mine_j = int(random()*15)
    # mine_array.append([mine_i,mine_j])
    
 
    a=0
    # if n>=1:
    for t in mine_array:
        if t.i_j == [mine_i, mine_j]:
            a+=1
    if a == 0:
        m = Mine(mine_i,mine_j) # store x_y not i_j
        mine_array.append(m)
        n+=1
for t in mine_array:
    print("mine_array:",t.i_j)
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
            game_over()
            return()
    if blocks[15*key_i+key_j].total != 0:
        draw_numbers(key_i,key_j)
    if blocks[15*key_i+key_j].total == 0:
        reveal_blocks([[key_i,key_j]])       
                # update
class Block:
    x_y = [0,0]
    is_reveal = False
    is_mine = False
    # m_list = [] # [0,0,1,1,0,0,1,0]
    total = 0
    def __init__(self, i,j,nm) -> None:
        i_j = [i,j]
        # record the number of mines around one block
        for m in nm:
            if m.i_j[0] == i and m.i_j[1] == j:
                break
            else:
                for p in [-1,0,1]:
                    for q in [-1,0,1]: # nm=mine_array
                        if m.i_j[0] == i+p and m.i_j[1] == j+q:
                            self.total += 1
        # print("total:",self.total)

    
blocks = []
for i in range(15):
    for j in range(15):
        b = Block(i, j, mine_array)
        # print("total_display: ",[i,j],":",b.total)
        # b.click()
        blocks.append(b)



# TODO: def draw_blocks
# TODO: if the block doesn't have a mine, reveal the block and label number of mines surrounding it; else, only reveal the block and game over
# TODO: condition1: reveal the mine and game over condition2: reveal the block and label numvers
# def draw_numbers(key_i, key_j):
#     if 15*key_i+key_j > 224 or 15*key_i+key_j < 0:
#         for m in [-1,0,1]:
#             for n in [-1,0,1]:
#                 draw_numbers(key_i+m,key_j+n)
#     else:
#         numbers = blocks[15*key_i+key_j].total
    
#     # numbers = blocks[key_i*key_j].total
#         if numbers == 0:
#             for m in [-1,0,1]:
#                 for n in [-1,0,1]:
#                     if key_i+m<0 or key_i+m>14 or key_j+n<0 or key_j+n>14:
#                         return()
#                     else:
#                         print("key_i:",key_i+m,key_j+n)
#                         blank = pygame.Rect(20*(key_i+m),20*(key_j+n),20,20)
#                         rgb = [170,170,170]
#                         pygame.draw.rect(screen,rgb,blank)
#                         draw_numbers(key_i+m,key_j+n)
                    
#         if numbers != 0:
#             blank = pygame.Rect(20*key_i,20*key_j,20,20)
#             rgb = [170,170,170]
#             pygame.draw.rect(screen,rgb,blank)
#             font=pygame.font.SysFont("Arial",18)
#             # txtsurf=font.render(str("game over"),True,(0,0,255))
#             # numbers = blocks[15*(key_y-1)+key_x].total
#             # text = 1
#             txtsurf=font.render(str(numbers).encode("utf-8").decode("utf-8"),True,(0,0,255))
            
#             screen.blit(txtsurf,(20*key_i,20*key_j))

def reveal_blocks(blocks_array):
    for bb in blocks_array:
        
        # if 15*bb[0]+bb[1] <= 224 and 15*bb[0]+bb[1] >= 0:
            # for m in [-1,0,1]:
            #     for n in [-1,0,1]:
            #         draw_numbers(key_i+m,key_j+n)
        # else:
        # numbers = blocks[15*bb[0]+bb[1]].total
        blocks_array.remove(bb)
    # numbers = blocks[key_i*key_j].total
        # if numbers == 0:
        temp_array = []
        for m in [-1,0,1]:
            for n in [-1,0,1]:
                if m == 0 and n == 0:
                    continue
                # if bb[0]+m<0 or bb[0]+m>14 or bb[1]+n<0 or bb[1]+n>14:
                    # if 15*(bb[0]+m)+bb[1]+n<0 or 15*(bb[0]+m)+bb[1]+n>224:
                        # return()
                else:
                    if 15*(bb[0]+m)+bb[1]+n >= 0 and 15*(bb[0]+m)+bb[1]+n <= 224:
                        # continue
                    # print("key_i:",bb[0]+m,bb[1]+n)
                    # blank = pygame.Rect(20*(bb[0]+m),20*(bb[1]+n),20,20)
                    # rgb = [170,170,170]
                    # pygame.draw.rect(screen,rgb,blank)
                    # if m == 0 and n == 0:
                    #     return()
                    
                        print("key_i:",bb[0]+m,bb[1]+n)
                        NUM = blocks[15*(bb[0]+m)+bb[1]+n].total
                        if NUM != 0:
                            blank = pygame.Rect(20*(bb[0]+m),20*(bb[1]+n),20,20)
                            rgb = [170,170,170]
                            pygame.draw.rect(screen,rgb,blank)
                            font=pygame.font.SysFont("Arial",18)
                            txtsurf=font.render(str(NUM).encode("utf-8").decode("utf-8"),True,(0,0,255))
                            screen.blit(txtsurf,(20*(bb[0]+m),20*(bb[1]+n)))
                            continue
                        
                        if NUM == 0:
                            blank = pygame.Rect(20*(bb[0]+m),20*(bb[1]+n),20,20)
                            rgb = [170,170,170]
                            pygame.draw.rect(screen,rgb,blank)                            
                            temp_array.append([bb[0]+m,bb[1]+n])
                    else:
                        continue

            reveal_blocks(temp_array)
                   
        # if numbers != 0:
        #     blank = pygame.Rect(20*bb[0],20*bb[1],20,20)
        #     rgb = [170,170,170]
        #     pygame.draw.rect(screen,rgb,blank)
        #     font=pygame.font.SysFont("Arial",18)
        #     # txtsurf=font.render(str("game over"),True,(0,0,255))
        #     # numbers = blocks[15*(key_y-1)+key_x].total
        #     # text = 1
        #     txtsurf=font.render(str(numbers).encode("utf-8").decode("utf-8"),True,(0,0,255))
            
        #     screen.blit(txtsurf,(20*bb[0],20*bb[1]))
def draw_numbers(key_i,key_j):
    blank = pygame.Rect(20*key_i,20*key_j,20,20)
    rgb = [170,170,170]
    pygame.draw.rect(screen,rgb,blank)
    font=pygame.font.SysFont("Arial",18)
    txtsurf=font.render(str(blocks[15*key_i+key_j].total).encode("utf-8").decode("utf-8"),True,(0,0,255))
    screen.blit(txtsurf,(20*key_i,20*key_j))

is_game_over = True
t = time.time()
while is_game_over:
    screen.fill((0,0,0),(0,0,40,40))
    font=pygame.font.SysFont("Arial",15)
    txtsurf = font.render(str(int(time.time()-t)).encode("utf-8").decode("utf-8"),True,(255,255,255))
    screen.blit(txtsurf,(20,20))
    # print(time.time()-t)
    for event in pygame.event.get():
        key_x, key_y = pygame.mouse.get_pos()
        key_i = int(key_x/20)
        key_j = int(key_y/20)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            reveal_mine(key_i, key_j, mine_array)
            # print(key_i,key_j)
    pygame.display.update()
    # pygame.display.flip()

    
    