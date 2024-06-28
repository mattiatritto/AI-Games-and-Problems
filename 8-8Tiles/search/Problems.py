import copy
import numpy as np



class NTiles:

    def __init__(self, n_tiles=8):
        self.initial_state = [['7', '2', '4'], ['5', ' ', '6'], ['8', '3', '1']]
        self.goal_state = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', ' ']]
        self.n_tiles = n_tiles
        self.n_rows = self.n_cols = np.sqrt(n_tiles + 1)

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def find_blank_tile(self, state):
        row = 0
        for line in state:
            try:
                col = line.index(' ')
                break
            except(ValueError):
                row = row + 1
        return row, col

    def actions(self, state):

        row, col = self.find_blank_tile(state)
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

        if (col == 0):
            possible_actions.remove('LEFT')
        if (col == self.n_cols-1):
            possible_actions.remove('RIGHT')
        if (row == 0):
            possible_actions.remove('UP')
        if (row == self.n_rows-1):
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        row, col = self.find_blank_tile(state)
        new_state = copy.deepcopy(state)

        if action == 'UP':
            temp = state[row-1][col]
            new_state[row-1][col] = ' '
            new_state[row][col] = temp
        if action == 'DOWN':
            temp = state[row+1][col]
            new_state[row+1][col] = ' '
            new_state[row][col] = temp
        if action == 'LEFT':
            temp = state[row][col-1]
            new_state[row][col-1] = ' '
            new_state[row][col] = temp
        if action == 'RIGHT':
            temp = state[row][col+1]
            new_state[row][col+1] = ' '
            new_state[row][col] = temp

        return new_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        goal_positions = {}
        for i in range(len(self.goal_state)):
            for j in range(len(self.goal_state[i])):
                goal_positions[self.goal_state[i][j]] = (i, j)

        distance = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                tile = state[i][j]
                if tile != ' ':
                    goal_i, goal_j = goal_positions[tile]
                    distance += abs(i - goal_i) + abs(j - goal_j)

        return distance

    def goal_test(self, state):
        return state == self.goal_state