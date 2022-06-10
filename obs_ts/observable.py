from abc import ABC, abstractmethod


class Observable:
    @abstractmethod
    def subscribe(self, observers):
        pass

    @abstractmethod
    def unsubscribe(self, observers):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def get_update(self):
        pass
