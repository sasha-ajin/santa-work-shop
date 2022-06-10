from abc import ABC, abstractmethod
from Toy import Toy

class ToyFactory(ABC):
    @abstractmethod
    def create_toy(self) -> Toy:
        pass
    