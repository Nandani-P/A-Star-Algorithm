#
# Nandani Patidar & Julian Torres
#
# AI Assignment One - Fall 2020
#
# Main
#

from maze import *
from RepeatedBackwardAStar import *
from FinalRepeatedForwardAStar import *
import time
import matplotlib.pyplot as plt
from matplotlib import colors

startTime = time.time()
a= Maze()

maze_gen = a.makeMaze(5)

### Calling display function from Maze class by creating an object of Maze()
##a.displaySingleMaze(maze_gen)
##
##initiateGrid(maze_gen)
##
### algoAstar return grid path vertex from start position to destination
##path = algoAstar(maze_gen)
##
### Displaying maze with the shortest path
##a.displaySingleMazeWithPath(path, maze_gen)

with open('storeMaze.txt', 'r') as file:
      y = file.readlines()
      arryMaze = []
      for i in y:
          listMaze = (json.loads(i))
          arryMaze.append(listMaze)
          
for maze in arryMaze:
   repeatedbackwardAStar(maze)
   
          
##for maze in arryMaze:
##   repeatedforwardAStar(maze)

##cmap = colors.ListedColormap(['Blue','red'])   
##path = repeatedbackwardAStar(maze_gen)
##plt.figure(figsize=(10, 9), dpi=70)
##plt.imshow(maze_gen)
###plt.pcolor(path[::-1],cmap=cmap,edgecolors='k', linewidths=3)
##plt.show()



print("Time to execute the all programs is %s seconds" % (time.time() - startTime))

##maze = [[1, 1, 0, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 1, 0, 0, 1]]   
