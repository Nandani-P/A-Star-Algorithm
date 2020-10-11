#
# Nandani Patidar & Julian Torres
#
# AI Assignment One - Fall 2020
#
# Main
#

from maze import *
from RepeatedForwardAStarFirst import *
import time

startTime = time.time()
a= Maze()
maze_gen = a.makeMaze(5)

# Calling display function from Maze class by creating an object of Maze()
a.displaySingleMaze(maze_gen)

initiateGrid(maze_gen)

# algoAstar return grid path vertex from start position to destination
path = algoAstar(maze_gen)

# Displaying maze with the shortest path
a.displaySingleMazeWithPath(path, maze_gen)


print("Time to execute the program is %s seconds" % (time.time() - startTime))
