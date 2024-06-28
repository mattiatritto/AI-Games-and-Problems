import sys
from game.Battleship import Battleship
from game.search import Minimax



# You can play yourself!
game = Battleship('MAX')
game.play("MAX", "MIN")