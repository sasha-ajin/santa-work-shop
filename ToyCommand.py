from abc import ABC, abstractmethod


class ToyCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
