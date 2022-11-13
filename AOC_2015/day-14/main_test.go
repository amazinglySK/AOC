package main 


import (
	"os"
	"testing"
	"strings"
)

func TestGetWinningPoints(t *testing.T) {
	d, _ := os.ReadFile("./test.txt")
	reindeers := ParseReindeers(strings.Split(string(d), ".\r\n"))
	points := GetWinningPoints(reindeers, 1000)

	if points != 689 {
		t.Errorf("expected %d, got %d", 689, points)
	}
}
