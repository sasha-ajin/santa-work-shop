from ToyCommand import ToyCommand
from DollFactory import DollFactory


class DollCommand(ToyCommand):
    _doll_factory = DollFactory()

    def execute(self):
        self._doll_factory.create_toy()
