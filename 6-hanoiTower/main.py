from search.Problems import HanoiTowerProblem
from search.strategies import BreadthFirst, DepthFirst, UniformCost, Greedy, AStar
from search.GraphSearch import GraphSearch

initial_state = {
    'tow1': [2, 3],
    'tow2': [1],
    'tow3': [4]
}

goal_state = {
    'tow1': [4, 3, 2, 1],
    'tow2': [],
    'tow3': []
}

problem = HanoiTowerProblem(initial_state, goal_state)
strategies = [BreadthFirst, AStar(problem), Greedy(problem), BreadthFirst, DepthFirst, UniformCost]

for strategy in strategies:
    search = GraphSearch(problem, strategy)
    res = search.run()
    print(res[1].path())