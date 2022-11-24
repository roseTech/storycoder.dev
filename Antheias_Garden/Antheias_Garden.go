package main

import (
	"fmt"
)

func main() {
	lilies := 1
	for night := 1; night < 29; night += 1 {
		lilies = lilies * 2
	}
	fmt.Println(lilies)
}
