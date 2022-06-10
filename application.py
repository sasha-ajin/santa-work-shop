from BicycleFactory import BicycleFactory
from Gnome import Gnome
from Board import Board

board = Board()
gnome1 = Gnome("gnome1")
gnome2 = Gnome("gnome2")
gnome3 = Gnome("gnome3")
board.subscribe(gnome1)
board.subscribe(gnome2)
board.subscribe(gnome3)

board.add_toy_to_list("Bicycle")
board.add_toy_to_list("Doll")
board.add_toy_to_list("Bicycle")
board.add_toy_to_list("Doll")  

