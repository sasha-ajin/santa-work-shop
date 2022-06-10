from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observers):
        pass

    @abstractmethod
    def unsubscribe(self, observers):
        pass

    @abstractmethod
    def add_toy_to_list(self):
        pass

    @abstractmethod
    def get_update(self):
        pass
