package main

import (
	"fmt"
	"os"
	"strings"
)

type Text struct {
	str string
}

func includes(arr []interface{}, elem interface{}) bool {
	for _, i := range arr {
		if i == elem {
			return true
		}
	}
	return false
}
func count(arr []interface{}, elem interface{}, elem_idx int) int {
	count := 0
	for idx, i := range arr {
		if i == elem && elem_idx != idx-1 && elem_idx != idx+1 {
			count += 1
		}
	}
	return count
}

func (txt *Text) CheckVowels() bool {
	count := 0
	vowels := []interface{}{'a', 'e', 'i', 'o', 'u'}
	for _, t := range txt.str {
		if includes(vowels, t) {
			count += 1
		}
		if count == 3 {
			return true
		}
	}
	return false
}
func (txt *Text) CheckDouble() bool {
	var prev rune
	for idx, t := range txt.str {
		if idx == 0 {
			prev = t
			continue
		}
		if prev == t {
			return true
		}
		prev = t
	}
	return false
}
func (txt *Text) CheckNotBadSub() bool {
	not_allowed := []interface{}{"ab", "cd", "pq", "xy"}
	var prev rune
	for idx, t := range txt.str {
		if idx == 0 {
			prev = t
			continue
		}
		if includes(not_allowed, fmt.Sprintf("%c%c", prev, t)) {
			return false
		}
		prev = t
	}
	return true

}

type NewText struct {
	str string
}

func (txt *NewText) create_substr_pairs() []interface{} {
	text := txt.str
	var prev rune
	var substr_pairs []interface{}
	for idx, i := range text {
		if idx == 0 {
			prev = i
			continue
		}
		substr_pairs = append(substr_pairs, fmt.Sprintf("%c%c", prev, i))
		prev = i
	}
	return substr_pairs
}

func (txt *NewText) CheckDoublePair() bool {
	var pairs []interface{} = txt.create_substr_pairs()
	for idx, pair := range pairs {
		if count(pairs, pair, idx) >= 2 {
			return true
		}
	}
	return false
}

func (txt *NewText) OneLetterBetween() bool {
	for idx := range txt.str {
		if idx == 0 || idx == len(txt.str)-1 {
			continue
		}

		if txt.str[idx-1] == txt.str[idx+1] {
			return true
		}
	}
	return false
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	data, e := os.ReadFile("./input.txt")
	check(e)
	lines := strings.Split(string(data), "\r\n")
	count := 0
	sc_count := 0
	for _, line := range lines {
		text := Text{line}
		new_text := NewText{line}
		answer := [3]bool{text.CheckVowels(), text.CheckDouble(), text.CheckNotBadSub()}
		new_answer := [2]bool{new_text.CheckDoublePair(), new_text.OneLetterBetween()}
		if answer == [3]bool{true, true, true} {
			count += 1
		}
		if new_answer == [2]bool{true, true} {
			sc_count += 1
		}
	}

	fmt.Printf("Number of nice strings : %v\n", count)
	fmt.Printf("Number of nice strings (using the second algorithm) : %v\n", sc_count)
}
