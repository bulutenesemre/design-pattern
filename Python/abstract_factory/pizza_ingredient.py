class Dough:
    def toString(self) -> str:
        pass


class ThickCrustDough(Dough):
    def toString(self) -> str:
        return "ThickCrust stype extra thick crust dough"


class ThinCrustDough(Dough):
    def toString(self) -> str:
        return "Thin Crust Dough"


class Sauce:
    def toString(self) -> str:
        pass


class PlumTomatoSauce(Sauce):
    def toString(self) -> str:
        return "Tomato sauce with plum tomatoes"


class MarinaraSauce(Sauce):
    def toString(self) -> str:
        return "Marinara Sauce"


class Cheese:
    def toString(self) -> str:
        pass


class ReggianoCheese(Cheese):
    def toString(self) -> str:
        return "Reggiano Cheese"


class MozzarellaCheese(Cheese):
    def toString(self) -> str:
        return "Shredded Mozzarella"


class Veggies:
    def toString(self) -> str:
        pass


class BlackOlives(Veggies):
    def toString(self) -> str:
        return "Black Olives"


class Eggplant(Veggies):
    def toString(self) -> str:
        return "Eggplant"


class Spinach(Veggies):
    def toString(self) -> str:
        return "Spinach"


class Garlic(Veggies):
    def toString(self) -> str:
        return "Garlic"


class Onion(Veggies):
    def toString(self) -> str:
        return "Onion"


class Mushroom(Veggies):
    def toString(self) -> str:
        return "Mushrooms"


class RedPepper(Veggies):
    def toString(self) -> str:
        return "Red Pepper"


class Pepperoni:
    def toString(self) -> str:
        pass


class SlicedPepperoni(Pepperoni):
    def toString(self) -> str:
        return "Sliced Pepperoni"


class Clams:
    def toString(self) -> str:
        pass


class FreshClams(Clams):
    def toString(self) -> str:
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def toString(self) -> str:
        return "Frozen Clams from Chesapeake Bay"
