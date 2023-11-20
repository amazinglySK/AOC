package main 

import (
	"fmt"
	"strings"
	"strconv"
	"os"
	"regexp"
	"sort"
)

type Ingredient struct {
	name 	string
	cap 	int
	dur 	int
	flav 	int
	text 	int
	cal 	int
}

type Score struct {
	cap 	int
	dur 	int
	flav 	int
	text 	int
	cal 	int
}


func AddScores(a, b *Score) *Score {
	return &Score{a.cap + b.cap, a.dur + b.dur, a.flav + b.flav, a.text + b.text, a.cal + b.cal}
}

func GetAllScores(ingredients []*Ingredient, idx int, lim int, cal_lim int) []*Score{
	ingredient := ingredients[idx]
	scores := []*Score{}
	if idx == len(ingredients) - 1 {
		return []*Score{&Score{lim*ingredient.cap, lim*ingredient.dur, lim*ingredient.flav, lim*ingredient.text, lim*ingredient.cal}}
	}

	for i := 0; i <= lim; i++ {
		curr := &Score{i*ingredient.cap, i*ingredient.dur, i*ingredient.flav, i*ingredient.text, i*ingredient.cal}
		for _, score := range GetAllScores(ingredients, idx + 1, lim-i, cal_lim) {
			new := AddScores(curr, score)
			if idx == 0 && cal_lim != 0 {
				if new.cal != cal_lim {continue}
			}	
			scores = append(scores, new)
		}
	}
	return scores
}

func CalcTotal(score *Score) int {
	if score.cap <= 0 || score.text <= 0 || score.dur <= 0 || score.flav <= 0 {
		return 0
	}

	return score.cap*score.text*score.flav*score.dur
}

func GetBestScore(scores []*Score) int {
	totals := []int{}
	for _, score := range scores {
		total := CalcTotal(score)
		totals = append(totals, total)
	}
	sort.Ints(totals)
	return totals[len(totals)-1]
}

func ParseIngredients(data string) []*Ingredient {
	ingredients := []*Ingredient{}
	lines := strings.Split(data, "\r\n")
	for _, line := range lines {
		split := strings.Fields(line)
		r := regexp.MustCompile("-?[0-9]+")
		params := r.FindAllString(line, -1)
		if len(split) <= 1 {
			continue
		}
		name, cap, dur, flav, text, cal := strings.TrimSuffix(split[0], ":"), params[0], params[1], params[2], params[3], params[4] 
		capInt, _ := strconv.Atoi(cap)
		durInt, _ := strconv.Atoi(dur)
		flavInt, _ := strconv.Atoi(flav)
		textInt, _ := strconv.Atoi(text)
		calInt, _ := strconv.Atoi(cal)
		ingredient := Ingredient{name, capInt, durInt, flavInt, textInt, calInt}
		ingredients = append(ingredients, &ingredient)

	}
	return ingredients
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	d, err := os.ReadFile("./input.txt")
	check(err)
	ingredients := ParseIngredients(string(d))
	scores := GetAllScores(ingredients, 0, 100, 0)
	withCal := GetAllScores(ingredients, 0, 100, 500)
	best := GetBestScore(scores)
	fmt.Println(best)
	bestWithCal := GetBestScore(withCal)
	fmt.Println(bestWithCal)
}
