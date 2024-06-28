import copy

class HanoiTowerProblem:

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        actions = []
        for rod in list(state.keys()):
            remaining_rods = [rem_rod for rem_rod in list(state.keys()) if rem_rod != rod]
            if state[rod] != []:
                [actions.append((rod, rem_rod)) for rem_rod in remaining_rods]
        return actions


    def result(self, state=None, action=None):
        new_state = copy.deepcopy(state)
        disk = new_state[action[0]].pop()
        new_state[action[1]].append(disk)
        return new_state


    def goal_test(self, state):
        return state == self.goal_state

    def cost(self, state, action):
        return 1

    def h(self, state):
        h = 0

        for rod in list(state.keys()):
            if (state[rod] != []):
                prevElem = state[rod][0]
            else:
                continue
            for value in state[rod]:
                if prevElem < value:
                    h = h + 1
                    prevElem = value

        return h