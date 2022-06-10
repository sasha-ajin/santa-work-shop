from Toy import Toy

class Doll(Toy):
    def __init__(self):
        super().__init__("Doll")
    def __str__(self) -> str:
        return "Doll"
