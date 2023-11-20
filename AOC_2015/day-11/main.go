package main

import "fmt"

func reverse(str string) string{
    r := []rune(str)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}


func CreateSubstrPairs(str string) []string {
	substrs := []string{}
	var prev rune
	for i, r := range str {
		if i == 0 {
			prev = r
			continue
		}
		
		substrs = append(substrs, fmt.Sprintf("%c%c", prev, r))
		prev = r

	}

	return substrs
}

func CountNonOverlaps(strings []string) int {
	count := 0 
	prev_idx := 0
	for idx, str := range strings {
		rune_str := []rune(str)
		if rune_str[0] == rune_str[1] {
			if prev_idx != idx || idx == 0{
				count += 1
				prev_idx = idx + 1
			}
		}
	}

	return count
}

func Increment(str string) string {
	carry_over := false
	result := []rune{}
	for i, r := range reverse(str) {
		if i == 0 || carry_over == true{
			r += 1
			carry_over = false
		}
		if r > 122 {
			r = 97
			carry_over = true
		}
		result = append(result, r)
	}
	return reverse(string(result))
}

func CheckValidity(pwd string) bool {
	chain := 0
	consec_count := CountNonOverlaps(CreateSubstrPairs(pwd))
	str := []rune(pwd)
	for i, r := range str {
		if r == 'i' ||r == 'o' || r == 'l' {
			return false
		}

		if i > 1 {
			if str[i - 2] == str[i-1] - 1 && str[i-2] == r - 2 {
				chain += 1
			}
		}
		
	}
	return chain >= 1 && consec_count >= 2
}

func UpdatePassword(pwd string) string {
	plain_out := false
	pwd_rune := []rune{}
	for _, r := range pwd {
		if r == 'i' || r== 'o' || r == 'l' {
			plain_out = true
			pwd_rune = append(pwd_rune, r + 1)
			continue
		}
		if plain_out {
			pwd_rune = append(pwd_rune, 'a')
		}
		
		pwd_rune = append(pwd_rune, r)

	}
	return string(pwd_rune)
}

func FindNextValidPassword(str string, c int) string {
	next := Increment(str)
	if !CheckValidity(next) {
		return FindNextValidPassword(next, c + 1)
	}
	return next
}


func main() {
	fmt.Println(FindNextValidPassword("hxbxxyzz", 0))
	fmt.Println("Hello, World")
}
