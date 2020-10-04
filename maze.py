#
# Author: Nandani Patidar
#
# AI Project One
#

from random import randrange, shuffle
import json
class Maze(object):    
    
    def makeMaze(self, dimension):
        grid = []        
        for x in range(dimension):
            row = []
            for y in range(dimension):                  
                if randrange(10) < 7:  
                    row.append(1)
                else:
                    row.append(0)
                
            shuffle(row)
            grid.append(row)
        return grid

         
        
    def displayMaze(self, arryMaze):      
        for a in arryMaze:
            counter =0
            for i in a:
                c = 0
                for j in i:
                    if j ==1:
                        i[c] = " "
                    else:
                        i[c] = "X"
                    c = c + 1
                res = ' | '.join(map(str, a[counter]))
                print("---------------------")
                print( "| " + res + " |")
                counter = counter + 1
            print("---------------------")
        
    
    def mulGrid(self, num, dimension):
        
        with open('storeMaze.txt', 'w') as file:
            for i in range(num):
                x = json.dumps(self.makeMaze(dimension))
                file.write(x + "\n")
                file.flush()

        with open('storeMaze.txt', 'r') as file:
            y = file.readlines()
            arryMaze = []
            for i in y:
                listMaze = (json.loads(i))
                arryMaze.append(listMaze)
        return arryMaze
                
                
        
a = Maze()    
#a.makeMaze(5, 5)
#a.mulGrid(5, 5)
a.displayMaze(a.mulGrid(5, 5))
