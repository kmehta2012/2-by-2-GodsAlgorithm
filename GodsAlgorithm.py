"""
TO - DO

1. efficiency issue of add-vertex
2. Keeping a seperate adjacency list and bfs queue or just one?
3. The key can't be a list. The cube states are a list rn - BIGGEST FIX
4. Implement a BFS, config graph for >= 2 iterations
5. Depending on how to user does this - what'll the solved state of the cube like (like what cube will be at FUR pos ....)
5. Convert into a two way BFS - HARD
6. 
"""


from math import inf
from Cube import *

moveNumber = 0

"""
Core idea - I'm growing the graph and doing a BFS on it at the same time - in the same DS. 
"""
#Class rep of a graph

def printAdjList(adjList):
    for key, value in adjList.items():
        print(f"State : {key} \nPredecessor: {value[0]}\nMove: {value[1]}\nShortest Path Length: {value[2]} \n")

class Graph:
    def __init__(self, adjList):
        self.adjacency_list = adjList

    def add_neighbours(self, cube):
        """
        Uses BFS to explore cube.state. Adds all neighbours to the adj list (which is also the BFS queue) that does not exist in the graph
        yet.

        Major efficiency issue #1: Don't need to do calculate the (inverse) anticlockwise move for a clockwise config and vice versa

        MAJOR EFFICIENY ISSUE #2 (MORE important): I'm always casting the cube state (which is a list) to a tuple so that I can use it 
        as the state . THIS IS (VERY ?)INEFFICIENT. I can maybe represent the state as a tuple from the get-go but that does NOT seem to 
        solve the problem. Let's see. 
        """
        # Add a new cube state to the graph - if the state isn't in the graph yet
        #initialState = copy.deepcopy(cube.state)

        #Clockwise moves
        for i in moves: # i are the KEYS
            key = cube.applyMove(i)
            if self.adjacency_list.get(key, None) is None: #if the state does not exist in graph, then I add it. I think None is a decent choice, since the value is always a list
                self.adjacency_list[key] = [cube.state, moves[i], moveNumber] #using ID for increasing readability while I test. Can change it later
        
        #Anticlockwise moves
        for i in inverseMoves: # i are the KEYS
            key = cube.applyInverseMove(i)
            if self.adjacency_list.get(key, None) is None: 
                self.adjacency_list[key] = [cube.state, inverseMoves[i], moveNumber]
            
    def add_edge(self, from_vertex, to_vertex, weight=None):
        # Add an edge between two vertices in the graph
        pass

    def remove_vertex(self, vertex):
        # Remove a vertex and all its associated edges from the graph
        pass

    def remove_edge(self, from_vertex, to_vertex):
        # Remove an edge between two vertices from the graph
        pass

    def get_vertices(self):
        # Return a list of all vertices in the graph
        pass

    def get_neighbors(self, state):
        pass
        

    def is_adjacent(self, from_vertex, to_vertex):
        # Check if there is an edge between two vertices
        pass

    def __str__(self):
        # Return a string representation of the graph
        pass
    
    def bfs(self, source):
        #bfs to solve the single source shortest path problem for the source vertex passed by the user
        shortestPath = {}
        predecessor = {}
        queue = []
        
        for vertex in self.adjacency_list:
            shortestPath[vertex] = inf
            predecessor[vertex] = None
        
        shortestPath[source] = 0
        queue.append(source)

        while queue:
           print(queue)
           vertex = queue.pop(0)
           for i in self.adjacency_list[vertex]:
                if shortestPath[i] == inf:
                    shortestPath[i] = shortestPath[vertex] + 1
                    queue.append(i)
                    predecessor[i] = vertex
        
        return shortestPath, predecessor




#main
"""
initialState = ('y', 'g', 'r', 
                'r', 'w', 'g',
                'y', 'b', 'r',
                'g', 'o', 'w',
                'r', 'b', 'w',
                'w', 'o', 'b',
                'o', 'g', 'y',
                'b', 'y', 'o')

solvedState = None #NEED TO FIGURE THIS SHIT OUT
moveNumber = 0 
"""

"""
moveNumer is the 3rd parameter in the value parameter list in the adjList. For any key value (Cube State) in the adjList, it represents 
the number of moves required to go from initialState to that key value.

Logic - Everytime add_neighbours function is called, we increment moveNumber by 1.

This parameter is arguably not needed - but it doesn't hurt to have it. Besides helps me in testing and debugging.
"""

"""
initialBfsNode = initialState #Represents the current node in the BFS queue that we're exploring (initial -> solved direcion)
solvedBfsNode = solvedState  #Represents the current node in the BFS queue that we're exploring (solved -> initial direction)

adjList = {initialState : [None, None, moveNumber]} # FORMAT - { State : [predecessor, Move that gets me from predecessor to State, moveNumber] }
configGraph = Graph(adjList) #Also acts as BFS queue in the initial -> solved direction
pocketCube = Cube(initialState)
moveNumber += 1
configGraph.add_neighbours(pocketCube)
printAdjList(configGraph.adjacency_list)
"""
