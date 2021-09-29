#
# Nandani Patidar & Julian Torres
#
# AI Assignment One - Fall 2020
#
# Main
#

from maze import *
from RepeatedBackwardAStar import *
from RepeatedForwardAStar import *
from AdaptiveAStar import *
import time
import matplotlib.pyplot as plt
from matplotlib import colors
import sys


arg = sys.argv[1]
print ("This is %s A*" % (arg))

startTime = time.time()

a= Maze()

# Calling the function to generate 50 mazes of dimension 101*101 and load mazes in the .txt file
a.storeMulGrid(50, 101)

## Getting 50 mazes of 101*101 from storeMaze.txt file
arryMaze = a.getMazesFromFile()

if arg == "backward":
    
    # Iterating 50 mazes of 101*101 from arryMaze and calling Backward A star
    count = 1
    for maze in arryMaze:
        
        print("Maze : ", count)
        path = repeatedbackwardAStar(maze)
        print("Number of moves done by the agent: ", len(path))
        print("----------------------------------------------------------------------------------")
        count = count + 1
 
                                    ##   print("Travelled cells by the agent: ", path)
    

if arg == "forward":
    
    # Iterating 50 mazes of 101*101 from arryMaze and calling Forward A star
    count = 1
    for maze in arryMaze:
        
        print("Maze : ", count)
        path = repeatedforwardAStar(maze)
        print("Number of moves done by the agent: ", len(path))
        print("----------------------------------------------------------------------------------")
        count = count + 1
 
                                ##   print("Travelled cells by the agent: ", path)


if arg == "adaptive":
    
    # Iterating 50 mazes of 101*101 from arryMaze and calling Adaptive A star
    count = 1
    for maze in arryMaze:
        
        print("Maze : ", count)
        path = adaptiveAStar(maze)
        print("Number of moves done by the agent: ", len(path))
        print("----------------------------------------------------------------------------------")
        count = count + 1
                              ##   print("Travelled cells by the agent: ", path)


   
### Displaying a maze using matplotlib library
##for maze in arryMaze:
##    path = repeatedbackwardAStar(maze)
##    for i in path:
##         maze[i[0]][i[1]] = 2                                   
##    plt.figure(figsize=(10, 9), dpi=70)              # Reference https://stackoverflow.com/questions/52566969/python-mapping-a-2d-array-to-a-grid-with-pyplot  plt.imshow(maze)
##    plt.show()


    
print("Time to execute the all programs is %s seconds" % (time.time() - startTime))

