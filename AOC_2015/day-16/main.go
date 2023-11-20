package main

import (
	"fmt"
	"strings"	
	"strconv"
	"os"
)

type Aunt struct {
	no int
	children int
	cats int
	goldfish int
	trees int
	samoyeds int
	pomeranians int
	akitas int
	vizslas int
	cars int
	perfumes int
	score int
	modScore int
}

func InitializeAunt(no int) Aunt {
	return Aunt{no, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0}
}

func (a *Aunt) ChangeProp(prop string, val int) {
	switch prop {
	case "children":
		a.children = val
	case "cats" :
		a.cats = val
	case "goldfish" :
		a.goldfish = val
	case "trees" :
		a.trees = val
	case "samoyeds" :
		a.samoyeds = val
	case "pomeranians" :
		a.pomeranians = val
	case "akitas" :
		a.akitas = val
	case "vizslas" :
		a.vizslas = val
	case "cars" :
		a.cars = val
	case "perfumes":
		a.perfumes = val
	}
}


func (a *Aunt) AssignModScore(comp *Aunt) {
	score := 0
	if a.samoyeds == comp.samoyeds {score+=1}
	if a.akitas == comp.akitas {score+=1}
	if a.vizslas == comp.vizslas {score+=1}
	if a.cars == comp.cars {score+=1}
	if a.perfumes == comp.perfumes {score+=1}
	if a.children == comp.children {score+=1}
	if a.cats < comp.cats {score+=1}
	if a.trees < comp.trees {score+=1}
	if a.pomeranians > comp.pomeranians && comp.pomeranians != -1 {score+=1}
	if a.goldfish > comp.goldfish && comp.goldfish != -1 {score+=1}
	
	comp.modScore = score 
}

func (a *Aunt) AssignScore(comp *Aunt) {
	score := 0
	if a.samoyeds == comp.samoyeds {score+=1}
	if a.akitas == comp.akitas {score+=1}
	if a.vizslas == comp.vizslas {score+=1}
	if a.cars == comp.cars {score+=1}
	if a.children == comp.children {score += 1}
	if a.perfumes == comp.perfumes {score+=1}
	if a.cats == comp.cats {score+=1}
	if a.trees == comp.trees {score+=1}
	if a.pomeranians == comp.pomeranians {score+=1}
	if a.goldfish == comp.goldfish {score+=1}
	
	comp.score = score 
}

func ParseAunts(data string) []*Aunt {
	aunts := []*Aunt{}
	lines := strings.Split(data, "\r\n")
	for _, line := range lines {
		split := strings.Split(line, " ")
		if len(split) <= 1 {
			continue
		}
		info := strings.Join(split[2:], "")
		info_arr := strings.Split(info, ",")
		sue_sno, _ := strconv.Atoi(strings.TrimSuffix(split[1], ":"))
		sue := InitializeAunt(sue_sno)
		for _, i := range info_arr {
			i_split := strings.Split(i, ":")
			if len(i_split) <= 1 {
				continue
			}
			lhs, rhs := i_split[0], i_split[1]
			rhs_int, _ := strconv.Atoi(rhs)
			sue.ChangeProp(lhs, rhs_int)
		}
		aunts = append(aunts, &sue)
	}
	return aunts
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main(){
	d, err := os.ReadFile("./input.txt")
	check(err)
	aunts := ParseAunts(string(d))
	correct_sue := Aunt{no : -1, children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1, score:0, modScore:0}
	max := &correct_sue
	maxMod := &correct_sue
	for _, aunt := range aunts {
		correct_sue.AssignScore(aunt)
		if aunt.score > max.score {
			max = aunt
		}
		correct_sue.AssignModScore(aunt)
		if aunt.modScore > maxMod.modScore {
			maxMod = aunt
		}
	}
	fmt.Println(max.no, maxMod.no)
}
