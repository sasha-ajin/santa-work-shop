from Observable import Observable


class Board(Observable):
    _gnomes = []
    _toys_list = []
    _last_gnome = int()

    def subscribe(self, observer):
        self._gnomes.append(observer)
        observer.set_topic(self)

    def unsubscribe(self, observer):
        self._gnomes.remove(observer)

    def notify_gnomes(self):
        if len(self._gnomes) != 3:
            print("You should have 3 gnomes")
            return "You should have 3 gnomes"
        for i in range(3):
            self._gnomes[i].create_toy(self._toys_list[i])
        self._toys_list = []

    def add_toy_to_list(self, toy):
        self._toys_list.append(toy)
        if len(self._toys_list) == 3:
            self.notify_gnomes()

    def get_update(self):
        return self._topic
