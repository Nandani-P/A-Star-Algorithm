#
# Nandani Patidar & Julian Torres
#
# AI Assignment One - Fall 2020
#
# Implementation of Forward repeated A* algorithm
#


from maze import *
import itertools
import heapq as hp
import copy as cp

hGrid =[]
gGrid = []
fGrid = []

# Initiate H, G and F grids 
def initiateGrid():
    global hGrid, gGrid, fGrid
    
    for row in maze_gen:
        hRow = []
        for block in row:   
            hRow.append(None)
        hGrid.append(hRow)
        
    gGrid = cp.deepcopy(hGrid)
    fGrid = cp.deepcopy(hGrid)
    
# Update H value as we explore adjecent nodes
def upd_H_Val(x, y):                     
    hValue = (targetX - x) + (targetY - y)
    hGrid[x][y] = hValue
    #print("hValue- ", hValue)
    return hValue
 
def upd_G_Val(x, y, curX, curY):
    #print("Inside g value function, G grid: ", gGrid)
    
    newGValue = gGrid[curX][curY] + 1
    if (gGrid[x][y] is None) or (gGrid[x][y] > newGValue) :
        gGrid[x][y] = newGValue 
    return newGValue    

def upd_F_Val(x, y, fVal):
    fGrid[x][y] = fVal

openList = []
closedList = []

def algoAstar(maze):
    global openList, closedList
    preVertex = {}
    startX = 0
    startY = 0
    currentX = startX 
    currentY = startY   
    hVal = upd_H_Val(currentX, currentY)
    gGrid[0][0]= 0
    fVal = hVal + 0
    upd_F_Val(currentX, currentY, fVal)
    currentVertex = [currentX, currentY]
    
    while ( not(currentX == targetX and currentY == targetY)): #while current vertex is not the destination       
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
        currentTuple = (fVal, currentVertex)

        for i in range(4):
            x = adj_block_X[i]
            y = adj_block_Y[i]
            
            if x in range(0, targetX + 1) and y in range(0, targetY + 1):
                coordinates = [x, y]
                print("-------------------------------------------------------------------")
                print("Adj Coordinates before check: ", coordinates)
                print("Closed list : ", closedList)
                print("Open list : ", openList)
                print("Maze (", x, y, ") = ", maze[x][y])
                
                if maze[x][y] == 1:
                    listCoordinates = list(zip(*openList))

                    if (len(listCoordinates) == 0 or coordinates not in listCoordinates[1]) and coordinates not in closedList:
                        
                        print("Current Vertex: ", currentVertex)
                        print("Adj Coordinates: ", coordinates)
                        gVal = upd_G_Val(x, y, currentX, currentY)
                        #print("G Value: ", gVal)
                        #print("G grid: ", gGrid)
                        hVal = upd_H_Val(x, y)
                        #print("H Value: ", hVal)
                        fVal = gVal + hVal
                        upd_F_Val(x, y, fVal)
                        #print("F Value: ", fVal)
                        hp.heappush(openList, (fVal, coordinates))
                        
                        preVertex[tuple(coordinates)] = tuple(currentVertex)                  
                                                            
                    elif len(listCoordinates) > 0 and coordinates in listCoordinates[1]:
                        gVal = upd_G_Val(x, y, currentX, currentY)
                        hVal = upd_H_Val(x, y)
                        fVal = gVal + hVal
                        if fVal < fGrid[x][y]:
                            upd_F_Val(x, y, fVal)
                            hp.heappush(openList, (fVal, coordinates))
                            preVertex[tuple(coordinates)] = tuple(currentVertex)                            
                        
        hp.heappush(closedList, currentVertex)
        if (len(openList) > 0):
            print("Open List", openList)
            currentTuple = hp.heappop(openList)
        else:
            print("No path exists to target.")
            print("Number of nodes expanded in the search : ", len(openList) + len(closedList))
            exit()
        
        currentX = currentTuple[1][0]
        currentY = currentTuple[1][1]
        currentVertex = [currentX, currentY]

    print("Number of nodes expanded in the search : ", len(openList) + len(closedList))       
    pre =()
    target = (targetX, targetY)
    path = [target]
    
    while not(pre == (0, 0)):        
        pre =(preVertex[target])
        path.append(pre)
        target = pre
    return path  

a= Maze()
maze_gen = a.makeMaze(50)
#print(maze_gen)

targetX = targetY = len(maze_gen)- 1

# Calling display function from Maze class by creating an object of Maze()
a.displaySingleMaze(maze_gen)

initiateGrid()

# algoAstar return grid path vertex from start position to destination
path = algoAstar(maze_gen)

# Displaying maze with the shortest path
a.displaySingleMazeWithPath(path, maze_gen)



