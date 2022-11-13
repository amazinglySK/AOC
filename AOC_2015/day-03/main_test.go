package main

import "testing"

func TestSimulateTrip(t *testing.T) {
	tests := []string{">", "^>v<", "^v^v^v^v^v"}
	expected := []int{2, 4, 2}
	for idx, test := range tests {
		result := SimulateTrip(test)
		if result != expected[idx] {
			t.Errorf("expected %v got %v\n", expected[0], result)
		}
	}
}

func TestSimulateTripWithRobot(t *testing.T) {
	tests := []string{"^v", "^>v<", "^v^v^v^v^v"}
	expected := []int{3, 3, 11}
	for idx, test := range tests {
		result := SimulateTripWithRobot(test)
		if result != expected[idx] {
			t.Errorf("expected %v got %v\n", expected[0], result)
		}
	}
}
