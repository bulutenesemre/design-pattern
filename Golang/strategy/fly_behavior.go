package strategy

import "fmt"

type FlyBehavior interface {
	Fly()
}

type FlyWithWings struct{}

func(fww FlyWithWings) Fly() {
	fmt.Println("I am flying!")
}

type FlyNoWay struct{}

func(fnw FlyNoWay) Fly() {
	fmt.Println("I can't fly")
}

type FlyRocketPowered struct{}

func(frp FlyRocketPowered) Fly() {
	fmt.Println("I'm flying with a rocket!")
}
