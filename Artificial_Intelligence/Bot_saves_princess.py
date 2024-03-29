#!/usr/bin/python

def displayPathtoPrincess(M,grid):
    # find mario and princess position
    output = ""

    for idx, value in enumerate(grid):
        if("m" in value):
            mario = (idx, grid[idx].index("m"))

        if("p" in value):
            princess = (idx, grid[idx].index("p"))

    direction_v = mario[0] - princess[0]
    direction_h = mario[1] - princess[1]

    if(direction_h < 0):
        output = ["RIGHT"]*abs(direction_h)
    elif(direction_h > 0):
        output = ["LEFT"]*direction_h

    if(direction_v < 0):
        output = output + ["DOWN"]*abs(direction_v)
    elif(direction_v > 0):
        output = output + ["UP"]*direction_v

    return("\n".join(output))

m = int(input())
grid = []
for i in range(0, m): 
    grid.append(input().strip())

print(displayPathtoPrincess(m,grid))
