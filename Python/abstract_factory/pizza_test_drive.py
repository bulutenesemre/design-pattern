from pizza import Pizza
from pizza_store import ChicagoPizzaStore, NYPizzaStore, PizzaStore


class PizzaTestDrive:
    @staticmethod
    def main(*args):
        nyStore: PizzaStore = NYPizzaStore()
        chicagoStore: PizzaStore = ChicagoPizzaStore()

        pizza: Pizza = nyStore.orderPizza("cheese")
        print(f"Enes ordered a pizza {pizza.getName()}")

        pizza2: Pizza = chicagoStore.orderPizza("pepperoni")
        print(f"Enes ordered a pizza {pizza2.getName()}")


if __name__ == "__main__":
    PizzaTestDrive.main()
