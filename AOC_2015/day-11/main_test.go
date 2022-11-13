package main

import "testing"

func TestCountNonOverlaps(t *testing.T) {
	input := []string{"aa", "ab", "bb", "bb"}
	result := CountNonOverlaps(input)
	if result != 2{
		t.Errorf("expected %d, got %d", 2, result)
		return
	}
	input = []string{"aa", "aa", "aa", "aa"}
	result = CountNonOverlaps(input)
	if result != 2 {
		t.Errorf("expected %d, got %d", 2, result)
		return
	}
}

func TestCreateSubstrPairs(t *testing.T) {
	str := "abcc"
	expected := []string{"ab", "bc", "cc"}
	result := CreateSubstrPairs(str)

	for idx, s := range result {
		if expected[idx] != s {
			t.Errorf("expected %v, got %v", expected, result)
			return
		}
	}
}


func TestCheckValidity(t *testing.T) {
	test_pwd := "ghijklmn"
	result := CheckValidity(test_pwd)
	if result == true {
		t.Errorf("expected %v, got %v", false, result)
		return
	}
	test_pwd = "ghjaabcc"
	result = CheckValidity(test_pwd)
	if result == false {
		t.Errorf("expected %v, got %v", true, result)
		return
	}

}
