from BicycleCommand import BicycleCommand
from DollCommand import DollCommand
from Observer import Observer


class Gnome(Observer):
    _name = ""
    _subscribed_to = []

    def __init__(self, name):
        self._name = name

    def create_toy(self, command):
        if command == "Bicycle":
            command = BicycleCommand()
        elif command == "Doll":
            command = DollCommand()
        command.execute()
        print(f"by {self._name}")

    def set_topic(self, topic):
        self._subscribed_to = topic