from pizza import Pizza
from pizza_factory import SimplePizzaFactory
from pizza_store import PizzaStore


class PizzaTestDrive:
    @staticmethod
    def main(*args) -> None:
        factory: SimplePizzaFactory = SimplePizzaFactory()
        store: PizzaStore = PizzaStore(factory)

        pizza: Pizza = store.order_pizza("cheese")
        print(f"We ordered a {pizza.type}\n")

        pizza = store.order_pizza("pepperoni")
        print(f"We ordered a {pizza.type}\n")


if __name__ == "__main__":
    PizzaTestDrive.main()
