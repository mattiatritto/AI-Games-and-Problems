from csp.contraints import *


class CSP:

    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.initial_state = dict()

    def consistent(self, state):
        return all([c.check(state) for c in self.constraints])

    def complete(self, state):
        return len(state) == len(self.variables)

    def goal_test(self, state):
        return self.complete(state) and self.consistent(state)

    def assign(self, state, variable, value):
        if variable in self.variables and value in self.domains[variable]:
            new_state = dict(state)
            new_state[variable] = value
            return new_state
        raise ValueError

    def rollback(self, state, variable):
        if variable in self.variables:
            new_state = dict(state)
            del new_state[variable]
            return new_state
        raise ValueError

    def legal_moves(self, state, variable):
        possible_values = self.domains[variable]
        return [value for value in possible_values
                if self.consistent(self.assign(state, variable, value))]

    def count_constraints(self, first_variable, second_variable):
        return sum([1 for c in self.constraints
                    if first_variable in c.variables
                    and second_variable in c.variables])

    def remaining_constraints(self, state, variable):
        remaining_variables = [var for var in self.variables if var not in state and var != variable]
        if remaining_variables:
            return sum([self.count_constraints(variable, rem_var) for rem_var in remaining_variables])
        else:
            return 0

    def assignable_variables(self, state):
        return [variable for variable in self.variables if variable not in state]

    def remove_inconsistent_values(self, arc, actual_state):
        x_i, x_j = arc.variables

        removed = False
        for value_i in self.domains[x_i]:
            state = self.assign(state=actual_state,
                                variable=x_i,
                                value=value_i)

            assignments = [arc.check(self.assign(state=state,
                                                 variable=x_j,
                                                 value=value_j)) for value_j in self.domains[x_j]]

            if not any(assignments):

                self.domains[x_i].remove(value_i)
                print(f'removing {value_i} from {x_i}')
                removed = True
        return removed



class Sudoku(CSP):
    def __init__(self, num_squares=4):
        self.variables = []

        for char in range(ord('A'), ord('A') + num_squares):
            for i in range(1, num_squares+1):
                self.variables.append(f'{chr(char)}{i}')


        single_domain = [i for i in range(1, num_squares+1)]
        self.domains = {var: single_domain for var in self.variables}

        self.constraints = [

            # Constraints for the same block
            DifferentValues(['A1', 'A2']),
            DifferentValues(['A1', 'A3']),
            DifferentValues(['A1', 'A4']),
            DifferentValues(['A2', 'A1']),
            DifferentValues(['A2', 'A3']),
            DifferentValues(['A2', 'A4']),
            DifferentValues(['A3', 'A1']),
            DifferentValues(['A3', 'A2']),
            DifferentValues(['A3', 'A4']),
            DifferentValues(['A4', 'A1']),
            DifferentValues(['A4', 'A2']),
            DifferentValues(['A4', 'A3']),

            DifferentValues(['B1', 'B2']),
            DifferentValues(['B1', 'B3']),
            DifferentValues(['B1', 'B4']),
            DifferentValues(['B2', 'B1']),
            DifferentValues(['B2', 'B3']),
            DifferentValues(['B2', 'B4']),
            DifferentValues(['B3', 'B1']),
            DifferentValues(['B3', 'B2']),
            DifferentValues(['B3', 'B4']),
            DifferentValues(['B4', 'B1']),
            DifferentValues(['B4', 'B2']),
            DifferentValues(['B4', 'B3']),

            DifferentValues(['C1', 'C2']),
            DifferentValues(['C1', 'C3']),
            DifferentValues(['C1', 'C4']),
            DifferentValues(['C2', 'C1']),
            DifferentValues(['C2', 'C3']),
            DifferentValues(['C2', 'C4']),
            DifferentValues(['C3', 'C1']),
            DifferentValues(['C3', 'C2']),
            DifferentValues(['C3', 'C4']),
            DifferentValues(['C4', 'C1']),
            DifferentValues(['C4', 'C2']),
            DifferentValues(['C4', 'C3']),

            DifferentValues(['D1', 'D2']),
            DifferentValues(['D1', 'D3']),
            DifferentValues(['D1', 'D4']),
            DifferentValues(['D2', 'D1']),
            DifferentValues(['D2', 'D3']),
            DifferentValues(['D2', 'D4']),
            DifferentValues(['D3', 'D1']),
            DifferentValues(['D3', 'D2']),
            DifferentValues(['D3', 'D4']),
            DifferentValues(['D4', 'D1']),
            DifferentValues(['D4', 'D2']),
            DifferentValues(['D4', 'D3']),

            # Constraints for the same column

            DifferentValues(['A1', 'A3']),
            DifferentValues(['A1', 'C1']),
            DifferentValues(['A1', 'C3']),
            DifferentValues(['A3', 'A1']),
            DifferentValues(['A3', 'C1']),
            DifferentValues(['A3', 'C3']),
            DifferentValues(['C1', 'A1']),
            DifferentValues(['C1', 'A3']),
            DifferentValues(['C1', 'C3']),
            DifferentValues(['C3', 'A1']),
            DifferentValues(['C3', 'A3']),
            DifferentValues(['C3', 'C1']),

            DifferentValues(['A2', 'A4']),
            DifferentValues(['A2', 'C2']),
            DifferentValues(['A2', 'C4']),
            DifferentValues(['A4', 'A2']),
            DifferentValues(['A4', 'C2']),
            DifferentValues(['A4', 'C4']),
            DifferentValues(['C2', 'A2']),
            DifferentValues(['C2', 'A4']),
            DifferentValues(['C2', 'C4']),
            DifferentValues(['C4', 'A2']),
            DifferentValues(['C4', 'A4']),
            DifferentValues(['C4', 'C2']),

            DifferentValues(['B1', 'B3']),
            DifferentValues(['B1', 'D1']),
            DifferentValues(['B1', 'D3']),
            DifferentValues(['B3', 'B1']),
            DifferentValues(['B3', 'D1']),
            DifferentValues(['B3', 'D3']),
            DifferentValues(['D1', 'B1']),
            DifferentValues(['D1', 'B3']),
            DifferentValues(['D1', 'D3']),
            DifferentValues(['D3', 'B1']),
            DifferentValues(['D3', 'B3']),
            DifferentValues(['D3', 'D1']),

            DifferentValues(['B2', 'B4']),
            DifferentValues(['B2', 'D2']),
            DifferentValues(['B2', 'D4']),
            DifferentValues(['B4', 'B2']),
            DifferentValues(['B4', 'D2']),
            DifferentValues(['B4', 'D4']),
            DifferentValues(['D2', 'B2']),
            DifferentValues(['D2', 'B4']),
            DifferentValues(['D2', 'D4']),
            DifferentValues(['D4', 'B2']),
            DifferentValues(['D4', 'B4']),
            DifferentValues(['D4', 'D2']),

            # Constraints for the same row

            DifferentValues(['A1', 'A2']),
            DifferentValues(['A1', 'B1']),
            DifferentValues(['A1', 'B2']),
            DifferentValues(['A2', 'A1']),
            DifferentValues(['A2', 'B1']),
            DifferentValues(['A2', 'B2']),
            DifferentValues(['B1', 'A1']),
            DifferentValues(['B1', 'A2']),
            DifferentValues(['B1', 'B2']),
            DifferentValues(['B2', 'A1']),
            DifferentValues(['B2', 'A2']),
            DifferentValues(['B2', 'B1']),

            DifferentValues(['A3', 'A4']),
            DifferentValues(['A3', 'B3']),
            DifferentValues(['A3', 'B4']),
            DifferentValues(['A4', 'A3']),
            DifferentValues(['A4', 'B3']),
            DifferentValues(['A4', 'B4']),
            DifferentValues(['B3', 'A3']),
            DifferentValues(['B3', 'A4']),
            DifferentValues(['B3', 'B4']),
            DifferentValues(['B4', 'A3']),
            DifferentValues(['B4', 'A4']),
            DifferentValues(['B4', 'B3']),

            DifferentValues(['C1', 'C2']),
            DifferentValues(['C1', 'D1']),
            DifferentValues(['C1', 'D2']),
            DifferentValues(['C2', 'C1']),
            DifferentValues(['C2', 'D1']),
            DifferentValues(['C2', 'D2']),
            DifferentValues(['D1', 'C1']),
            DifferentValues(['D1', 'C2']),
            DifferentValues(['D1', 'D2']),
            DifferentValues(['D2', 'C1']),
            DifferentValues(['D2', 'C2']),
            DifferentValues(['D2', 'D1']),

            DifferentValues(['C3', 'C4']),
            DifferentValues(['C3', 'D3']),
            DifferentValues(['C3', 'D4']),
            DifferentValues(['C4', 'C3']),
            DifferentValues(['C4', 'D3']),
            DifferentValues(['C4', 'D4']),
            DifferentValues(['D3', 'C3']),
            DifferentValues(['D3', 'C4']),
            DifferentValues(['D3', 'D4']),
            DifferentValues(['D4', 'C3']),
            DifferentValues(['D4', 'C4']),
            DifferentValues(['D4', 'D3'])
        ]

    def print_state(self, state):
        string = (f"{state['A1']} | {state['A2']} | {state['B1']} | {state['B2']}\n"
                  f"{state['A3']} | {state['A4']} | {state['B3']} | {state['B4']}\n"
                  f"{state['C1']} | {state['C2']} | {state['D1']} | {state['D2']}\n"
                  f"{state['C3']} | {state['C4']} | {state['D3']} | {state['D4']}\n")
        return string