package main

import (
	"day-09/helpers/conns"
	"day-09/helpers/slices"
	"fmt"
	"os"
	"strings"
)

func ParseCities(routes []string) []string {
	cityList := []string{}
	for _, route := range routes {
		routeSplit := strings.Split(route, " ")
		cities := []string{routeSplit[0], routeSplit[2]}
		for _, city := range cities {
			if !slices.Includes(cityList, city) {
				cityList = append(cityList, city)
			}
		}
	}
	return cityList
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	data, err := os.ReadFile("./input.txt")
	check(err)
	lines := strings.Split(string(data), "\r\n")
	cities := ParseCities(lines)
	connections := conns.ParseConnections(lines)
	routes := conns.GetAllValidRoutes(connections, cities)
	fmt.Println(conns.GetMinPath(routes))
	fmt.Println(conns.GetMaxPath(routes))
}
