import numpy as np
import random



class Battleship:

    def __init__(self, player, cols=4, rows=4, numShips=4):

        self.cols = cols
        self.rows = rows
        self.numShips = numShips
        self.initial_state = self.init_state()
        self.player = player



    def init_state(self):
        state = {
            'boardMax': np.zeros((self.cols, self.rows)),
            'boardMin': np.zeros((self.cols, self.rows)),
            'shipsSunkMax': 0,
            'shipsSunkMin': 0,
        }

        for _ in range(0, self.numShips):
            colShip = random.randint(0, self.cols-1)
            rowShip = random.randint(0, self.rows-1)
            while(state["boardMax"][rowShip][colShip] == 1):
                colShip = random.randint(0, self.cols - 1)
                rowShip = random.randint(0, self.rows - 1)
            state["boardMax"][rowShip][colShip] = 1

        for _ in range(0, self.numShips):
            colShip = random.randint(0, self.cols-1)
            rowShip = random.randint(0, self.rows-1)
            while(state["boardMin"][rowShip][colShip] == 1):
                colShip = random.randint(0, self.cols - 1)
                rowShip = random.randint(0, self.rows - 1)
            state["boardMin"][rowShip][colShip] = 1

        return state

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        actions = []
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                actions.append([row, col])
        return actions

    def result(self, state, action):

        new_state = state.copy()

        if self.player == 'MIN':
            if new_state["boardMax"][action[0]][action[1]] == 1:
                new_state["boardMax"][action[0]][action[1]] = 0
                new_state["shipsSunkMax"] = new_state["shipsSunkMax"] + 1
        elif self.player == 'MAX':
            if new_state["boardMin"][action[0]][action[1]] == 1:
                new_state["boardMin"][action[0]][action[1]] = 0
                new_state["shipsSunkMin"] = new_state["shipsSunkMin"] + 1

        return new_state

    def terminal_test(self, state):
        return (state["shipsSunkMax"] == self.numShips) | (state["shipsSunkMin"] == self.numShips)

    def utility(self, state):
        if self.player == 'MAX':
            return state["shipsSunkMin"]
        elif self.player == 'MIN':
            return state["shipsSunkMax"]

    def next_player(self):
        if self.player == 'MAX':
            return 'MIN'
        else:
            return 'MAX'

    def display_state(self, state):
        print("BOARD MAX")
        print(state["boardMax"])
        print("BOARD MIN")
        print(state["boardMin"])
        print("SHIPS SUNK MAX")
        print(state["shipsSunkMax"])
        print("SHIPS SUNK MIN")
        print(state["shipsSunkMin"])

    def next_move_random(self, state):
        possible_actions = self.actions(state)
        return random.choice(possible_actions)

    def next_move_input(self, state):
        return [int(input(f"[{self.player}]: Choose the row you want to attack: ")), int(input(f"[{self.player}]: Choose the col you want to attack: "))]

    def play(self, player_one, player_two):
        state = self.initial_state
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    if state["shipsSunkMax"] == self.numShips:
                        print("MIN WINS!")
                    else:
                        print("MAX WINS!")
                    return moves
                move = self.next_move_input(state)
                state = self.result(state, move)
                self.display_state(state)
                moves.append((move, self.player))
                self.player = self.next_player()