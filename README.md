# AI Project - Fall 2020
# Date - 10/12/2020

# Team - Nandani Patidar & Julian Torres
# Email - nandani.patidar@rutgers.edu & jlntorres8@gmail.com
# GitHub link - https://github.com/Nandani-cloud/AI-Project-One.git


The project contains 4 executable files: -

1. main.py
2. FinalRepeatedForwardAStar.py
3. RepeatedBackwardAStar.py
4. AdaptiveAStar.py
5. maze.py
--------------------------------------------------------------------------------------------------------------------------------------------------------------
1. main.py 
To run using the command line: -
cd "path of folder which contains these files"
To run backward A* type: python main.py backward
To run forward A* type: python main.py forward
To run adaptive A* type: python main.py adaptive

It calls storeMultiGrid function with parameters as (50, 101) and store mazes in a text file.
Then it reads from text file and store mazes in a list and iterate the list to call A*.
Then it calls forward, backward and adaptive A* algorithm function.  
---------------------------------------------------------------------------------------------------------------------------------------------------------------
2. FinalRepeatedForwardAStar.py

To run with smaller and larger g value:
>> Go to computePath() fuction:
>> In the end of computePath fuction - By default smaller g value condition is set


                # Open list with smaller g value implementation
                hp.heappush(openList, (fVal, gVal, (x, y)))

                # Openlist with larger g value implementation
                #hp.heappush(openList, (fVal, -gVal, (x, y)))

>> To change the conditon for larger g value - comment/uncomment for smaller/larger g value

To display maze using ascii values please uncomment line number: 113, 228, 165 
line 113: displays maze with obstacles
line 228: displays maze with agent movement from start to goal 
line 165: displays agent movement in case there is no path

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
3. RepeatedBackwardAStar.py
To display maze using ascii values please uncomment line number: 104, 214, 164 
line 104: displays maze with obstacles
line 214: displays maze with agent movement from start to goal 
line 158: displays agent movement in case there is no path

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
4. AdaptiveAStar.py
To display maze using ascii values please uncomment line number: 107, 233, 160 
line 107: displays maze with obstacles
line 233: displays maze with agent movement from start to goal 
line 160: displays agent movement in case there is no path
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

5. maze.py

This class is used to:
>>Generate grid enviornments.
>>To display various state of the agent.
>>To store mazes in a text file 
>>To read mazes from the text file
