from ToyFactory import ToyFactory
from Doll import Doll
from Toy import Toy


class DollFactory(ToyFactory):
    def create_toy(self) -> Toy:
        doll = Doll()
        print(doll, "was created", end=" ")
        return doll

