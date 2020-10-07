from maze import *
import itertools
import heapq as hp


hGrid =[]
def initiateGrid():
    global hGrid, gGrid, fGrid
    x1 =0
    for row in maze_gen:
        hRow = []
        y1 = 0
        for block in row:   
            hRow.append(None)
            y1 = y1 + 1
        x1 = x1 + 1
        hGrid.append(hRow)
        
    gGrid = hGrid[:]
    fGrid = hGrid[:]

def cal_H_Val(x, y, hValue):
    print(hGrid[x][y])
    hGrid[x][y] = hValue
    return hGrid    
 
def upd_G_Val(x, y, curX, curY):
    newGValue = gGrid[curX][curY] + 1 
    if (gGrid[x][y] is None) or (gGrid[x][y] > newGValue):
        gGrid[x][y] = newGValue
    return newGValue    

def upd_F_Value(g, h, x, y):
    fGrid[x][y] = g + h
    return fGrid[x][y]

def gen_Open_List(item):    
    hp.heappush(openList, item)    
    return openList
##
##openList = []
##closedList = []  
##def algoAstar(maze):   
##    startX = 0
##    startY = 0
##    currentX = startX 
##    currentY = startY   
##    targetX = targetY = len(maze)- 1
##    hCurrent = (targetX - currentX) + (targetY - currentY)
##    cal_H_Val(currentX, currentY, hCurrent)
##    gCurrent = (currentX - startX) + (currentY - startY)
##    gGrid[0][0]= 0
##    
##    while (currentX != targetX and currentY != targetY): #while current vertex is not the destination       
##        eastX = currentX + 1
##        eastY = currentY
##        northX = currentX
##        northY = currentY + 1
##        westX = currentX - 1
##        westY = currentY 
##        southX = currentX   
##        southY = currentY - 1
##        adj_block_X = [eastX, northX, westX, southX]
##        adj_block_Y = [eastY, northY, westY, southY]
##        
##        for (x, y) in zip(adj_block_X, adj_block_X):
##            if maze[x][y] == 1:            # out of range write if it is valid    
##                coordinates = str(x) + "," + str(y)
##                if coordinates not in openList and closedList:
##                    openList.append(coordinates)  
##                    upd_G_Val(x, y, currentX, currentY)
##                    cal_F_Val()
##                    """minCost = hp.heappop(openList)"""
##        currCoordinates = str(currentX) + "," + str(currentY)
##        closedList.append(currCoordinates)        
##        print("maze value with coordinates " + "("+ str(eastX)+ "," +str(eastX)+ ") is: ", maze[eastX][eastY])

a= Maze()
maze_gen = a.makeMaze(5)
#print(maze_gen)
initiateGrid()

##hValue = cal_H_Val(0,0, 8)

#algoAstar(maze_gen)

print("H value Grid: ", len(hGrid))
print("G value Grid: ", gGrid)
print("F value Grid: ", fGrid)
