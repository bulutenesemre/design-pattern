package simple_factory

import "fmt"


type pizzaStore struct {
	factory pizzaFactory
}


func NewPizzaStore(factory pizzaFactory) *pizzaStore {
	return &pizzaStore{
		factory: factory,
	}
}


func (ps *pizzaStore) OrderPizza(pizzaType string) {

	if pizza, err := ps.factory.CreatePizza(pizzaType); err != nil {
		fmt.Println(err.Error())
	} else {
		pizza.Prepare()
		pizza.Bake()
		pizza.Cut()
		pizza.Box()
	}
}