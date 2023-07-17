My implementation of various adversarial agents to play the game Othello as directed in the [instructions file](https://github.com/IustinToader9/CS380-Artificial-Intelligence/blob/a56d6959d5d12bc23c04686c8da76ea3ea998ae5/HW3%20%E2%80%93%20Othello/Othello.pdf)

The available agents are the following:
  - Human agent: The program awaits a human player's input for each turn
  - Random agent: The random agent picks a random legal move for each turn
  - Minimax agent: AI agent choosing each move using the standard minimax algorithm. The desired depth of search must be included in the agent constructor
  - Alpha-Beta Pruning agent: AI agent improving on the complexity of the Minimax agent by incorporating alpha-beta search. The desired depth of search must be included in the agent constructor

# File description
- run.sh – Shell script to pass arguments to Python code
- othello.py – Python file containing the OthelloMove and State classes. The OthelloMove class enables the functionality of player moves, containing information such as which player made it and its coordinates. The State class is the core class, which implements most of the game's functionality.
- agent.py – Python file containing the classes of each agent type. The HumanPlayer, RandomAgent, MinimaxAgent, and AlphaBeta classes are all extensions of the abstract Player class found in game.py
- game.py – Python file containing the Game class which uses all other classes to play the game of Othello, as well as the abstract Player class defining an Othello agent
- main.py – Python file converting the arguments passed in run.sh to a game of Othello
