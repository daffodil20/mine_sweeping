# for i in range(5):
#     print(i)

# blocks = [0,1,2,3]
blocks=[1,2,3,4]
def match_block1(click):
    def match_block2(bb):
        print(click,bb)
        return(click+bb)
    return match_block2(bb)

m2 = match_block1(2)
map(m2,blocks)
# print(list(map(m2,blocks)))
# print(match_block2(1))
# import time
# from functools import reduce
# blocks = []
# for i in range(10000000):
#     blocks.append(i)
# t0= time.time()
# def multiplier(a,b):
#     return a+b
# print(int(reduce(multiplier,blocks)))
# t1=time.time()-t0
# print(t1)
# t=time.time()
# i=0
# result=0
# while i<len(blocks):
#     result=blocks[i]+result
#     # blocks[i]*2
#     i+=1
# t2=time.time()-t
# print(t2)
# print(result)
























