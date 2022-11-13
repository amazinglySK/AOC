package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func CalcAreaAndRibbon(order string) (int, int) {
	dimensions := strings.Split(order, "x")
	int_dimension := []int{}
	for _, i := range dimensions {
		val, err := strconv.Atoi(i)
		check(err)
		int_dimension = append(int_dimension, val)
	}
	sort.Ints(int_dimension)

	min_area := int_dimension[0] * int_dimension[1]

	TSA := 2 * (int_dimension[0]*int_dimension[1] + int_dimension[1]*int_dimension[2] + int_dimension[2]*int_dimension[0])

	perimeter := 2 * (int_dimension[0] + int_dimension[1])
	ribbon := int_dimension[0] * int_dimension[1] * int_dimension[2]

	return TSA + min_area, perimeter + ribbon
}

func main() {

	data, err := os.ReadFile("./input.txt")
	check(err)
	order_wrapping_paper := 0
	order_ribbon := 0
	lines := strings.Split(string(data), "\r\n")
	fmt.Printf("%v\n", lines[0])
	for _, ord := range lines {
		wp, rb := CalcAreaAndRibbon(ord)
		order_wrapping_paper += wp
		order_ribbon += rb
	}

	fmt.Printf("Amount of wrapping paper required : %v\n", order_wrapping_paper)
	fmt.Printf("Amount of ribbon required : %v\n", order_ribbon)

}
