from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def create_toy(self):
        pass

   