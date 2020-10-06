#
# Nandani Patidar
#
# A* algorithm
#

from maze import *
import itertools
import heapq as hp

def cal_H_Val(maze):
    hGrid = []
    xT = yT =(len(maze))- 1
             
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

def cal_G_Val():
    gGrid = []
    xT = yT = 0
    x1 =0
    for row in maze_gen:
        gRow = []
        y1 = 0
        for block in row:    
            gRow.append(0)
            y1 = y1 + 1
        x1 = x1 + 1
        gGrid.append(gRow)
    
    return gGrid

def upd_G_Val(x, y, curX, curY):
    gGrid[x][y] = gGrid[curX][curY] + 1
    
    
def cal_F_Val():
    fGrid = []
    for (gRow, hRow) in zip(gGrid, hGrid):
        fRow = []

        for (g, h) in zip(gRow, hRow):
            f = g + h
            fRow.append(f)
        fGrid.append(fRow)        
    return fGrid


def gen_Open_List(item):    
    hp.heappush(openList, item)    
    return openList

openList = []
closedList = []  # Initialize open and closed list
def algoAstar(maze):
    
    startX = 0
    startY = 0
    currentX = startX # Make the start vertex current 
    currentY = startY
    # Calculate heuristic distance of start vertex to destination (h)
    # Calculate f value for start vertex (f = g + h)
  
    """minCost = hp.heappop(openList)"""
    targetX = targetY = len(maze)- 1
    
    while (currentX != targetX and currentY != targetY): #while current vertex is not the destination
        # For each vertex adjacent to current
            # If vertex not in closed list and not in open list then
                # Add vertex to open list
                # Calculate distance from start (g)
                # Calculate heuristic distance to destination (h)
                # Calculate f value (f = g + h)
                # If new f value < existing f value or there is no existing f value then
                    # update f value
                    # set parent to be the current index
                # End IF
            # End IF
        # Next adjecent
        
        eastX = currentX + 1
        eastY = currentY
        northX = currentX
        northY = currentY + 1
        westX = currentX - 1
        westY = currentY 
        southX = currentX   
        southY = currentY - 1
    
        adj_block_X = [eastX, northX, westX, southX]
        adj_block_Y = [eastY, northY, westY, southY]
        
        for (x, y) in zip(adj_block_X, adj_block_X):
            if maze[x][y] == 1:            # out of range write if it is valid    
                coordinates = str(x) + "," + str(y)
                if coordinates not in openList and closedList:
                    openList.append(coordinates)  
                    upd_G_Val(x, y, currentX, currentY)
                    cal_F_Val()
        currCoordinates = str(currentX) + "," + str(currentY)
        closedList.append(currCoordinates)
        
        
        print("maze value with coordinates " + "("+ str(eastX)+ "," +str(eastX)+ ") is: ", maze[eastX][eastY])
        
        '''if maze[eastX][eastY] == 1:
            openList.append(eastX:eastY)
        if maze[northX][northY] == 1:
            openlist.append([northX][northY])'''
          

a= Maze()
maze_gen = a.makeMaze(5)
#print(maze_gen)
maze_H = cal_H_Val()
#print(maze_H)
maze_G = cal_G_Val()
#print(maze_G)
#print(cal_F_Val(maze_H, maze_G))
algoAstar(maze_gen)
