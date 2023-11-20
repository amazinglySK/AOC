package main

import (
	"fmt"
	"os"
	"strings"
)

func GetEncryptedCount(str []string) int {
	count := 0
	for _, s := range str {
		for _, r := range s {
			switch r {
			case '\\':
				count += 2
			case '\x22':
				count += 2
			default:
				count += 1
			}
			// fmt.Printf("%c %d\n", r, count)
		}
		count += 2
	}
	return count
}

func GetCharCount(str []string) int {
	count := 0
	for _, s := range str {
		skip_count := 0
		for _, r := range s {
			switch r {
			case '\\':
				if skip_count == 1 {
					skip_count -= 1
				} else {
					count += 1
					skip_count = 1
				}

			case 'x':
				if skip_count == 1 {
					skip_count = 2
				} else {
					count += 1
				}
			default:
				if skip_count == 0 {
					count += 1
				} else {
					skip_count -= 1
				}
			}
			// fmt.Printf("%c %d %d\n", r, skip_count, count)
		}
		count -= 2
		// fmt.Println(count)
	}
	return count
}
func GetCodeCount(str []string) int {
	count := 0
	for _, s := range str {
		// fmt.Println(s)
		count += len(s)
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
	str := strings.Split(string(d), "\r\n")
	chars := GetCharCount(str)
	code := GetCodeCount(str)
	encoded := GetEncryptedCount(str)
	fmt.Println(code - chars)
	fmt.Println(encoded - code)
}
