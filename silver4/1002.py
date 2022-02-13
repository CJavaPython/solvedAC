import math
#r1, x1, y1
#r2, x2, y2
#num of enemy location case / infinite : print "-1"
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, list(input().split()))
    #center distance 
    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if dist == 0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if abs(r1-r2) < dist < r1+r2:
            print(2)
        elif dist == abs(r1 - r2):
            print(1)
        elif dist == r1+r2:
            print(1)
        #use else!! it will be some problem if you don't think about exception
        else:
            print(0)