from pizza import CheesePizza, PepperoniPizza, Pizza


class SimplePizzaFactory:

    def create_pizza(self, type_: str) -> Pizza:
        pizza: Pizza = None
        if type_ == "cheese":
            pizza = CheesePizza()
        elif type_ == "pepperoni":
            pizza = PepperoniPizza()
        return pizza
