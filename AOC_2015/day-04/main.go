package main

import (
	"crypto/md5"
	"fmt"
	"strings"
)

func GetMinDec(key string, string_to_check string) int {
	answer := 0
	for i := 10000; i < 10000000; i++ {
		data := []byte(fmt.Sprintf("%v%v", key, i))
		string_hash := fmt.Sprintf("%x", md5.Sum(data))
		if strings.HasPrefix(string_hash, string_to_check) {
			answer = i
			break
		}
	}
	return answer
}

func main() {
	fmt.Printf("Your answer is : %v\n", GetMinDec("ckczppom", "00000"))
	fmt.Printf("Your second answer is : %v\n", GetMinDec("ckczppom", "000000"))
}
