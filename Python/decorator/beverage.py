from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str = "Unknown Beverage"

    def getDescription(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class Espresso(Beverage):
    def __init__(self):
        self.description = "Expresso"

    def cost(self) -> float:
        return 1.99


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99
