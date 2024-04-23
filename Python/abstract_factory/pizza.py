from abc import ABC, abstractmethod
from typing import List

from pizza_ingredient_factory import (
    Cheese,
    Clams,
    Dough,
    Pepperoni,
    PizzaIngredientFactory,
    Sauce,
    Veggies,
)


class Pizza(ABC):
    name: str = None
    dough: Dough = None
    sauce: Sauce = None
    veggies: List[Veggies] = None
    cheese: Cheese = None
    pepperoni: Pepperoni = None
    clam: Clams = None

    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError

    def bake(self) -> None:
        print("Bake for 25 minutes at 350 degree")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        print("Place pizza in official Pizzastore box")

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name


class CheesePizza(Pizza):
    ingredientFactory: PizzaIngredientFactory

    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
        self.veggies = []  # Avoid sharing "veggies" with subclass of class Pizza

    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()


class PepperoniPizza(Pizza):
    ingredientFactory: PizzaIngredientFactory

    def __init__(self, ingredientFactory: PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
        self.veggies = []

    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()
