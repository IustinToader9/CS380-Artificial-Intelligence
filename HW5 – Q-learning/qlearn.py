import random
import sys


DEFAULT_STATE = '       | ###  -| # #  +| # ####|       '


class Action:

    def __init__(self, name, dx, dy):
        self.name = name
        self.dx = dx
        self.dy = dy


ACTIONS = [
    Action('UP', 0, -1),
    Action('RIGHT', +1, 0),
    Action('DOWN', 0, +1),
    Action('LEFT', -1, 0)
]


class State:

    def __init__(self, env, x, y):
        self.env = env
        self.x = x
        self.y = y

    def clone(self):
        return State(self.env, self.x, self.y)

    def is_legal(self, action):
        cell = self.env.get(self.x + action.dx, self.y + action.dy)
        return cell is not None and cell in ' +-'
    
    def legal_actions(self, actions):
        legal = []
        for action in actions:
            if self.is_legal(action):
                legal.append(action)
        return legal
    
    def reward(self):
        cell = self.env.get(self.x, self.y)
        if cell is None:
            return None
        elif cell == '+':
            return +10
        elif cell == '-':
            return -10
        else:
            return 0

    def at_end(self):
        return self.reward() != 0

    def execute(self, action):
        self.x += action.dx
        self.y += action.dy
        return self

    def __str__(self):
        tmp = self.env.get(self.x, self.y)
        self.env.put(self.x, self.y, 'A')
        s = ' ' + ('-' * self.env.x_size) + '\n'
        for y in range(self.env.y_size):
            s += '|' + ''.join(self.env.row(y)) + '|\n'
        s += ' ' + ('-' * self.env.x_size)
        self.env.put(self.x, self.y, tmp)
        return s


class Env:

    def __init__(self, string):
        self.grid = [list(line) for line in string.split('|')]
        self.x_size = len(self.grid[0])
        self.y_size = len(self.grid)

    def get(self, x, y):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            return self.grid[y][x]
        else:
            return None

    def put(self, x, y, val):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            self.grid[y][x] = val

    def row(self, y):
        return self.grid[y]

    def random_state(self):
        x = random.randrange(0, self.x_size)
        y = random.randrange(0, self.y_size)
        while self.get(x, y) != ' ':
            x = random.randrange(0, self.x_size)
            y = random.randrange(0, self.y_size)
        return State(self, x, y)


class QTable:

    def __init__(self, env, actions):
        self.env=env
        self.actions=actions
        self.dict={}

    def get_q(self, state, action):
        return self.dict.get((state.x, state.y, action), 0)
        # return the value of the q table for the given state, action

    def get_q_row(self, state):
        q_max=float('-inf')
        idx=0
        for key, value in self.dict.items():
            if key[0]==state.x and key[1]==state.y:
                if value >= q_max:
                    q_max=value
                    idx=key
        if q_max==float('-inf'):
            return (0, None)
        return (q_max, idx)
        # return the row of q table corresponding to the given state

    def set_q(self, state, action, val):
        self.dict[(state.x, state.y, action)]=val
        return
        # set the value of the q table for the given state, action

    def learn_episode(self, alpha=.10, gamma=.90):
        state=env.random_state()
        while not state.at_end():
            print(state, (state.x, state.y))
            actions = state.legal_actions(self.actions)
            action = random.choice(actions)
            new_state=state.clone().execute(action)
            reward=new_state.reward()
            max_q=gamma*self.get_q_row(new_state)[0]
            sample=reward+max_q
            new_val=(1-alpha)*self.get_q(state, action)+alpha*sample
            self.set_q(state, action, new_val)
            state=new_state.clone()

        # with the given alpha and gamma values,
        # from a random initial state,
        # consider a random legal action, execute that action,
        # compute the reward, and update the q table for (state, action).
        # repeat until an end state is reached (thus completing the episode)
        # also print the state after each action
    
    def learn(self, episodes, alpha=.10, gamma=.90):
        for i in range(episodes):
            self.learn_episode()
        # run <episodes> number of episodes for learning with the given alpha and gamma

    def __str__(self):
        s=str()
        for a in self.actions:
            s+=a.name+'\n'
            for i in range(self.env.y_size):
                for j in range(self.env.x_size):
                    if self.dict.get((j, i, a), 0)==0:
                        s+='----'+'\t'
                    else:
                        s+="{:.2f}".format( self.dict[(j, i, a)])+'\t'
                s+='\n'
            s+='\n'
        return s
        # return a string for the q table as described in the assignment

    def play(self):
        state=env.random_state()
        while not state.at_end():
            print(state)
            action = self.get_q_row(state)[1]
            print(action[2].name)
            state.execute(action[2])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        env = Env(sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE)
        if cmd == 'learn':
            qt = QTable(env, ACTIONS)
            qt.learn(100)
            print(qt)
