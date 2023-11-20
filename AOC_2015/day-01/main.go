package main

import (
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func CalcFloor(input string) (int, int) {
	floor := 0
	basement := 0
	for idx, i := range input {
		if i == '(' {
			floor += 1
		}
		if i == ')' {
			floor -= 1
		}
		if floor < 0 && basement == 0 {
			basement = idx + 1
		}
	}
	return floor, basement
}

func main() {
	fmt.Println("Hello, world.")
	data, err := os.ReadFile("./input.txt")
	check(err)
	floor, neg := CalcFloor(string(data))
	fmt.Printf("Floor : %v\nFirst floor where he entered the basement : %v", floor, neg)
}
