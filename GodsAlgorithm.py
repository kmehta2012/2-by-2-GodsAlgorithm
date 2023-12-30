"""
TO - DO

1. efficiency issue of add-vertex
2. Keeping a seperate adjacency list and bfs queue or just one?
3. The key can't be a list. The cube configurations are a list rn - BIGGEST FIX
4. Implement a BFS, config graph for >= 2 iterations
5. Convert into a two way BFS - HARD
6. Done
"""


from math import inf
from Cube import *

"""
Core idea - I'm growing the graph and doing a BFS on it at the same time - in the same DS?
"""
#Class rep of a graph
class Graph:
    def __init__(self, adjList):
        self.adjacency_list = adjList

    def add_vertex(self, cube):
        """
        Major efficiency issue : Don't need to do calculate the (inverse) anticlockwise move for a clockwise config and vice versa
        """
        # Add a new cube configuration to the graph - if the configuration isn't in the graph yet
        initialConfig = cube

        #Clockwise moves
        for i in moves: # i are the KEYS
            cube.applyMove(i) 
            if self.adjacency_list.get(cube, 1): #if the configuration does not exist in graph, then I add it:
                self.adjacency_list[cube] = [initialConfig, moves[i]]
            
            cube.cube = initialConfig
        
        #Anticlockwise moves
        for i in inverseMoves: # i are the KEYS
            cube.applyInverseMove(i) 
            if self.adjacency_list.get(cube.cube, 1): #if the configuration does not exist in graph, then I add it:
                self.adjacency_list[cube.cube] = [initialConfig, inverseMoves[i]]
            
            cube.cube = initialConfig

        


            

            
        

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

    def get_neighbors(self, vertex):
        # Return a list of neighbors for a given vertex
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
initialState = ['y', 'g', 'r', 
                'r', 'w', 'g',
                'y', 'b', 'r',
                'g', 'o', 'w',
                'r', 'b', 'w',
                'w', 'o', 'b',
                'o', 'g', 'y',
                'b', 'y', 'o']

adjList = {initialState : [None, None]} # State : [predecessor, Move that gets me from predecessor to State]
configGraph = Graph(adjList)
pocketCube = Cube(initialState)
configGraph.add_vertex(pocketCube.cube)


"""
adjList =  {'r': ['s', 'v'], 
            's': ['r', 'w'],
            't': ['u', 'w', 'x'],
            'u': ['t', 'x', 'y'],
            'v': ['r'],
            'w': ['s', 't', 'x'],
            'x': ['w', 't', 'u', 'y'],
            'y': ['u', 'x']}

graph = Graph(adjList)


results = graph.bfs('s')
print(results)
"""