#
# Nandani Patidar
#
# A* algorithm
#


from maze import *
import itertools

def cal_H_Val(maze):

    hGrid = []
    xT = yT = len(maze)- 1
    x1 =0
    for row in maze:
        hRow = []
        y1 = 0
        for block in row:   
            hueValue = (xT - x1) + (yT - y1)
            hRow.append(hueValue)
            y1 = y1 + 1
        x1 = x1 + 1
        hGrid.append(hRow)
    
    return hGrid

def cal_G_Val(maze):
    gGrid = []
    xT = yT = 0
    x1 =0
    for row in maze:
        gRow = []
        y1 = 0
        for block in row:    
            gRow.append(0)
            y1 = y1 + 1
        x1 = x1 + 1
        gGrid.append(gRow)
    
    return gGrid

def cal_F_Val(hGrid, gGrid):
    fGrid = []
    for (gRow, hRow) in zip(gGrid, hGrid):
        fRow = []

        for (g, h) in zip(gRow, hRow):
            f = g + h
            fRow.append(f)
        fGrid.append(fRow)
        
    return fGrid

def algoAstar(maze):
    openList = []
    closedList = []
    startX = 0
    startY = 0
    currentX = startX
    currentY = startY
    
    while (currentX != targetX & currentY != targetY):
        eastX = currentX + 1
        eastY = currentY

        northX = currentX
        northY = currentY + 1
        
        westX = currentX - 1
        westY = currentY 
        
        southX = currentX   
        southY = currentY - 1
        
          

a= Maze()
maze_gen = a.makeMaze(5)
maze_H = cal_H_Val(maze_gen)
print(maze_H)
maze_G = cal_G_Val(maze_gen)
print(maze_G)
print(cal_F_Val(maze_H, maze_G))
