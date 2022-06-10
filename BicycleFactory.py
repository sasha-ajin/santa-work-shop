from ToyFactory import ToyFactory
from Bicycle import Bicycle
from Toy import Toy


class BicycleFactory(ToyFactory):
    def create_toy(self) -> Toy:
        bicycle = Bicycle()
        print(bicycle, "was created", end=" ")
        return bicycle
    
