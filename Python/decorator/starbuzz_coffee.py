from beverage import Beverage, DarkRoast, Espresso
from decorator import Milk, Mocha, Soy, Whip


class StarbuzzCoffee:
    @staticmethod
    def main(*args) -> None:
        beverage: Beverage = Espresso()
        print("{} {}".format(beverage.getDescription(), beverage.cost()))
        beverage2: Beverage = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print("{} {}".format(beverage2.getDescription(), beverage2.cost()))


if __name__ == "__main__":
    StarbuzzCoffee.main()
