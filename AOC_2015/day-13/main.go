package main

import (
	"fmt"
	"strings"
	"strconv"
	"day-13/helpers/permut"
	"os"
)


type PeopleConn struct {
	main string
	to string
	cost int
}


func includes(list []string, el string) bool {
	
	for _, i := range list {
		if i == el {
			return true
		}
	}

	return false
}

func ParsePeople(people []string) []string {
	people_list := []string{}
	for _, desc := range people {
		split := strings.Split(desc, " ")
		if len(split) <= 1 {
			continue
		}
		peeps := []string{split[0], split[len(split)-1]}
		for _, peep := range peeps {
			if !includes(people_list, peep){
				people_list = append(people_list, peep)
			}
		}
	}
	return people_list
}

func ParsePeopleConn(people []string) []PeopleConn {
	conns := []PeopleConn{}
	for _, desc := range people {
		split := strings.Split(desc, " ")
		if len(split) < 2 {
			continue
		}
		first, sign, cost, second := split[0], split[2], split[3], split[len(split)-1]
		var intCost int
		switch sign {
		case "gain":
			intCost, _ = strconv.Atoi(cost)
		case "lose":
			raw, _ := strconv.Atoi(cost)
			intCost = 0-raw
		}
		conns = append(conns, PeopleConn{first, second, intCost})

	}

	return conns

}

func FindHappiness(first string, second string, conns *[]PeopleConn) int {
	if first == "You" || second == "You" {
		return 0
	}
	for _, conn := range *conns {
		if conn.main == first && conn.to == second {
			return conn.cost
		}
	}
	return 0
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	d, err := os.ReadFile("./input.txt") 
	check(err)
	lines := strings.Split(string(d), ".\r\n")

	conns := ParsePeopleConn(lines) 
	people := ParsePeople(lines)
	happiness := 0
	for perm := range permut.GetPerms(people) {
		curr := 0
		for idx, peep := range perm {
			var first, second string 
			if idx == len(perm) - 1 {
				first, second = peep, perm[0]
			} else {
				first, second = peep, perm[idx + 1]
			}
			curr += FindHappiness(first, second, &conns)
			curr += FindHappiness(second, first, &conns)
		}
		if curr > happiness {
			happiness = curr
		}
	}
	
	fmt.Println(happiness)

	people = append(people, "You")
	happiness = 0

	for perm := range permut.GetPerms(people) {
		curr := 0
		for idx, peep := range perm {
			var first, second string 
			if idx == len(perm) - 1 {
				first, second = peep, perm[0]
			} else {
				first, second = peep, perm[idx + 1]
			}
			curr += FindHappiness(first, second, &conns)
			curr += FindHappiness(second, first, &conns)
		}
		if curr > happiness {
			happiness = curr
		}
	}

	fmt.Println(happiness)
	fmt.Println("Hello, World")
}

