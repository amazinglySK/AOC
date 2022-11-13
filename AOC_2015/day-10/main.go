package main

import (
	"fmt"
	"strconv"
	"strings"
)

func IntSliceToStr(sl []int) string {
	str_slice := []string{}

	for _, i := range sl {
		str := strconv.Itoa(i)
		str_slice = append(str_slice, str)
	}

	return strings.Join(str_slice, "")
}

func Simulate(str string, step int, step_cap int) string {
	step += 1
	answer_stack := []int{}
	curr := 0
	curr_count := 0

	for idx, r := range str {
		d, _ := strconv.Atoi(string(r))

		if idx == 0 || d == curr {
			curr = d
			curr_count += 1
		}

		if d != curr {
			answer_stack = append(answer_stack, curr_count, curr)
			curr_count = 1
			curr = d
		}

		if idx == len(str)-1 {
			answer_stack = append(answer_stack, curr_count, curr)
		}
	}

	if step == step_cap {
		return IntSliceToStr(answer_stack)
	}
	return Simulate(IntSliceToStr(answer_stack), step, step_cap)
}

func main() {
	results := Simulate("1113122113", 0, 50)
	fmt.Println(len(results))
}
