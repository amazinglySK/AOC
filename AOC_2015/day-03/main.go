package main

import (
	"fmt"
	"os"
)

func Contains[T comparable](arr []T, elem T) bool {
	for _, i := range arr {
		if i == elem {
			return true
		}
	}
	return false
}

type Location struct {
	x int
	y int
}

type Santa struct {
	location Location
}

func (orig *Location) Equal(e Location) bool {
	return orig.x == e.x && orig.y == e.y
}

func SimulateTrip(directions string) int {
	visited := []Location{Location{0, 0}}
	curr_x, curr_y := 0, 0
	for _, dir := range directions {
		switch dir {
		case '^':
			curr_y -= 1
		case '>':
			curr_x += 1
		case '<':
			curr_x -= 1
		case 'v':
			curr_y += 1
		}
		point := Location{curr_x, curr_y}

		if !Contains(visited, point) {
			visited = append(visited, point)
		}

	}
	return len(visited)
}
func SimulateTripWithRobot(directions string) int {
	visited := []Location{Location{0, 0}}
	var (
		curr_x *int
		curr_y *int
	)
	santa := Santa{Location{0, 0}}
	robot := Santa{Location{0, 0}}
	for idx, dir := range directions {
		if idx%2 == 0 {
			curr_x, curr_y = &santa.location.x, &santa.location.y
		} else {
			curr_x, curr_y = &robot.location.x, &robot.location.y
		}
		switch dir {
		case '^':
			*curr_y -= 1
		case '>':
			*curr_x += 1
		case '<':
			*curr_x -= 1
		case 'v':
			*curr_y += 1
		}
		point := Location{*curr_x, *curr_y}

		if !Contains(visited, point) {
			visited = append(visited, point)
		}

	}
	return len(visited)
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	data, err := os.ReadFile("./input.txt")
	check(err)
	houses := SimulateTrip(string(data))
	fmt.Printf("No. of houses visited : %v\n", houses)
	houses = SimulateTripWithRobot(string(data))
	fmt.Printf("No. of houses visited with the robot: %v\n", houses)

}
