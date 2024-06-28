import numpy as np



class Minimax:
    def __init__(self, game):
        self.game = game

    def max_value(self, state):
        if self.game.terminal_test(state):
            return self.game.utility(state)
        values = [self.min_value(s) for s, a in self.game.successors(state)]
        return max(values)

    def min_value(self, state):
        if self.game.terminal_test(state):
            return self.game.player(state)
        values = [self.max_value(s) for s, a in self.game.successors(state)]
        return min(values)

    def next_move(self, state):
        moves = self.game.actions(state)
        for move in moves:
            print(move, self.min_value(self.game.result(state, move)))
        return max(moves, key=lambda move: self.min_value(self.game.result(state, move)))


class AlphaBeta:

    def __init__(self, game):
        self.game = game

    def max_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.player(state)

        best_value = -np.inf
        for s, a in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            best_value = max(best_value, value)
            if best_value > beta:
                return best_value
            alpha = max(alpha, best_value)
        return best_value

    def min_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.player(state)

        best_value = np.inf
        for s, a in self.game.successors(state):
            value = self.max_value(s, alpha, beta)
            best_value = min(best_value, value)
            if best_value < alpha:
                return best_value
            beta = min(beta, best_value)
        return best_value

    def next_move(self, state):
        alpha = -np.inf
        beta = np.inf

        best_move = None

        for s, move in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            if value > alpha:
                alpha = value
                best_move = move
        return best_move


class LimitedAlphaBeta:

    def __init__(self, game, limit=1000000000):
        self.game = game
        self.limit = limit

    def max_value(self, state, alpha, beta, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player(state)
        best_value = -np.inf
        for s, a in self.game.successors(state):
            value = self.min_value(s, alpha, beta, limit-1)
            best_value = max(best_value, value)
            if best_value > beta:
                return best_value
            alpha = max(alpha, best_value)
        return best_value

    def min_value(self, state, alpha, beta, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player(state)
        best_value = np.inf
        for s, a in self.game.successors(state):
            value = self.max_value(s, alpha, beta, limit-1)
            best_value = min(best_value, value)
            if best_value < alpha:
                return best_value
            beta = min(beta, best_value)
        return best_value

    def next_move(self, state):
        alpha = -np.inf
        beta = np.inf

        best_move = None

        for s, move in self.game.successors(state):
            value = self.min_value(s, alpha, beta, self.limit)
            if value > alpha:
                alpha = value
                best_move = move
        return best_move


class LimitedMinimax:
    def __init__(self, game, limit=100000000):
        self.game = game
        self.limit = limit

    def max_value(self, state, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player(state)
        values = [self.min_value(s, limit - 1) for s, a in self.game.successors(state)]
        return max(values)

    def min_value(self, state, limit):
        if self.game.terminal_test(state) or limit == 0:
            return self.game.player(state)
        values = [self.max_value(s, limit - 1) for s, a in self.game.successors(state)]
        return min(values)

    def next_move(self, state):
        moves = self.game.actions(state)
        return max(moves, key=lambda move: self.min_value(self.game.result(state, move), self.limit))