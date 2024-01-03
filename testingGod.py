import GodsAlgorithm as ga
from Cube import Cube
from math import inf

initialState = ('y', 'o', 'g',
                'b', 'r', 'y',
                'g', 'w', 'o',
                'b', 'w', 'o',
                'w', 'r', 'b',
                'y', 'g', 'r',
                'o', 'y', 'b',
                'g', 'r', 'w') 

# Logic for solvedState : 
"""
Logic figuring out the solved state configuration:

- My program uses the clockwise and anticlockwise moves for left, Up, Front. 

-This means that the cubie on the back-down-right
 position NEVER gets changed. 

- Before the user inputs their cube, I ask them to orient the cube in a way so that the yellow - green - red cubie is the back - down - red cubie, 
  with the green sticker in the down position.

- Since this cubie is unchanged irrespective of the moves, this means that in the solved state: 
  1. the BACK side is: yellow
  2. the DOWN side is: green
  3. the RIGHT side is: red

  white opposes yellow, orange opposes red, and green opposes blue, it follows that:
  4. the FRONT side is: white
  5. the UP side is: blue
  6. the LEFT side is: orange

"""

solvedState = ('w', 'b', 'r',
               'w', 'g', 'r',
               'w', 'b', 'o',
               'w', 'g', 'o',
               'y', 'b', 'r',
               'y', 'g', 'r',
               'y', 'b', 'o',
               'y', 'g', 'o',
            ) 


"""
moveNumer is the 3rd parameter in the value parameter list in the adjList. For any key value (Cube State) in the adjList, it represents 
the number of moves required to go from initialState(or the solved state in solvedAdjList) to that key value.

Logic - match with the current Key moveNumber parameter + 1
"""

initialAdjList = {initialState : [None, None, 0]} # FORMAT - { State : [predecessor, Move that gets me from predecessor to State, moveNumber] }
solvedAdjList = {solvedState : [None, None, 0]}

initialConfigGraph = ga.Graph(initialAdjList, [initialState], 0) 
solvedConfigGraph = ga.Graph(solvedAdjList, [solvedState], 0)

initialCube = Cube(initialState)
solvedCube = Cube(solvedState)

optimalMoves = inf
optimalCommonState = None

#Quick fix for printing the inverse moves for the optimalCommonState -> Solved State direction. There's definetly a better way of doing 
# this, let's see later.

oppositeMoves = {"F" : "F'", "L" : "L'", "U" : "U'", "F'" : "F", "L'" : "L", "U'" : "U"} 


while True:

    commonStates = set(initialConfigGraph.adjacency_list) & set(solvedConfigGraph.adjacency_list)
    
    if commonStates:
      for i in commonStates:
        optimalMoves = min(optimalMoves, initialConfigGraph.adjacency_list[i][2] + solvedConfigGraph.adjacency_list[i][2])
        if optimalMoves == initialConfigGraph.adjacency_list[i][2] + solvedConfigGraph.adjacency_list[i][2]:
          optimalCommonState = i
      break

    initialKey = initialConfigGraph.bfsQueue.pop(0)
    solvedKey = solvedConfigGraph.bfsQueue.pop(0)

    initialCube.state = initialKey
    solvedCube.state = solvedKey

    initialConfigGraph.moveNumber = initialConfigGraph.adjacency_list[initialKey][2] + 1
    solvedConfigGraph.moveNumber = solvedConfigGraph.adjacency_list[solvedKey][2] + 1

    initialConfigGraph.add_neighbours(initialCube)
    solvedConfigGraph.add_neighbours(solvedCube)

solution = []
currentState = optimalCommonState
while True:
  if currentState == initialState: #WE HAVE REACHED THE INITIAL STATE; this is (probably) the inefficient way to do this
    break
  solution.insert(0, initialConfigGraph.adjacency_list[currentState][1])
  currentState = initialConfigGraph.adjacency_list[currentState][0]

  

currentState = optimalCommonState
while True:
  if currentState == solvedState: #WE HAVE REACHED THE SOLVED STATE; this is (probably) the inefficient way to do this
    break
  solution.append(oppositeMoves[solvedConfigGraph.adjacency_list[currentState][1]])
  currentState = solvedConfigGraph.adjacency_list[currentState][0]

  
print(f"Total moves : {optimalMoves}")
j = 1
for i in solution:
  print(f"{j}. {i}")
  j += 1


  

  
  



"""
while ga.bfsQueue:
    
    key = ga.bfsQueue.pop(0)
    pocketCube.state = key
    ga.moveNumber = configGraph.adjacency_list[key][2] + 1
    print(ga.moveNumber)
    if(ga.moveNumber == 15):
        break
    configGraph.add_neighbours(pocketCube)
"""

