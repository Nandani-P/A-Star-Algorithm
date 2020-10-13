#
# Nandani Patidar & Julian Torres
#
# AI assignment One - FAll 2020
#
# Generate, display and store Maze
#

from random import randrange, shuffle
import json
import copy as cp

class Maze(object):    

    # Create a two dimentional array of dimension dimension*dimension
    def makeMaze(self, dimension):
        grid = []        
        for x in range(dimension):
            row = []
            for y in range(dimension):                  
                if randrange(10) < 7:  # Marking 70% grid unblocked
                    row.append(1)       # 1 for unblocked block in the grid
                else:
                    row.append(0)       # 0 for blocked block in the grid                
            grid.append(row)
        grid[0][0] = 1
        grid[dimension-1][dimension-1] = 1
        
        return grid

    # display multiple Mazes by passing an array of Mazes 
    def displayMaze(self, arryMaze):      
        for a in arryMaze:
            counter =0
            for i in a:
                c = 0
                for j in i:
                    if j ==1:
                        i[c] = " "
                    else:
                        i[c] = "█"
                    c = c + 1
                res = ' | '.join(map(str, a[counter]))
                print("----" *len(arryMaze))
                print( "| " + res + " |")
                counter = counter + 1
            print("----"*len(arryMaze))
            
    # Dispalys single maze with obstacles
    def displaySingleMaze(self, Maze):
        dpMaze = cp.deepcopy(Maze)
        counter = 0
        for i in dpMaze:
            c = 0
            for j in i:
                if j == 1:
                    i[c] = " "
                elif j == 2:
                    i[c] = "*"
                else:
                    i[c] = "█"
                c = c + 1
            res = '|'.join(map(str, dpMaze[counter]))
            print("--"*len(dpMaze))
            print( "|" + res + "|")
            counter = counter + 1
        print("--"*len(dpMaze))
        return dpMaze

    # this function displays grid with path from start to destination 
    def displaySingleMazeWithPath(self, path, maze): 
        dpMaze = cp.deepcopy(maze)
        for i in path:
            x = i[0]
            y = i[1]
            dpMaze[x][y] = 2
        a.displaySingleMaze(dpMaze)
             
    # function to generate multiple grids
    # source of json: https://www.w3schools.com/python/python_json.asp
    def storeMulGrid(self, num, dimension):                   
        with open('storeMaze.txt', 'w') as file:
            for i in range(num):
                x = json.dumps(self.makeMaze(dimension))    
                file.write(x + "\n")
                file.flush()
                
    # function to get the array of mazes stored in the file            
    def getMazesFromFile(self):
        with open('storeMaze.txt', 'r') as file:
            y = file.readlines()
            arryMaze = []
            for i in y:
                listMaze = (json.loads(i))
                arryMaze.append(listMaze)
        return arryMaze               
        
a = Maze()    
#a.makeMaze(5)
#a.storeMulGrid(50, 101)
#a.displayMaze(a.mulGrid(5, 5))
#a.displaySingleMaze(a.makeMaze(5))
