from Gnome import Gnome
from Board import Board
from SantaClaus import SantaClaus

santa_claus = SantaClaus()
board = Board()
santa_claus.set_board(board)

gnome1 = Gnome("gnome1 John")
gnome2 = Gnome("gnome2 Bill")
gnome3 = Gnome("gnome3 Steve")

santa_claus.hire_gnome(gnome1)
santa_claus.hire_gnome(gnome2)
santa_claus.hire_gnome(gnome3)

santa_claus.add_toy_to_list("Bicycle")
santa_claus.add_toy_to_list("Bicycle")
santa_claus.add_toy_to_list("Doll")
santa_claus.add_toy_to_list("Bicycle")

# Bicycle was created by gnome1 John
# Bicycle was created by gnome2 Bill
# Doll was created by gnome3 Steve
# Bicycle was created by gnome1 John
