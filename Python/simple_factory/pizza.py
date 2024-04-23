from abc import ABC, abstractmethod


class Pizza(ABC):
    type: str

    def prepare(self) -> None:
        print(f'Preparing {self.type}')

    def bake(self) -> None:
        print(f'Baking {self.type}')

    def cut(self) -> None:
        print(f'Cutting {self.type}')

    def box(self) -> None:
        print(f'Boxing {self.type}')


class CheesePizza(Pizza):
    def __init__(self):
        self.type = "Cheese Pizza"


class PepperoniPizza(Pizza):
    def __init__(self):
        self.type = "Pepperoni Pizza"
