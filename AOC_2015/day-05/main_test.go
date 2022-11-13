package main

import "testing"

func TestText(t *testing.T) {
	texts := []Text{Text{"ugknbfddgicrmopn"}, Text{"aaa"}, Text{"jchzalrnumimnmhp"}, Text{"haegwjzuvuyypxyu"}, Text{"dvszwmarrgswjxmb"}}
	results := [][3]bool{{true, true, true}, {true, true, true}, {true, false, true}, {true, true, false}, {false, true, true}}
	for i, text := range texts {
		result := [3]bool{text.CheckVowels(), text.CheckDouble(), text.CheckNotBadSub()}
		expected := results[i]
		if result != expected {
			t.Errorf("expected %v got %v", expected, result)
			return
		}
	}
}

func TestNewText(t *testing.T) {
	texts := []NewText{NewText{"qjhvhtzxzqqjkmpb"}, NewText{"xxyxx"}, NewText{"uurcxstgmygtbstg"}, NewText{"ieodomkazucvgmuy"}}
	results := [][2]bool{{true, true}, {true, true}, {true, false}, {false, true}}
	for i, text := range texts {
		result := [2]bool{text.CheckDoublePair(), text.OneLetterBetween()}
		expected := results[i]
		if result != expected {
			t.Errorf("expected %v got %v", expected, result)
			return
		}
	}
}
