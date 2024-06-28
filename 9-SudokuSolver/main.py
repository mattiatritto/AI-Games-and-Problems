from csp.ac3 import AC3
from csp.problem import Sudoku
from csp.backtracking import BackTracking, random_assignment, random_variable

problem = Sudoku()
CSP = BackTracking(problem=problem, var_criterion=random_variable, value_criterion=random_assignment)
initial_state = {"A1": 1, "B1": 2}

# Trying to prune the domains
optimizer = AC3(CSP)
optimizer.run(initial_state)
print(problem.domains)

# Run the backtracking search
state = CSP.run(initial_state)
print(problem.print_state(state))