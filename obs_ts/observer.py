from abc import ABC, abstractmethod


class Observer:
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def set_topic(self, topic):
        pass
