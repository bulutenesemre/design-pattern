from typing import List

from pizza_ingredient import Cheese, Clams, Dough, Pepperoni, Sauce, Veggies, ThickCrustDough, MarinaraSauce, \
    ReggianoCheese, Garlic, Onion, Mushroom, RedPepper, SlicedPepperoni, FreshClams, PlumTomatoSauce, \
    MozzarellaCheese, BlackOlives, Spinach, Eggplant, FrozenClams


class PizzaIngredientFactory:

    def createDough(self) -> Dough:
        pass

    def createSauce(self) -> Sauce:
        pass

    def createCheese(self) -> Cheese:
        pass

    def createVeggies(self) -> List[Veggies]:
        pass

    def createPepperoni(self) -> Pepperoni:
        pass

    def createClams(self) -> Clams:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self) -> Dough:
        return ThickCrustDough()

    def createSauce(self) -> Sauce:
        return MarinaraSauce()

    def createCheese(self) -> Cheese:
        return ReggianoCheese()

    def createVeggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createClams(self) -> Clams:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self) -> Dough:
        return ThickCrustDough()

    def createSauce(self) -> Sauce:
        return PlumTomatoSauce()

    def createCheese(self) -> Cheese:
        return MozzarellaCheese()

    def createVeggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createClams(self) -> Clams:
        return FrozenClams()
