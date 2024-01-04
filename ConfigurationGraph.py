
from Cube import moves, inverseMoves


"""
Core idea - I'm growing the graph and doing a BFS on it at the same time - in the same DS. 
"""
#Class rep of a graph

def printAdjList(adjList):
    for key, value in adjList.items():
        print(f"State : {key} \nPredecessor: {value[0]}\nMove: {value[1]}\nShortest Path Length: {value[2]} \n")

class ConfigurationGraph:
    def __init__(self, adjList, bfsQueue, moveNumber = 0):
        self.adjacency_list = adjList
        self.bfsQueue = bfsQueue
        self.moveNumber = moveNumber

    def add_neighbours(self, cube):
        """
        Uses BFS to explore cube.state. Adds all neighbours to the adj list (which is also the BFS queue) that does not exist in the graph
        yet.

        Efficiency issue #1: Don't need to do calculate the (inverse) anticlockwise move for a clockwise config and vice versa
        """
        # Add a new cube state to the graph - if the state isn't in the graph yet

        #Clockwise moves
        for i in moves: # i are the KEYS
            key = cube.applyMove(i)
            if self.adjacency_list.get(key, None) is None: #if the state does not exist in graph, then I add it. I think None is a decent choice, since the value is always a list
                self.adjacency_list[key] = [cube.state, moves[i], self.moveNumber] #using ID for increasing readability while I test. Can change it later
                self.bfsQueue.append(key)
    
        #Anticlockwise moves
        for i in inverseMoves: # i are the KEYS
            key = cube.applyInverseMove(i)
            if self.adjacency_list.get(key, None) is None: 
                self.adjacency_list[key] = [cube.state, inverseMoves[i], self.moveNumber]
                self.bfsQueue.append(key)
            

