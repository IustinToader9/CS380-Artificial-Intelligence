# File description

- run.sh - shell script to pass different arguments to the code
- RubiksCube.py – Python implementation of the Rubik's Cube

# State Representation 

- Cube has 6 2x2 faces, with each letter representing the color of a cubie. The default state of the cube is the following: "WWWW RRRR GGGG YYYY OOOO BBBB"
- The indexing order that maps this string to the 2-dimensional representation of the cube is as follows:
       0  1
       2  3
16 17  8  9  4  5  20 21
18 19 10 11  6  7  22 23
      12 13
      14 15

# Methods

## - print
  - Function that prints the state in ASCII characters
  - If the state representation argument is not provided, uses the default state mentioned above
  - Example: sh run.sh print "RWOR GOYB BOGW BRBW YWYO RGYG"
       RW
       OR
    YW BO GO RG
    YO GW YB YG
       BR
       BW

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
   GW
   WR
WB OG YR BR
OO GW GR BB
   YO
   YY
   

## - shuffle
  - Starts from the default cube and shuffles it by picking n random moves
  - Example:
sh run.sh shuffle 10 R' R F D' B R' B' R R F
   WG
   GY
OR WG OW OB
RW BG RY BY
   RY
   BO

## - random 
  - Method that completes a random walk
  - It takes an input of sequence used to permute the default cube state, then randomly selects N moves from the set of all possible moves and stops after N moves, or once the cube has been solved. If it has not been solved, the cycle is counted as a single iteration, the cube is reset to the initial permuted state, and the process is repeated. Finally, it returns the number of iterations needed to solve the cube.
  - The method also takes a time limit in seconds
  - Example: sh run.sh random "L D' R' F R D'" 6 10
             U B' U' F L F'
      BW            GB            WR    
      GW            WW            WW  
   OY RR BB OY   RR BB OY OY   RR BB OG YG
   WR BY OO WG   WR BY OO WG   GR BY OB OW
      YG            YG            YG 
      RG            RG            OY    

      RW            RW            WW 
      WW            RG            GG
   YG RR BB OG   YY BR WB OG   GY RR WB OO
   GR BY OB OW   GG YR WB OW   GY RR WB OO
      YG            OB            BB
      OY            OY            YY
      
      WW
      WW 
   GG RR BB OO
   GG RR BB OO
      YY
      YY

916314
5.33
