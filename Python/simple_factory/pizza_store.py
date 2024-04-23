from pizza import Pizza
from pizza_factory import SimplePizzaFactory


class PizzaStore:
    factory: SimplePizzaFactory

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, type_: str) -> Pizza:
        pizza: Pizza

        pizza = self.factory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
