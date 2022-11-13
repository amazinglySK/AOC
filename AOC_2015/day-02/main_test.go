package main

import "testing"

func TestCalcAreaAndRibbon(t *testing.T) {
	tests := []string{"2x3x4", "1x1x10"}
	results_a := []int{58, 43}
	results_p := []int{34, 14}
	for idx, test := range tests {
		a, p := CalcAreaAndRibbon(test)
		s_a, s_p := results_a[idx], results_p[idx]
		if a != s_a || p != s_p {
			t.Errorf("expected %v and %v but got %v and %v\n", s_a, s_p, a, p)
		}
	}
}
