package decorator

type CondimentDecorator interface {
	Beverage
	AddOnDescription() string
}

type Milk struct {
	beverage Beverage
}

func NewMilk(beverage Beverage) Beverage {
	return &Milk{beverage: beverage}
}

func (m *Milk) Cost() float64 {
	return 0.1 + m.beverage.Cost()
}

func (m *Milk) GetDescription() string {
	return m.beverage.GetDescription() + m.AddOnDescription()
}

func (m *Milk) AddOnDescription() string {
	return "\n + AddOn Milk"
}

type Mocha struct {
	beverage Beverage
}

func NewMocha(beverage Beverage) Beverage {
	return &Mocha{beverage: beverage}
}

func (m *Mocha) Cost() float64 {
	return 0.2 + m.beverage.Cost()
}

func (m *Mocha) GetDescription() string {
	return m.beverage.GetDescription() + m.AddOnDescription()
}

func (m *Mocha) AddOnDescription() string {
	return "\n + AddOn Mocha"
}

type Whip struct {
	beverage Beverage
}

func NewWhip(beverage Beverage) Beverage {
	return &Whip{beverage: beverage}
}

func (m *Whip) Cost() float64 {
	return 0.2 + m.beverage.Cost()
}

func (m *Whip) GetDescription() string {
	return m.beverage.GetDescription() + m.AddOnDescription()
}

func (m *Whip) AddOnDescription() string {
	return "\n + AddOn Whip"
}