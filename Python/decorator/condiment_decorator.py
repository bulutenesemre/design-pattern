from abc import abstractmethod

from beverage import Beverage


class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError
