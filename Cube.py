
"""
This script is going to implement the D.S. required to represent the 3*3*3 cube. The strategy is to use 6 3*3 arrays 
(i.e. 6 * 9 matrix), with each row (array) representing one of the 6 faces of the cube along with its colors

We'll use a python nested List to do so. going to be a global variable because the cube will be accessed in multiple files most prob.
"""

#Order White, Orange, Yellow, Red, Green, Blue
cube = [
    ['','' ,'' , '','W', '', '', '', ''],
    ['','' ,'' , '','O', '', '', '', ''],
    ['','' ,'' , '','Y', '', '', '', ''],
    ['','' ,'' , '','R', '', '', '', ''],
    ['','' ,'' , '','G', '', '', '', ''],
    ['','' ,'' , '','B', '', '', '', ''],
]

def initializeCube() :
    ''

    
#Get a uniformly distributed configuration of the cube among the ~43 quintillion configs (Most prob doesn't do a unif dist tho).
# Do ~21 random moves 
def randomShuffle() :
    ''

