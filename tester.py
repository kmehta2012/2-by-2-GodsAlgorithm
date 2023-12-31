from Cube import *
import copy
"""
Testing all the moves on a sample cube state.

6 Test cases - one for each move (F, F', L, L', U, U')
"""
totalTests = 0
passedTests = 0

def printCube(cube):
    j = 0
    for i in cube:
        if(j % 3 == 0):
            print("\n")
        print(i)
        j += 1


cube = ('y', 'g', 'r', 
        'r', 'w', 'g',
        'y', 'b', 'r',
        'g', 'o', 'w',
        'r', 'b', 'w',
        'w', 'o', 'b',
        'o', 'g', 'y',
        'b', 'y', 'o')

originalCube = copy.deepcopy(cube)
cube = Cube(cube)

#Test A: Front clockwise

totalTests += 1
cube.state = cube.applyMove(F)
resultantState =         ('y', 'r', 'b',
                          'y', 'r', 'g',
                          'g', 'w', 'o',
                          'r', 'g', 'w',
                          'r', 'b', 'w', #Back cubies unchanged
                          'w', 'o', 'b',
                          'o', 'g', 'y',
                          'b', 'y', 'o')

if cube.state == resultantState:
    print("Front Clockwise Test Passed")
    passedTests += 1
else:
    print("Front Clockwise Test Failed")



#Test B: Front Counter Clockwise

totalTests += 1
cube.state = cube.applyInverseMove(F)
if cube.state == originalCube:
    print("Front Counter Clockwise test passed \n")
    passedTests += 1
else:
    print("Front Counter Clockwise test failed \n")

#Test C:  Left Clockwise

totalTests += 1
cube.state = cube.applyMove(L)
resultantState = ('y', 'g', 'r',
                 'r', 'w', 'g',
                 'g', 'o', 'y',
                 'b', 'y', 'r',
                 'r', 'b', 'w',
                 'w', 'o', 'b', 
                 'y', 'b', 'o',
                 'o', 'g', 'w')

if cube.state == resultantState:
    print("Left Clockwise Test Passed")
    passedTests += 1
else:
    print("Left Clockwise Test Failed")

#Test D: Left Counter Clockwise

totalTests += 1
cube.state = cube.applyInverseMove(L)
if cube.state == originalCube:
    print("Left Counter Clockwise test passed \n")
    passedTests += 1
else:
    print("Left Counter Clockwise test failed \n")

#Test E: Up Clockwise

totalTests += 1
cube.state = cube.applyMove(U)
resultantState = ('w', 'b', 'r', 
                 'r', 'w', 'g',
                 'r', 'g', 'y',
                 'g', 'o', 'w', 
                 'y', 'g', 'o', 
                 'w', 'o', 'b', 
                 'r', 'b', 'y',
                 'b', 'y', 'o')

if cube.state == resultantState:
    print("Up Clockwise Test Passed")
    passedTests += 1
else:
    print("Up Clockwise Test Failed")

printCube(cube.state)

#Test F: Up Counter Clockwise

totalTests += 1
cube.state = cube.applyInverseMove(U)
if cube.state == originalCube:
    print("Up Counter Clockwise test passed \n")
    passedTests += 1
else:
    print("Up Counter Clockwise test failed \n")

#---------- RESULTS --------------------------------#
print(f"Tests passed: {passedTests} OUT OF {totalTests}")
