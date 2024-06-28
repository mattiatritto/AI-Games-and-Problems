from search.Node import Node



class GraphSearch:

    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []
        self.visited = []

    def __repr__(self):
        return 'Graph Search'

    def run(self):

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        while True:

            if self.problem.goal_test(node.state):
                return 'Ok', node

            self.visited.append(node.state)

            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=self.problem.cost(node.state, a)) for s, a in new_states]

            new_nodes = [n for n in new_nodes if n.state not in self.visited]
            self.fringe = [n for n in self.fringe if n.state not in self.visited]

            self.fringe = self.fringe + new_nodes

            if len(self.fringe) != 0:
                self.fringe, node = self.strategy.select(fringe=self.fringe)
                if node is None:
                    return 'Fail', []
            else:
                if self.problem.goal_test(node.state):
                    return 'Ok', node
                else:
                    return 'Fail', []