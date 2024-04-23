from abc import ABC, abstractmethod

from pizza import CheesePizza, PepperoniPizza, Pizza
from pizza_ingredient_factory import (
    ChicagoPizzaIngredientFactory,
    NYPizzaIngredientFactory,
    PizzaIngredientFactory,
)


class PizzaStore(ABC):
    @abstractmethod
    def _createPizza(self, item: str) -> Pizza:
        raise NotImplementedError

    def orderPizza(self, type_: str) -> Pizza:
        pizza: Pizza = self._createPizza(type_)
        print(f"--- Making a {pizza.getName()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):

    def _createPizza(self, item: str) -> Pizza:
        pizza: Pizza = None
        ingredientFactory: PizzaIngredientFactory = NYPizzaIngredientFactory()

        if item == "cheese":

            pizza = CheesePizza(ingredientFactory)
            pizza.setName("New York Style Cheese Pizza")

        elif item == "pepperoni":

            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("New York Style Pepperoni Pizza")

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def _createPizza(self, item: str) -> Pizza:
        pizza: Pizza = None
        ingredientFactory: PizzaIngredientFactory = ChicagoPizzaIngredientFactory()

        if item == "cheese":

            pizza = CheesePizza(ingredientFactory)
            pizza.setName("Chicago style Cheese Pizza")

        elif item == "pepperoni":

            pizza = PepperoniPizza(ingredientFactory)
            pizza.setName("Chicago style Pepperoni Pizza")

        return pizza
