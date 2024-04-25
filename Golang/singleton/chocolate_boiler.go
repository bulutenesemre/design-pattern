package singleton

import "fmt"


type ChocolateBoiler struct {
	empty bool
	boiled bool
}

var uniqueInstance *ChocolateBoiler

func NewChocolateBoiler() *ChocolateBoiler {
	if uniqueInstance == nil {
		fmt.Println("Creating unique instance of Chocolate Boiler")
		uniqueInstance = &ChocolateBoiler{
			empty: true,
			boiled: false,
		}
	}
	fmt.Println("Returning instance of Chocolate Boiler")
	return uniqueInstance
}

func (cb *ChocolateBoiler) Fill() {
	if cb.IsEmpty() {
		cb.empty = false
		cb.boiled = false
	}
}

func (cb *ChocolateBoiler) Drain() {
	if !cb.IsEmpty() && !cb.IsBoiled() {
		cb.empty = true
	}
}

func (cb *ChocolateBoiler) Boil() {
	if !cb.IsEmpty() && !cb.IsBoiled(){
		cb.boiled = true
	} 
}

func (cb *ChocolateBoiler) IsEmpty() bool {
	return cb.empty
}

func(cb *ChocolateBoiler) IsBoiled() bool {
	return cb.boiled
}