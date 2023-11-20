package main

import (
	"fmt"
	"os"
	"strings"
)

type Coord struct {
	x, y int
}

func (c *Coord) IsCorner(size int) bool {
	if c.x == 0 || c.x == size-1 {
		if c.y == size-1 || c.y == 0 {
			return true
		}
	}

	return false
}

func (c *Coord) GetNeigh(max int) []Coord {
	coords := [][]int{{c.x - 1, c.y}, {c.x + 1, c.y}, {c.x - 1, c.y - 1}, {c.x + 1, c.y + 1}, {c.x, c.y + 1}, {c.x, c.y - 1}, {c.x - 1, c.y + 1}, {c.x + 1, c.y - 1}}
	coord_val := []Coord{}
outer:
	for _, i := range coords {
		for _, c := range i {
			if c < 0 || c >= max {
				continue outer
			}
		}
		coord_val = append(coord_val, Coord{i[0], i[1]})
	}

	return coord_val

}

type Light struct {
	pos       Coord
	status    bool
	neigh     []Coord
	is_corner bool
}

func InitLight(stat bool, pos Coord, max int, corner bool) *Light {
	n := pos.GetNeigh(max)
	return &Light{pos, stat, n, corner}
}

type Matrix struct {
	lights [][]*Light
}

func InitMatrix(inp []string) Matrix {
	lights := [][]*Light{}
	for y, line := range inp {
		if len(line) <= 1 {
			continue
		}
		size := len(line)
		row := []*Light{}
		for x, block := range strings.Split(line, "") {
			coord := Coord{x, y}
			var light *Light
			corner := coord.IsCorner(size)
			if block == "." {
				if corner {
					light = InitLight(true, coord, size, corner)
				} else {
					light = InitLight(false, coord, size, corner)
				}
			}
			if block == "#" {
				light = InitLight(true, coord, size, corner)
			}
			row = append(row, light)
		}
		lights = append(lights, row)
	}

	return Matrix{lights}
}

func (m *Matrix) GetLight(c Coord) *Light {
	return m.lights[c.y][c.x]
}

func CountOn(lights []*Light) (int, int) {
	on := 0
	off := 0
	for _, light := range lights {
		if light.status {
			on += 1
		} else {
			off += 1
		}
	}

	return on, off

}

func (m *Matrix) GetStats() [][]bool {
	all_status := [][]bool{}
	for _, row := range m.lights {
		statuses := []bool{}
		for _, light := range row {
			neigh := []*Light{}
			for _, coord := range light.neigh {
				neigh = append(neigh, m.GetLight(coord))
			}
			on, _ := CountOn(neigh)

			switch light.status {
			case true:
				if !(on == 2 || on == 3) {
					statuses = append(statuses, false)
				} else {
					statuses = append(statuses, true)
				}
			case false:
				if on == 3 {
					statuses = append(statuses, true)
				} else {
					statuses = append(statuses, false)
				}
			}
		}
		all_status = append(all_status, statuses)
	}
	return all_status
}

func (m *Matrix) ChangeStats(status [][]bool) {
	for y, row := range status {
		for x, s := range row {
			light := m.GetLight(Coord{x, y})
			// the modified step
			if light.is_corner {
				continue
			}
			light.status = s
		}
	}
}

func (m *Matrix) Animate(steps int) {
	for i := 0; i < steps; i++ {
		stats := m.GetStats()
		m.ChangeStats(stats)
	}
}

func (m *Matrix) Print() {
	for _, row := range m.lights {
		for _, light := range row {
			if light.status {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Print("\n")
	}
}

func (m *Matrix) CountOnLights() int {
	count := 0
	for _, i := range m.lights {
		for _, j := range i {
			if j.status {
				count += 1
			}
		}
	}
	return count
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	d, err := os.ReadFile("./input.txt")
	check(err)

	matrix := InitMatrix(strings.Split(string(d), "\r\n"))
	matrix.Animate(100)
	fmt.Println(matrix.CountOnLights())
}
