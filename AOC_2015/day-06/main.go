package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Light struct {
	x          int
	y          int
	status     bool
	brightness int
}

type Grid struct {
	lights [][]*Light
	rows   int
	cols   int
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func convert_to_int(arr []string) []int {
	results := []int{}
	for _, i := range arr {
		res, err := strconv.Atoi(i)
		check(err)
		results = append(results, res)
	}
	return results
}

func NewGrid(rows int, cols int) Grid {
	grid_lights := [][]*Light{}
	for i := 0; i < rows; i++ {
		light_row := []*Light{}
		for j := 0; j < cols; j++ {
			light := Light{i, j, false, 0}
			light_row = append(light_row, &light)
		}
		grid_lights = append(grid_lights, light_row)
	}
	return Grid{
		grid_lights,
		rows,
		cols,
	}
}

func (g *Grid) GetRange(start string, end string) []*Light {
	start_coords := convert_to_int(strings.Split(start, ","))
	s_x, s_y := start_coords[0], start_coords[1]
	end_coords := convert_to_int(strings.Split(end, ","))
	e_x, e_y := end_coords[0], end_coords[1]
	result := []*Light{}
	for _, i := range g.lights[s_y : e_y+1] {
		for _, j := range i[s_x : e_x+1] {
			result = append(result, j)
		}
	}

	return result

}

func (g *Grid) Binary(cmd string, rng string) {
	rng_split := strings.Split(rng, " through ")
	start, end := rng_split[0], rng_split[1]
	light_rng := g.GetRange(start, end)
	switch cmd {
	case "toggle":
		for _, i := range light_rng {
			i.status = !i.status
		}
	case "turn on":
		for _, i := range light_rng {
			i.status = true
		}
	case "turn off":
		for _, i := range light_rng {
			i.status = false
		}
	}
}

func (g *Grid) BrightnessControl(cmd string, rng string) {
	rng_split := strings.Split(rng, " through ")
	start, end := rng_split[0], rng_split[1]
	light_rng := g.GetRange(start, end)
	switch cmd {
	case "toggle":
		for _, i := range light_rng {
			i.brightness += 2
		}
	case "turn on":
		for _, i := range light_rng {
			i.brightness += 1
		}
	case "turn off":
		for _, i := range light_rng {
			i.brightness -= 1
			if i.brightness < 0 {
				i.brightness = 0
			}
		}
	}
}

func (g *Grid) CountOnLights() int {
	count := 0
	for _, i := range g.lights {
		for _, j := range i {
			if j.status {
				count += 1
			}
		}
	}
	return count
}

func (g *Grid) BrightnessTotal() int {
	count := 0
	for _, i := range g.lights {
		for _, j := range i {
			count += j.brightness
		}
	}
	return count
}

func (g *Grid) ParseCmds(cmds []string) {
	for _, cmd := range cmds {
		cmd_split := strings.Split(cmd, " ")
		switch cmd_split[0] {
		case "turn":
			command := strings.Join(cmd_split[0:2], " ")
			input := strings.Join(cmd_split[2:], " ")
			g.Binary(command, input)
			g.BrightnessControl(command, input)
		case "toggle":
			command := cmd_split[0]
			input := strings.Join(cmd_split[1:], " ")
			g.Binary(command, input)
			g.BrightnessControl(command, input)
		}
	}
}

func main() {
	grid := NewGrid(1000, 1000)
	data, err := os.ReadFile("./input.txt")
	check(err)
	lines := strings.Split(string(data), "\r\n")
	grid.ParseCmds(lines)
	fmt.Printf("%v\n", grid.CountOnLights())
	fmt.Printf("%v\n", grid.BrightnessTotal())
}
