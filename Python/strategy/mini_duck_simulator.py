from fly_behavior import FlyRocketPowered
from mallard_duck import MallardDuck


class MiniDuckSimulator:
    @staticmethod
    def main(*args):
        mallard: MallardDuck = MallardDuck()

        mallard.performQuick()
        mallard.display()
        mallard.performFly()
        mallard.setFlyBehavior(FlyRocketPowered())  # Manipulate behavior of mallard duck
        mallard.performFly()
        mallard.swim()


if __name__ == "__main__":
    MiniDuckSimulator.main()
