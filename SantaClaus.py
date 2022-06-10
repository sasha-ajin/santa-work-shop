from Gnome import Gnome
from Board import Board


class SantaClaus:
    __instance = None
    _board = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(SantaClaus, cls).__new__(cls)
        return cls.__instance

    def set_board(self, board: Board):
        self._board = board

    def hire_gnome(self, gnome: Gnome):
        self._board.subscribe(gnome)

    def add_toy_to_list(self, toy: str):
        self._board.add_toy_to_list(toy)

    def get_board(self):
        return self._board
