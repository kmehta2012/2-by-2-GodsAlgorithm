from GodsAlgorithm import *
#The following is just 2 quarter twists away from a solved configuration (L' L')
# I'm gonna print out all all reachable configurations in 2 quarter twists (via BFS) to see if my implementation indeed works or not
initialState = ('w', 'g', 'o', 
                'w', 'b', 'o',
                'y', 'b', 'r',
                'y', 'g', 'r',
                'y', 'g', 'o',
                'y', 'b', 'o',
                'w', 'b', 'r',
                'w', 'g', 'r')

solvedState = None #NEED TO FIGURE THIS SHIT OUT
"""
moveNumer is the 3rd parameter in the value parameter list in the adjList. For any key value (Cube State) in the adjList, it represents 
the number of moves required to go from initialState to that key value.

Logic - match with the current Key moveNumber parameter + 1

This parameter is arguably not needed - but it doesn't hurt to have it. Besides helps me in testing and debugging.
"""
initialBfsNode = initialState #Represents the current node in the BFS queue that we're exploring (initial -> solved direcion)
solvedBfsNode = solvedState  #Represents the current node in the BFS queue that we're exploring (solved -> initial direction)

adjList = {initialState : [None, None, moveNumber]} # FORMAT - { State : [predecessor, Move that gets me from predecessor to State, moveNumber] }
configGraph = Graph(adjList) #Also acts as BFS queue in the initial -> solved direction
pocketCube = Cube(initialState)

for key, value in list(configGraph.adjacency_list.items()):
    pocketCube.state = key
    moveNumber = value[2] + 1
    if(moveNumber == 3):
        break
    configGraph.add_neighbours(pocketCube)

print(moveNumber)
printAdjList(configGraph.adjacency_list)
