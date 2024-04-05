package strategy

import "fmt"

type QuackBehavior interface {
	Quack()
}

type Quack struct{}

func(q Quack) Quack() {
	fmt.Println("Quack!")
}

type Squeak struct{}

func(s Squeak) Quack() {
	fmt.Println("Squeak!")
}

type MuteQuack struct{}

func(mq MuteQuack) Quack() {
	fmt.Println("Can't Quack!")
}