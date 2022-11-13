package main 

import (
	"fmt"
	"os"
	"unicode"
	"strconv"
	"strings"
	"encoding/json"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func rec(f interface{}) (output float64) {
	outer:
	switch fv := f.(type) {
		case []interface{}:
			for _, val := range fv {
				output += rec(val)
			}
		case float64:
			output += fv
		case map[string]interface{}:
			for _, val := range fv {
				if val == "red" {
					break outer
				}
			}
			for _, val := range fv {
				output += rec(val)
			}
	}

	return output
}

func IgnoreRedInts(jsonString string) float64 {
	var f interface{}
	var output float64
	json.Unmarshal([]byte(jsonString), &f)
	output = rec(f)

	return output
}

func AddAllInts(json string) int {
	sum := 0
	number_start := false
	number := []string{}
	for _, r := range json {

		if r == '-' || unicode.IsNumber(r){
			number = append(number, string(r))
			number_start = true
			continue
		}
		if number_start == true && !unicode.IsNumber(r){
			number_start = false
			str_num, err := strconv.Atoi(strings.Join(number, ""))
			check(err)
			sum += str_num
			number = []string{}
		}
	}
	return sum
}

func CorrectedSum(json string) int {
	return 0
}

func main() {
	d, err := os.ReadFile("./input.json")
	check(err)
	result := AddAllInts(string(d))
	fmt.Println(result)
	sec_result := IgnoreRedInts(string(d))
	fmt.Println(sec_result)
	fmt.Println("Hello, World")
}
