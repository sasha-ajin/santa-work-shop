from Observable import Observable


class Board(Observable):
    _gnomes = []
    _toy = ""
    _duty_gnome = int()

    def subscribe(self, observer):
        self._gnomes.append(observer)
        observer.set_topic(self)

    def unsubscribe(self, observer):
        self._gnomes.remove(observer)

    def notify_gnomes(self):
        if len(self._gnomes) != 3:
            print("You should have 3 gnomes")
            return "You should have 3 gnomes"
        self._gnomes[self._duty_gnome].create_toy(self._toy)
        if self._duty_gnome == 2:
            self._duty_gnome = 0
        else:
            self._duty_gnome +=1


    def add_toy_to_list(self, toy):
        self._toy = toy
        self.notify_gnomes()

    def get_update(self):
        return self._topic
