
import random
import sys
import time


# different moves
# https://ruwix.com/online-puzzle-simulators/2x2x2-pocket-cube-simulator.php

move_list=["U", "U'", "R", "R'", "F", "F'", "D", "D'", "L", "L'"
           , "B", "B'"]

MOVES = {
    "U": [2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23],
    "U'": [1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23],
    "R": [0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23],
    "R'": [0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12, 9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23],
    "F": [0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9, 6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23],
    "F'": [0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23],
    "D": [0,  1,  2,  3,  4,  5, 10, 11,  8,  9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21,  6,  7],
    "D'": [0,  1,  2,  3,  4,  5, 22, 23,  8,  9,  6,  7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19],
    "L": [23,  1, 21,  3,  4,  5,  6,  7,  0,  9,  2, 11, 8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12],
    "L'": [8,  1, 10,  3,  4,  5,  6,  7, 12,  9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20,  2, 22,  0],
    "B": [5,  7,  2,  3,  4, 15,  6, 14,  8,  9, 10, 11, 12, 13, 16, 18,  1, 17,  0, 19, 22, 20, 23, 21],
    "B'": [18, 16,  2,  3,  4,  0,  6,  1,  8,  9, 10, 11, 12, 13,  7,  5, 14, 17, 15, 19, 21, 23, 20, 22],
}


'''
sticker indices:

      0  1
      2  3
16 17  8  9   4  5  20 21
18 19  10 11  6  7  22 23
      12 13
      14 15

face colors:

    0
  4 2 1 5
    3

moves:
[ U , U', R , R', F , F', D , D', L , L', B , B']
'''

indeces = {
    0: [0, 3],
    1: [0, 4],
    2: [1, 3],
    3: [1, 4],
    4: [2, 6],
    5: [2, 7],
    6: [3, 6],
    7: [3, 7],
    8: [2, 3],
    9: [2, 4],
    10: [3, 3],
    11: [3, 4],
    12: [4, 3],
    13: [4, 4],
    14: [5, 3],
    15: [5, 4],
    16: [2, 0],
    17: [2, 1],
    18: [3, 0],
    19: [3, 1],
    20: [2, 9],
    21: [2, 10],
    22: [3, 9],
    23: [3, 10]

}


def is_proper(state):
    if len(state)!=29:
        return 1
    else:
        for i in range(4,len(state),5):
            if state[i]!=" ":
                return 1
        if state.count('W')!=4:
            return 1
        if state.count('R')!=4:
            return 1
        if state.count('G')!=4:
            return 1
        if state.count('Y')!=4:
            return 1
        if state.count('O')!=4:
            return 1
        if state.count('B')!=4:
            return 1
    return 0

def append_matrix(m1, m2):
    if not m1:
        return m2
    else:
        m3=[]
        for i in range(len(m1)):
            m3.append(m1[i]+m2[i])
        return m3

def heuristic_mapping(state):
    corners= {
        (1, 1, 1): {state[3], state[4], state[9]},
        (1, 1, 0): {state[1], state[5], state[20]},
        (1, 0, 1): {state[13], state[6], state[11]},
        (1, 0, 0): {state[15], state[7], state[22]},
        (0, 1, 1): {state[2], state[17], state[8]},
        (0, 1, 0): {state[0], state[16], state[21]},
        (0, 0, 1): {state[12], state[19], state[10]},
        (0, 0, 0): {state[14], state[18], state[23]}
    }
    return corners

def heuristic(state):
    default_cube=heuristic_mapping("WWWWRRRRGGGGYYYYOOOOBBBB")
    state_map=heuristic_mapping(state)
    man_dist=0
    for corner_idx, corner_map in state_map.items():
        default_idx=list(default_cube.keys())[list(default_cube.values()).index(corner_map)]
        man_dist+=abs(corner_idx[0]-default_idx[0]) + abs(corner_idx[1]-default_idx[1]) + abs(corner_idx[2]-default_idx[2])
    return man_dist/4


class cube:

  def __init__(self, string="WWWW RRRR GGGG YYYY OOOO BBBB"):
    # normalize stickers relative to a fixed corner
    self.string=string.replace(" ", '')
    self.norm_string=self.norm()
    return
    
  def update(self, string):
      self.string=string
      self.norm_string=self.norm()
      return

  def norm(self, state=None):
    # your code
    if state is None:
        state=self.clone()
    else:
        state=state.replace(" ", '')
    matr = [[' '] * 15 for i in range(6)]

    for s in range(len(state)):
        matr[indeces[s][0]][indeces[s][1]]=state[s]

    return matr

  def equals(self, cube):
    # your code
    for s in range(len(self.string)):
        if self.string[s]!=cube[s]:
            print('False')
            return
    print('True')
    return

  def goal(self, state=None):
      if state is None:
          state = self.clone()
      else:
          state = state.replace(" ", '')
      for s in range(len(state)-1):
          if state[s]!=state[s+1] and (s+1)%4!=0:
              return 1
      return 0

  def clone(self):
    # your code
    return self.string

    # apply a move to a state
  def applyMove(self, state, move):
    # your code
    new_str=[0]*24
    for s in range(len(state)):
        new_str[s]=state[MOVES[move][s]]
    state=new_str
    return state

    # apply a string sequence of moves to a state
  def applyMovesStr(self, alg, state=None):
    if state is None:
        state=self.clone()
    else:
        state=state.replace(" ", '')
    moves=alg.split(" ")
    for i in moves:
        state=self.applyMove(state, i)
    state=''.join(state)
    return state


    # print state of the cube
  def print(self, state=None):
    if state is None:
        norm_state=self.norm_string
    else:
        state=state.replace(" ", '')
        norm_state=self.norm(state)

    for i in range(6):
        for j in range(13):
            print(norm_state[i][j], end='')
        print()
    return

  def shuffle(self, n):
    # your code
    state = self.clone()
    for i in range(n):
        m=random.randint(0,len(MOVES)-1)
        print(move_list[m], end=' ')
        state=self.applyMove(state,move_list[m])
    state=''.join(state)
    print()
    print()
    self.print(state)
    return state

  def random(self, alg, n, t):
      self.string=''.join(self.applyMovesStr(alg))
      self.norm_string=self.norm()
      start=time.time()
      elapsed=0
      iter=0
      moves = alg.split(" ")
      hist=[self.string]
      seq=[]
      while elapsed<t:
          state = self.clone()
          for i in range(n):
              m = random.randint(0, len(MOVES) - 1)
              seq.append(move_list[m])
              state = self.applyMove(state, move_list[m])
              state = ''.join(state)
              hist.append(state)
              if self.goal(state)==0:
                  print(' '.join(seq))
                  print()
                  for j in range(len(hist)):
                      self.print(hist[j])
                      print()
                  print(iter)
                  print(str(round(time.time()-start,2)))
                  return 0
          hist=[self.string]
          seq=[]
          iter+=1
          elapsed=time.time()-start
      print("No solution")
      return 1

  def expand(self, state=None):

    nodes=[]
    for move in move_list:
        nodes.append(''.join(self.applyMove(state, move)))
    return nodes

  def print_seq(self, seq):
      state=self.string
      matr=self.norm_string
      ct=1
      n=len(seq)
      for k in range(n):
          move=seq[k]
          new_state=self.applyMove(state, move)
          new_state=''.join(new_state)
          matr=append_matrix(matr, self.norm(new_state))
          ct+=1
          state=new_state
          if ct%3==0 or k==n-1:
              for i in range(6):
                  for j in range(len(matr[i])):
                      print(matr[i][j], end='')
                  print()
              print("\n")
              ct=0
              matr=[]

      return

  def bfs(self, alg):
    self.string = ''.join(self.applyMovesStr(alg))
    self.norm_string = self.norm()

    closed=set()
    fringe=[(self.string, [])]
    open=set([self.string])
    node_count=0

    while fringe:
        state, seq = fringe.pop(0)
        open.remove(state)
        node_count+=1
        if self.goal(state) == 0:
            elapsed=time.time()-start
            return (seq, node_count)
        closed.add(state)
        successors=self.expand(state)

        for i in range(len(successors)):
            successor=successors[i]
            move=move_list[i]
            if successor not in closed and successor not in open:
                new_seq=seq+[move]
                fringe.append((successor, new_seq))
                open.add(successor)

    elapsed=time.time()-start
    return (None, node_count)


  def dls(self, dl):
    closed=set()
    fringe=[(self.string, [], 0)]
    open=set([self.string])
    node_count=0

    while fringe:
        state, seq, d = fringe.pop()
        open.remove(state)
        node_count+=1
        if self.goal(state) == 0:
            return (seq, node_count)
        if d<dl:
            closed.add((state, d))
            successors=self.expand(state)
            for i in range(len(successors)):
                successor=successors[i]
                move=move_list[i]
                if (successor, d+1) not in closed and successor not in open:
                    new_seq=seq+[move]
                    fringe.append((successor, new_seq, d+1))
                    open.add(successor)


    return (0, node_count)

  def ids(self, alg, dl):
      self.update(self.applyMovesStr(alg))
      total_nodes=0
      start=time.time()
      for i in range(dl+1):
          seq, node_count=self.dls(i)
          total_nodes+=node_count
          print("Depth: {d} d: {n}".format(d=i, n=node_count))
          if seq!=0:
              print("IDS found a solution at depth", i)
              print(' '.join(seq))
              self.print_seq(seq)
              print(total_nodes)
              print(str(round(time.time()-start, 2)))
              return

  def astar(self, alg):
      self.string = ''.join(self.applyMovesStr(alg))
      self.norm_string = self.norm()
      closed=set()
      fringe=[(heuristic(self.string), 0, self.string, [])]
      open=set([self.string])
      node_count=0

      while fringe:
          fringe.sort()
          f, g, state, seq=fringe.pop(0)
          open.remove(state)
          node_count+=1
          if self.goal(state) == 0:
              return (seq, node_count)
          closed.add(state)
          successors=self.expand(state)

          for i in range(len(successors)):
              successor=successors[i]
              move=move_list[i]
              if successor not in closed and successor not in open:
                  new_seq=seq+[move]
                  new_f=g+1+heuristic(successor)
                  fringe.append((new_f, g+1, successor, new_seq))
                  open.add(successor)
      return None



if sys.argv[1]=="print":
    if len(sys.argv)==2:
        cube1=cube()
        cube1.print()
    else:
        if is_proper(sys.argv[2]) == 1:
            print("Wrong input string")
        else:
            cube1=cube(sys.argv[2])
            cube1.print()
elif sys.argv[1]=="goal":
    cube1=cube()
    if is_proper(sys.argv[2]) == 1:
        print("Wrong input string")
    else:
        goal=cube1.goal(sys.argv[2])
        if goal==0:
            print("True")
        else:
            print("False")
elif sys.argv[1]=="applyMovesStr":
    cube1=cube()
    if len(sys.argv)==3:
        state=cube1.applyMovesStr(sys.argv[2])
        print(state)
        cube1.print(state)
    else:
        if is_proper(sys.argv[3]) == 1:
            print("Wrong input string")
        else:
            state=cube1.applyMovesStr(sys.argv[2], sys.argv[3])
            print(state)
            cube1.print(state)
elif sys.argv[1]=="shuffle":
    cube1=cube()
    cube1.shuffle(int(sys.argv[2]))
elif sys.argv[1]=="random":
    cube1=cube()
    cube1.random(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
elif sys.argv[1]=="bfs":
    cube1=cube()
    start=time.time()
    seq, node_count = cube1.bfs(sys.argv[2])
    print(' '.join(seq))
    cube1.print_seq(seq)
    print(node_count)
    print(str(round(time.time()-start,2)))
elif sys.argv[1]=="dls":
    cube1=cube()
    init_state=cube1.applyMovesStr(sys.argv[2])
    cube1.update(init_state)
    start=time.time()
    seq, node_count = cube1.dls(int(sys.argv[3]))
    if seq==0:
        print("Solution not found")
    else:
        print(' '.join(seq))
        cube1.print_seq(seq)
        print(node_count)
        print(str(round(time.time()-start,2)))
elif sys.argv[1]=="ids":
    cube1=cube()
    cube1.ids(sys.argv[2], int(sys.argv[3]))
elif sys.argv[1]=="astar":
    cube1=cube()
    start=time.time()
    seq, node_count = cube1.astar(sys.argv[2])
    print(' '.join(seq))
    cube1.print_seq(seq)
    print(node_count)
    print(str(round(time.time()-start,2)))

