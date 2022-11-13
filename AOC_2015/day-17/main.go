package main

import (
	"fmt"
	"os"
	"strings"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func Intify(strs []string) []int {
	ints := []int{}
	for _, s := range strs {
		no, _ := strconv.Atoi(s)
		ints = append(ints, no)	
	}
	return ints
}

func Possibilities(list []int) int {
	count := 0
	for i:=0; i<1<<len(list); i++{
		t := i
		s := 0

		for _, j := range list {
			if t % 2 == 1 {
				s += j
			}
			t /= 2
		}
		if s == 150 {
			count += 1
		}
	}
	return count
}

func main() {
	d, err := os.ReadFile("./input.txt")
	check(err)
	split := strings.Split(string(d), "\r\n")
	split = split[:len(split) - 1]
	new := Intify(split)
	fmt.Println(Possibilities(new))
	fmt.Println("Hello World")
}
