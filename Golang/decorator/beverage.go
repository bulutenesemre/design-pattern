package decorator

type Beverage interface {
	Cost() float64
	GetDescription() string
}


type DarkRoast struct{}

func NewDarkRoast() Beverage {
	return &DarkRoast{}
} 

func (dr *DarkRoast) Cost() float64 {
	return 0.99
}

func (dr *DarkRoast) GetDescription() string {
	return "Dark Roast Coffee"
}

type Espresso struct{}

func NewEspresso() Beverage {
    return &Espresso{}
}

func (e *Espresso) Cost() float64 {
	return 1.99
}

func (e *Espresso) GetDescription() string {
	return "Espresso"
}

