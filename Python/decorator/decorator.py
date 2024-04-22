from beverage import Beverage
from condiment_decorator import CondimentDecorator


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Milk'

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Mocha'

    def cost(self) -> float:
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Soy'

    def cost(self) -> float:
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', Whip'

    def cost(self) -> float:
        return 0.10 + self.beverage.cost()
