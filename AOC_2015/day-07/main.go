package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

type Wire struct {
	name      string
	signal    uint16
	signalled bool
	cmd       string
}

func (w *Wire) Equal(wire Wire) bool {
	return w.name == wire.name
}

func OnlyInts(str string) bool {
	for _, r := range str {
		if !unicode.IsDigit(r) {
			return false
		}
	}
	return true
}

func GetInitials(cmds []string) map[string]*Wire {
	wires := map[string]*Wire{}
	for _, cmd := range cmds {
		splitted := strings.Split(cmd, " -> ")
		lhs, rhs := splitted[0], splitted[1]
		rhs_wire := Wire{}
		rhs_wire.name = rhs
		rhs_wire.cmd = lhs
		if OnlyInts(lhs) {
			normal_int, _ := strconv.Atoi(lhs)
			rhs_wire.signal = uint16(normal_int)
			rhs_wire.signalled = true
		} else {
			rhs_wire.signalled = false
		}
		wires[rhs] = &rhs_wire
	}
	return wires
}

func ProcessWires(wires map[string]*Wire, wire string) uint16 {
	for _, wire := range wires {
		if wire.signalled {
			continue
		}
		operator, inputs := ProcessCommand(wire.cmd)
		real_inp := []uint16{}
		for _, i := range inputs {
			if OnlyInts(i) {
				i, _ := strconv.Atoi(i)
				real_inp = append(real_inp, uint16(i))
				continue
			}

			if wires[i].signalled {
				real_inp = append(real_inp, wires[i].signal)
			}
		}

		if len(real_inp) == len(inputs) {
			signal := RunCommand(operator, real_inp)
			wire.signal = signal
			wire.signalled = true
		}
	}

	if !wires[wire].signalled {
		return ProcessWires(wires, wire)
	}

	return wires[wire].signal

}

func RunCommand(op string, values []uint16) uint16 {
	var result uint16
	switch op {
	case "LSHIFT":
		result = values[0] << values[1]
	case "RSHIFT":
		result = values[0] >> values[1]
	case "AND":
		result = values[0] & values[1]
	case "OR":
		result = values[0] | values[1]
	case "NOT":
		result = ^values[0]
	case "PUT":
		result = values[0]
	}
	return result
}

func ProcessCommand(cmd string) (string, []string) {
	split := strings.Split(cmd, " ")
	if len(split) == 1 {
		return "PUT", []string{cmd}
	}
	if split[0] == "NOT" {
		return split[0], []string{split[1]}
	}
	op := split[1]
	return op, []string{split[0], split[2]}
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	data, err := os.ReadFile("./input.txt")
	check(err)
	lines := strings.Split(string(data), "\r\n")
	wires := GetInitials(lines)
	values := ProcessWires(wires, "a")
	fmt.Println(values)
	data, err = os.ReadFile("./next_input.txt")
	check(err)
	lines = strings.Split(string(data), "\r\n")
	wires = GetInitials(lines)
	values = ProcessWires(wires, "a")
	fmt.Println(values)

}
