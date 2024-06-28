from search.Problems import NTiles
from search.strategies import AStar, DepthFirst
from search.GraphSearch import GraphSearch

EightTilesProblem = NTiles(n_tiles=8)

strategies = [AStar(EightTilesProblem)]
for strategy in strategies:
    search = GraphSearch(EightTilesProblem, strategy)
    print(strategy)
    res = search.run()
    print(res[1].path())