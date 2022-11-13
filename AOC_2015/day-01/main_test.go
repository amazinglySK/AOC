package main

import "testing"

func TestCalcFloor(t *testing.T) {
	tests := []string{"(())", "(((", "))(((((", "())", ")))"}
	floors := []int{0, 3, 3, -1, -3}

	for i, test := range tests {
		floor, _ := CalcFloor(test)
		if floors[i] != floor {
			t.Errorf("Expected %v got %v", floors[i], floor)
		}
	}

	tests = []string{")", "()())"}
	negs := []int{1, 5}
	for i, test := range tests {
		_, floor := CalcFloor(test)
		if negs[i] != floor {
			t.Errorf("Expected %v got %v", negs[i], floor)
		}
	}

}
