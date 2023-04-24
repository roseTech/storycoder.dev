package main

import "fmt"

func main() {
	const iterations = 10
	const p = 7

	sum := 0
	for i := 0; i < iterations; i++ {
		sum += ((i + 1) * p)
	}

	fmt.Println(sum)
}
