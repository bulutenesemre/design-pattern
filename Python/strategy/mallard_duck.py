from duck import Duck
from fly_behavior import FlyWithWings
from quack_behavior import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self) -> None:
        print("I am a real Mallard Duck")
