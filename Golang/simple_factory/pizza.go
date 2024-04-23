package simple_factory

import "fmt"

type IPizza interface {
	Prepare()
	Bake()
	Cut()
	Box()
}

type pizza struct {
	pizzaType string
}

func (p *pizza) Prepare() {
	fmt.Printf("Preparing %s \n",p.pizzaType)
}

func (p *pizza) Bake() {
	fmt.Printf("Baking %s \n", p.pizzaType)
}

func (p *pizza) Cut() {
	fmt.Printf("Cutting %s \n", p.pizzaType)
}

func (p *pizza) Box() {
	fmt.Printf("Boxing %s \n", p.pizzaType)
}

type CheesePizza struct {
	*pizza
}

func NewCheesePizza() IPizza {
	p := &pizza{
		pizzaType: "Cheese",
	}

	return &CheesePizza{
		pizza: p,
	}
}

type PepperoniPizza struct {
	*pizza
}

func NewPepperoniPizza() IPizza{
	p := &pizza{
		pizzaType: "Pepperoni",
	}

	return &PepperoniPizza{
		pizza: p,
	}
}
