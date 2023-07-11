# File description

- run.sh - shell script to pass different arguments to the code
- RubiksCube.py – Python implementation of the Rubik's Cube

# State Representation 

- Cube has 6 2x2 faces, with each letter representing the color of a cubie. The default state of the cube is the following: "WWWW RRRR GGGG YYYY OOOO BBBB"
- The indexing order that maps this string to the 2-dimensional representation of the cube is as follows:
![image](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/476b599ce4d5f402a85858fe68eb8eee34962175/HW1%20%E2%80%93%20Rubik's%20Cube%20part%201/imgs/img1.png)

# Methods

## - print
  - Function that prints the state in ASCII characters
  - If the state representation argument is not provided, uses the default state mentioned above
  - Example: sh run.sh print "RWOR GOYB BOGW BRBW YWYO RGYG"
    
![image](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/476b599ce4d5f402a85858fe68eb8eee34962175/HW1%20%E2%80%93%20Rubik's%20Cube%20part%201/imgs/img2.png)

## - goal
  - Method that determines whether the given cube is at a goal state (i.e. solved)
  - Example: sh run.sh goal "WWWW RRRR GGGG YYYY OOOO BBBB"
    
             True
## - applyMove
  - Given a state and a move, performs the move in the state
  - Possible moves are:
    - F (Front), R (Right), U (Up), B (Back), L (Left), D (Down) – 90-degree clockwise rotation
    - F' (Front), R' (Right), U' (Up), B' (Back), L' (Left), D' (Down) – 90-degree counterclockwise rotation

 ## - applyMovesStr
   - Given a state and a string sequence of moves, returns a new state, resulting from cloning the state and then applying the sequence of moves to the cloned state.
   - If the state representation argument is not provided, the default state is used
   - Example: sh run.sh applyMovesStr "R U' R'" "WWWW RRRR GGGG YYYY OOOO BBBB"
     
![image](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/476b599ce4d5f402a85858fe68eb8eee34962175/HW1%20%E2%80%93%20Rubik's%20Cube%20part%201/imgs/img3.png)
   

## - shuffle
  - Starts from the default cube and shuffles it by picking n random moves
  - Example:
sh run.sh shuffle 10 R' R F D' B R' B' R R F

![image](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/476b599ce4d5f402a85858fe68eb8eee34962175/HW1%20%E2%80%93%20Rubik's%20Cube%20part%201/imgs/img4.png)

## - random 
  - Method that completes a random walk
  - It takes an input of sequence used to permute the default cube state, then randomly selects N moves from the set of all possible moves and stops after N moves, or once the cube has been solved. If it has not been solved, the cycle is counted as a single iteration, the cube is reset to the initial permuted state, and the process is repeated. Finally, it returns the number of iterations needed to solve the cube.
  - The method also takes a time limit in seconds
  - Example: sh run.sh random "L D' R' F R D'" 6 10
    
U B' U' F L F'
![image](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/476b599ce4d5f402a85858fe68eb8eee34962175/HW1%20%E2%80%93%20Rubik's%20Cube%20part%201/imgs/img5.png)

916314

5.33
