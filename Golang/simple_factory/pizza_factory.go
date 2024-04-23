package simple_factory

import "fmt"

type pizzaFactory interface {
	CreatePizza(pizzaType string) (IPizza, error)
}

type SimplePizzaFactory struct {}

func (spf *SimplePizzaFactory) CreatePizza(pizzaType string) (IPizza, error) {
	switch pizzaType {
	case "cheese":
		return NewCheesePizza(), nil
	case "pepperoni":
		return NewPepperoniPizza(), nil
	}

	return nil, fmt.Errorf("invalid pizza type")

}