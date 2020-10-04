from random import randrange, shuffle
import json
class Maze(object):
    
    """def makeMaze(self, dimension):
                
        for x in range(dimension):
            row = []
            for y in range(dimension):                  
                row.append(randrange(2))
                
            shuffle(row)
            self.grid.append(row)
        return self.grid"""
    
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
        

    '''def mulGrid(self, num, dimension):
        file = open("gridStore.txt", "w+")
        for i in range(num):
            file.write(str(self.makeMaze(dimension)))
            file.write('\n')
        file.close()

        gridOne = []

        with open('gridStore.txt', 'r') as file:
            for line in file:
                item = line[:-1]
                gridOne.append(item)

   def mulGrid(self, dimension):
        with open('listfile.txt', 'w') as file:
            json.dump(self.makeMaze(dimension), file)

        with open('listfile.txt', 'r') as file:
            basicList = json.load(file)
        print(type(basicList))
        return basicList'''
    
    def mulGrid(self, num, dimension):
        
        with open('listfile.txt', 'w') as file:
            for i in range(num):
                x = json.dumps(self.makeMaze(dimension))
                file.write(x + "\n")
                file.flush()

        with open('listfile.txt', 'r') as file:
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
