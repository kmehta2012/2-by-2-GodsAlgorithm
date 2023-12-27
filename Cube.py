"""
This script is going to implement the D.S. required to represent the 2*2*2 cube. 

To-Do:
1. How is this associating colors to each cubie
2. Actually implement the moves
3. User-input
"""
import copy
# 6 colors: Blue, Green, Orange, Red, White, Yellow 

"""
How to associate color with the stickers?
    Idea #1
        Create a class called sticker with value and color parameter and make all these sticker variables instances of the class
    
    Idea #2

"""

# (Front/Back) F/B, (Up/Down) U/D, (Right/Left) R/L

#Front Up right cubie
FUR = 0 
URF = 1 
RUF = 2

#Front Down Right cubie
FDR = 3 
DFR = 4 
RFD = 5 

#Front Up Left cubie
FUL = 6 
ULF = 7 
LUF = 8      

#Front Down Left Cubie
FDL = 9 
DFL = 10 
LFD = 11  

#Back Up Right Cubie
BUR = 12 
URB = 13 
RUB = 14  

#Back Down Right Cubie
BDR = 15 
DRB = 16 
RDB = 17 

#Back Up Left Cubie
BUL = 18 
ULB = 19 
LUB = 20  

#Back Down Left Cubie
BDL = 21 
DLB = 22 
LDB = 23

'''
    There are some symmetries within the moves, which reduce the number of moves from 12 to 6

    front clockwise rotation  = back counter-clockwise rotation
    front counter-clockwise = back clockwise rotation

    left clockwise rotation = right counter-clockwise rotation
    left counter clockwise rotation = right counter-clockwise rotation

    Up clockwise rotation = down counter-clockwise rotation
    Up counter-clockwise rotation = down clockwise rotation

    Because of these symmetries we only need to implement 6 moves on the cube. 
    We choose to implement front, left, and Up moves in both directions
'''

#F - Singmaster notation fron Front Clockwise
'''
(We're only concerned about front cubies here so omitting front, back here)
Up left cubie -> Up right cubie
    fur = ful
    ufr = LUF
    rfu = ufl

    Up right cubie -> Down right cubie:
    fdr = fur
    dfr = ruf
    rdf = urf

Down left cubie -> Up left cubie
    ful = fdl
    ulf = lfd
    lfu = dfl

    Down right cubie -> Down left cubie
    fdl = fdr
    dfl = rdf
    ldf = drf
'''
F = [FUL, LUF, ULF, 
    FUR, RUF, URF, 
    FDL, LFD, DFL,
    FDR, RFD, DFR, 
    BUR, URB, RUB,  # Down cubie unchanged
    BDR, DRB, RDB,  # ""
    BUL, ULB, LUB,  # ""
    BDL, DLB, LDB ] # ""


#F' - Front Counter clockwise
"""
This is just the inverse of front clock wise - is there an easy way to compute the inverse of a permutation?
"""


#L - Left Clockwise
'''
Back Up left cubie -> Front Up Left cubie
FUL = ULB
ULF = BUL
LUF = LUB

Front Up left cubie -> Front Down Left Cubie
FDL = ULF
DFL = FUL
LFD = LUF    

Front Down Left Cubie -> Back Down Left Cubie
BDL = DFL
DLB = FDL
LDB = LFD 

Back Down Left Cubie -> Back Up Left Cubie
BUL = DLB
ULB = BDL
LUB = LDB   
'''

L = [   FUR, URF, RUF, #Front Up Right cubie unchanged
        FDR, DFR, RFD, #Front Down Right cubie unchanged
        ULB, BUL, LUB, 
        ULF, FUL, LUF,
        BUR, URB, RUB, #Back Up Right cubie unchanged
        BDR, DRB, RDB, #Back Down Right cubie unchanged
        DLB, BDL, LDB,
        DFL, FDL, LFD
        ]

#L' - Left Counter Clockwise
"""
This is just the inverse of leftClockwise
"""
pass

#U - Up Clockwise
"""
Back Up Right Cubie -> Front Up Right Cubie
    FUR = RUB
    URF = URB
    RUF = BUR

Front Up Right Cubie -> Front Up Left Cubie
    FUL = RUF
    ULF = URF
    LUF = FUR

Front Up Left Cubie -> Back Up Left Cubie
    BUL = LUF
    ULB = ULF
    LUB = FUL

Back Up Left Cubie -> Back Up Right Cubie
    BUR = LUB
    URB = ULB
    RUB = BUL

"""
U =    [RUB, URB, BUR, 
        FDR, DFR, RFD, #Front Down Right Cubie unchanged
        RUF, URF, FUR, 
        FDL, DFL, LFD, #Front Down Left Cubie unchanged
        LUB, ULB, BUL, 
        BDR, DRB, RDB, #Back Down Right Cubie unchanged
        LUF, ULF, FUL,
        BDL, DLB, LDB ] #Back Down Left Cubie unchanged


# U'
"""
inverse of UpClockwise
"""

class Cube:
    '''
    ENCODING OF THE CUBE
    note: The idea of the encoding has been shamelessly copied from MIT 6.006 FA2011 Recitation 16.
    Here's an explanation of the encoding that we're using:

    The entire cube is 8 cubies with each cubie having 3 colors (stickers). Therefore there are 
    24 stickers in total. To represent a cube we can thus use an array of size 24, with each index 
    representing a sticker.

    for example, from the POV of the person holding the cube, the cubie on the (front, up, right)
    has three stickers. We represent each sticker on that cubie as follows:

    There is one sticker on the front position, one on up position, and one on right position.

    
    [frontUpRight, UpRightFront, RightUpFront, FrontdownRight, downFrontRight, RightFrontdown,
     frontUpLeft, UpLeftFront, LeftUpFront, FrontdownLeft, downFrontLeft, LeftFrontdown,
     backUpRight, UpRightBack, RightdownBack, backdownRight, downRightBack, RightdownBack, 
     backUpLeft, UpLeftBack, LeftdownBack, backdownLeft, downLeftBack, LeftdownBack]

    '''

    def __init__(self, cube):
        self.cube = cube

    #Shuffle the cube randomly n times (under the QTM)
    def shuffle(n):
        pass

    
    def applyMove(self, permutation):
        self.cube = [self.cube[i] for i in permutation]

    def applyInverseMove(self, permutation):
        """
        
        """
        initialCube = [i for i in self.cube] 
        i = 0
        for j in permutation:
            self.cube[j] = initialCube[i]  
            i += 1

"""
def userInput(cube = []):
    
    NEED A GOOD WAY TO TEST THIS - ignoring this for now
    print("Hold the cube such that cubie with _, _, _ stickers is on the Front Up Right position with the _ color on the ", 
        " _ position \n")

    print("We have three axes of freedom for each sticker on a cubie: Front/Back, Up/Down, Right/Left.", 
            " To describe the color of a cubie, do the following: \n")

    cubies = ["Front up right cubie ", "Front Down Right Cubie ", "Front Up Left Cubie", "Front Down Left Cubie", 
                "Back up right cubie ", "Back Down Right Cubie ", "Back Up Left Cubie", "Back Down Left Cubie"]

    for i in cubies:
        color = input(f"\n Colors of the {i}: ")
        cube.append(color[0])
        cube.append(color[1])
        cube.append(color[2])
"""


        
            


