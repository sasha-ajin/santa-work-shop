from ToyCommand import ToyCommand
from BicycleFactory import BicycleFactory


class BicycleCommand(ToyCommand):
    _bicycle_factory = BicycleFactory()

    def execute(self):
        self._bicycle_factory.create_toy()
