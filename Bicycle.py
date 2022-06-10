from Toy import Toy

class Bicycle(Toy):
    def __init__(self):
        super().__init__("Bicycle")
    def __str__(self) -> str:
        return "Bicycle"

