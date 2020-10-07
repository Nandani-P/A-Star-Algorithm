from maze import *
import itertools
import heapq as hp

hGrid =[]
def initiateGrid():
    global hGrid, gGrid, fGrid
    
    for row in maze_gen:
        hRow = []
        for block in row:   
            hRow.append(None)
        hGrid.append(hRow)
        
    gGrid = hGrid[:]
    fGrid = hGrid[:]
    print("G grid: ", gGrid)

def upd_H_Val(x, y):
    hValue = (targetX - x) + (targetY - y)
    hGrid[x][y] = hValue
    return hValue    
 
def upd_G_Val(x, y, curX, curY):
    print("Inside g value fun, G grid: ", gGrid)
    print("Inside update g value function, current g value: ", gGrid[curX][curY])
    newGValue = gGrid[curX][curY] + 1
    print("Inside update g value function, new g value: ", newGValue)
    if (gGrid[x][y] is None) or (gGrid[x][y] > newGValue) :
        gGrid[x][y] = newGValue
    return newGValue    

def upd_F_Val(x, y, fVal):
    fGrid[x][y] = fVal

openList = []
closedList = []

def algoAstar(maze):   
    startX = 0
    startY = 0
    currentX = startX 
    currentY = startY   
    hVal = upd_H_Val(currentX, currentY)
    gGrid[0][0]= 0
    print("---------------------------------------------")
    print("G grid inside algo: ", gGrid)
    fVal = hVal + 0
    upd_F_Val(currentX, currentY, fVal)

    currentVertex = [currentX, currentY]
    hp.heappush(openList, (fVal, currentVertex))
    
    while (currentX != targetX and currentY != targetY): #while current vertex is not the destination       
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
            if x > 0 and y > 0 and x <= targetX and y <= targetY:
                
                if maze[x][y] == 1:
                    print("Maze: ", maze)
                    coordinates = [x, y]
                    print("Adj Coordinates: ", coordinates)
                    gVal = upd_G_Val(x, y, currentX, currentY)
                    print("currentVertex", currentVertex)
                    print("G Value: ", gVal)
                    hVal = upd_H_Val(x, y)
                    print("H Value: ", hVal)
                    fVal = gVal + hVal
                    if (fVal < fGrid[x][y]) or (fGrid[x][y] is None):
                        print("F VAlue: ", fVal)
                        upd_F_Val(x, y, fVal)
                        preVertex = dict(zip(coordinates, currentVertex))
                                        
                    currentTuple = (fVal, coordinates)
                    if currentTuple not in openList and closedList:
                        hp.heappush(openList, (fVal, coordinates))
                   
        hp.heappush(closedList, currentVertex)
        currentTuple = hp.heappop(openList)
        currentX = currentTuple[1][0]
        currentY = currentTuple[1][1]
    

a= Maze()
maze_gen = a.makeMaze(10)
targetX = targetY = len(maze_gen)- 1
#print(maze_gen)
initiateGrid()

#hValue = cal_H_Val(0, 1)
algoAstar(maze_gen)

print("H value Grid: ", hGrid)
print("G value Grid: ", gGrid)
print("F value Grid: ", fGrid)
