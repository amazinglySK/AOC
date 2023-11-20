package main

import (
	"fmt"
	//"math"
)

func GetFactorSum(n int) int {
	sum := 0
	for i:=1; i<= n; i++ {
		if n % i == 0 {
			sum += i
		}
	}
	return sum 
}

func GetLeastHouseWithScore(n int) int {
	i := 1 
	found := false

	for !found {
		score := GetFactorSum(i)*10 
		
		if score >= n {
			found = true
			break
		}
		i+=1
	}

	return i
}

func main() {
	fmt.Println("Hello World")
	input := 36000000 
	fmt.Println(GetLeastHouseWithScore(input))
}
