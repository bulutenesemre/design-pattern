from abc import ABC, abstractmethod
from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck(ABC):
    flyBehavior: FlyBehavior
    quackBehavior: QuackBehavior

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError

    def setFlyBehavior(self, fb: FlyBehavior) -> None:
        self.flyBehavior = fb

    def setQuackBehavior(self, qb: QuackBehavior) -> None:
        self.quackBehavior = qb

    def performFly(self) -> None:
        self.flyBehavior.fly()

    def performQuick(self) -> None:
        self.quackBehavior.quack()

    def swim(self) -> None:
        print("All ducks float!")

