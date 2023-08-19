import pygame
from random import random
import time
DIMENSION = 300
LEFT = 1
counter = 0
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

    total = 0
    def __init__(self, i,j,nm) -> None:
        i_j = [i,j]
        # record the number of mines around one block
        for m in nm:
            if m.i_j[0] == i and m.i_j[1] == j:
                break
            else:
                for p in [-1,0,1]:
                    for q in [-1,0,1]:
                        if m.i_j[0] == i+p and m.i_j[1] == j+q:
                            if p == 0 and q == 0:
                                self.total -= 1# nm=mine_array
                            else:
                                self.total += 1
        print("total:",i_j,self.total)
        
    
blocks = []
for i in range(15):
    for j in range(15):
        b = Block(i, j, mine_array)
        # print("total_display: ",[i,j],":",b.total)
        # b.click()
        blocks.append(b)

def reveal_blocks(blocks_array):
    # global counter
    # if counter < 60:
    print("bb:",blocks_array)
        # counter += 1
    for bb in blocks_array:
        # blocks_array.remove(bb)
    # numbers = blocks[key_i*key_j].total
        # if numbers == 0:
        temp_array = []
        for m in [-1,0,1]:
            for n in [-1,0,1]:
                if m == 0 and n == 0:
                    continue
                else:
                    if bb[0]+m >= 0 and bb[0]+m <= 14 and bb[1]+n >= 0 and bb[1]+n <= 14:
                        NUM = blocks[15*(bb[0]+m)+bb[1]+n].total
                        if NUM != 0 and NUM !=-1 and blocks[15*(bb[0]+m)+bb[1]+n].is_reveal == False:
                            blank = pygame.Rect(20*(bb[0]+m),20*(bb[1]+n),20,20)
                            rgb = [170,170,170]
                            pygame.draw.rect(screen,rgb,blank)
                            font = pygame.font.SysFont("Arial",18)
                            txtsurf = font.render(str(NUM).encode("utf-8").decode("utf-8"),True,(0,0,255))
                            screen.blit(txtsurf,(20*(bb[0]+m),20*(bb[1]+n)))
                            blocks[15*(bb[0]+m)+bb[1]+n].is_reveal = True
                            continue
                        
                        if NUM == 0 and NUM != -1 and blocks[15*(bb[0]+m)+bb[1]+n].is_reveal == False:
                            blank = pygame.Rect(20*(bb[0]+m),20*(bb[1]+n),20,20)
                            rgb = [170,170,170]
                            pygame.draw.rect(screen,rgb,blank)
                            blocks[15*(bb[0]+m)+bb[1]+n].is_reveal = True
                            temp_array.append([bb[0]+m,bb[1]+n])
                    else:
                        continue

        reveal_blocks(temp_array)
def reveal_state():
    for x in range(15):
        for y in range(15):
            print("is_reveal",15*x+y,blocks[15*x+y].is_reveal)
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
            reveal_state()
            # print(key_i,key_j)
    pygame.display.update()
    # pygame.display.flip()

    
    