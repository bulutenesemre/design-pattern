package strategy

import "fmt"

type Duck struct {
    FlyBehavior FlyBehavior
    QuackBehavior QuackBehavior
}

func (d Duck) PerformFly() {
    d.FlyBehavior.Fly()
}

func (d Duck) PerformQuack() {
    d.QuackBehavior.Quack()
}

func (d Duck) Swim() {
    fmt.Println("All ducks float!")
}

func (d *Duck) SetFlyBehavior(fb FlyBehavior) {
    d.FlyBehavior = fb
}

func (d *Duck) SetQuackBehavior(qb QuackBehavior) {
    d.QuackBehavior = qb
}

type MallardDuck struct {
    Duck
}

func NewMallardDuck() *MallardDuck {
    mallard := &MallardDuck{}
    mallard.FlyBehavior = FlyWithWings{}
    mallard.QuackBehavior = Quack{}
    return mallard
}

func (md MallardDuck) Display() {
    fmt.Println("I'm a Mallard Duck")
}
