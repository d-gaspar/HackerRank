#!/usr/bin/python

def nextMove(n,r,c,grid):
    # find princess position 
    for idx,value in enumerate(grid):
        if("p" in value):
            princess = (idx, value.index("p"))
    
    direction_h = c - princess[1]
    direction_v = r - princess[0]
    
    if(direction_h < 0):
        return("RIGHT")
    elif(direction_h > 0):
        return("LEFT")
    
    if(direction_v < 0):
        return("DOWN")
    elif(direction_v > 0):
        return("UP")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
