package main

import "testing"

func TestGetMinDec(t *testing.T) {
	tests := []string{"abcdef", "pqrstuv"}
	results := []int{609043, 1048970}

	for idx, test := range tests {
		result := GetMinDec(test, "00000")
		expected := results[idx]
		if result != expected {
			t.Errorf("expected %v got %v", expected, result)
		}
	}

}
