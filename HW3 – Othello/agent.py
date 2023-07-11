import math
import random

import game

class HumanPlayer(game.Player):

    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        # generate the list of moves:
        moves = state.generateMoves()
        if not moves:
            return None
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class RandomAgent(game.Player):

    def __init__(selfs):
        super().__init__()

    def choose_move(self, state):
        moves=state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        if len(moves)==1:
            response=0
        elif not moves:
            return None
        else:
            response=random.randint(0, len(moves)-1)
        move=moves[response]
        return move



class MinimaxAgent(game.Player):
    def __init__(selfs, depth, turn):
        super().__init__()
        selfs.depth=depth
        selfs.turn=turn

    def max_value(self, state, d):
        if state.game_over() or d>self.depth:
            return state.score()
        v=float('-inf')
        moves=state.generateMoves()
        d+=1
        for i, action in enumerate(moves):
            v=max(v, self.min_value(state.applyMoveCloning(action), d))
        return v

    def min_value(self, state, d):
        if state.game_over() or d>self.depth:
            return state.score()
        v=float('inf')
        moves=state.generateMoves()
        d+=1
        for i, action in enumerate(moves):
            v=min(v, self.max_value(state.applyMoveCloning(action), d))
        return v

    def choose_move(self, state):
        d=0
        action_list=[]
        moves=state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
            if self.turn==1:
                action_list.append(self.min_value(state.applyMoveCloning(action), d))
            else:
                action_list.append(self.max_value(state.applyMoveCloning(action), d))
        if self.turn==1:
            max=float('-inf')
            #print(action_list)
            if len(action_list)==1:
                max_i=0
            elif not action_list:
                return None
            else:
                for i in range(len(action_list)):
                    if action_list[i]>max:
                        max=action_list[i]
                        max_i=i
                if max==float('-inf'):
                    max_i=0
            print(action_list)
            return moves[max_i]
        else:
            min = float('inf')
            # print(action_list)
            if len(action_list) == 1:
                min_i = 0
            elif not action_list:
                return None
            else:
                for i in range(len(action_list)):
                    if action_list[i] < min:
                        min = action_list[i]
                        min_i = i
                if min == float('inf'):
                    min_i = 0
            print(action_list)
            return moves[min_i]



class AlphaBeta(game.Player):
    def __init__(selfs, depth, turn):
        super().__init__()
        selfs.depth=depth
        selfs.turn=turn

    def max_value(self, state, alpha, beta, d):
        #print(state)
        if state.game_over() or d>self.depth:
            return state.score()
        v=float('-inf')
        moves=state.generateMoves()
        d+=1
        for i, action in enumerate(moves):
            v=max(v, self.min_value(state.applyMoveCloning(action), alpha, beta, d))
            if v>=beta:
                return v
            alpha=max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, d):
        #print(state)
        if state.game_over() or d>self.depth:
            return state.score()
        v=float('inf')
        moves=state.generateMoves()
        d+=1
        for i, action in enumerate(moves):
            v=min(v, self.max_value(state.applyMoveCloning(action), alpha, beta, d))
            if v<=alpha:
                return v
            beta=min(beta, v)
        return v

    def choose_move(self, state):
        d=0
        action_list=[]
        moves=state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
            if self.turn==1:
                action_list.append(self.min_value(state.applyMoveCloning(action), float('-inf'), float('inf'), d))
            else:
                action_list.append(self.max_value(state.applyMoveCloning(action), float('-inf'), float('inf'), d))
        if self.turn==1:
            max=float('-inf')
            #print(action_list)
            if len(action_list)==1:
                max_i=0
            elif not action_list:
                return None
            else:
                for i in range(len(action_list)):
                    if action_list[i]>max:
                        max=action_list[i]
                        max_i=i
                if max==float('-inf'):
                    max_i=0
            print(action_list)
            return moves[max_i]
        else:
            min = float('inf')
            # print(action_list)
            if len(action_list) == 1:
                min_i = 0
            elif not action_list:
                return None
            else:
                for i in range(len(action_list)):
                    if action_list[i] < min:
                        min = action_list[i]
                        min_i = i
                if min == float('inf'):
                    min_i = 0
            print(action_list)
            return moves[min_i]