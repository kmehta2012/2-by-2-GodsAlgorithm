# How to Set-up the 2-by-2 God's algorithm application
1. Clone the repository:  To clone the repository, run the following command in your terminal:  
`git clone https://github.com/kmehta2012/2-by-2-GodsAlgorithm.git`
2. Navigate to the Project Directory using the terminal:  
`cd 2-by-2-GodsAlgorithm`
3. ***You need to have python3 installed to use this application.*** Assuming you have python3, run the following command to use the application:  
`python3 GodsAlgorithm.py`
4. After running the above command on the terminal, you follow the instructions as seen on the terminal. For the program to run correctly, you'll need to understand how to correctly input the cube to the program. ***Please see the heading titled "Inputting the Cube correctly" to understand how to correctly input the cube.***

# How to correctly use the program
## Inputting the Cube correctly
After step 3 (under the "How to Use the 2-by-2 God's Algorithm application") the program prompts the user to input the cube. The user must input the cube correctly for
the program to work correctly. Below is an explanation of the terms that the program uses when asking for input and how to input the cube.

1. The 2 by 2 cube has 6 faces: The Front and Back Faces, the Up and Down faces, and the Right and Left Faces. There are 8 cubies (the smaller cubes) each having 3 colours (a colour is also called a sticker in cubing) in 3 of the 6 faces. The location of a cubie can be described by the faces where its stickers lie.

2. For example, the Front Up Right Cubie has one sticker on the Front face, one sticker on the Up face, and one Sticker on the Right face.

3. Any Cubie will have a sticker on the Front/Back face, Up/Down Face, and Left/Right face. The program prompts the user to enter the colors of each cubie. To correctly do so, enter the first letter of the colour on the Front/Back face, then the first letter of the colour on the Up/Down Face, and lastly enter the first letter of the color on the left/right face - all without any space.
4. Here's a concrete example:  
   ![Imgur](https://i.imgur.com/GVXXyfib.jpg)  
The Front Up Right right cubie has Yellow on the Front face, Blue on the Up Face, and Orange on the Right face. When the program asks the user to enter the colors on the Front Up Right cubie, the user should enter the following: `ybo`. Again, enter the first letter of the color on the Front/Back Face, then on the Up/Down face, and then on the Right/Left face.


## Interpreting the results 
1. After the user inputs the cube to the program, the program prints out a list of moves that will solve the cube. Standard singmaster notation has been used for the moves. Here is a quick glossary of the notation:
     1. F : Rotate the Front Face 90 degrees clockwise
     2. F' : Rotate the Front Face 90 degrees counterclockwise
     3. U : Rotate the Up Face 90 degrees clockwise
     4. U' : Rotate the Up Face 90 degrees counterclockwise
     5. L : Rotate the Left Face 90 degrees clockwise
     6. L' Rotate the Left face 90 degrees counterclockwise
       
The program only uses the above moves. You can of course also rotate the Right and Down faces, it is probably easy to guess the notation of those four moves. The program does not use those four moves, so we don't mention them in the glossary.

# How the program works
1. The idea is to model the Rubik's cube as a graph. The vertices of the graph are distinct states of the cube and there is an edge between any two vertices that are one quarter move apart (where a quarter move is one of the six moves listed above under "Interpreting the results").
2. Now we can use a search algorithm to search for the shortest path between any two states of this graph. The program uses a Breadth First Search algorithm. More specifically, a two-way BFS on the graph.
3. The program runs a BFS from the initial state and a BFS from the solved state. The common state where both the BFSs meet gives us the shortest path:  Go from the initial state to the common state using the shortest path given by the BFS and then go from the common state to the solved state using the shortest path from the common state to the solved state.
4. This is computationally tractable because the God's Number for the 2 by 2 is only 14 and there are only about ~3.7 million legal states of the cube, which isn't a huge number for a computer to handle.
   

# Video Demo
to be added

# Future work

to be written
