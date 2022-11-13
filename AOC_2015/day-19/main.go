package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"
	"unicode"
)

func Includes(a string, b []string) bool {
	for _, i := range b {
		if i == a {
			return true
		}
	}

	return false
}

func GenerateElementList(molecule string) []string {
	elements := []string{}
	stack := []rune{}
	for idx, i := range molecule {
		if unicode.IsUpper(i) && idx != 0{
			elements = append(elements, string(stack))
			stack = []rune{i}
			continue
		}
		stack = append(stack, i)
	}

	return elements
}

func CountElement(elements []string, el string) (count int) {
	count = 0
	for _, i := range elements {
		if i == el {
			count++
		}
	}
	return count
}

func CountSteps(molecule string) (steps int) {
	elements := GenerateElementList(molecule)
	Y := CountElement(elements, "Y")
	Rn := CountElement(elements, "Rn")
	Ar := CountElement(elements, "Ar")

	steps = len(elements) - (Rn + Ar) - 2*Y - 1

	return steps
}

func GenerateAllMolecules(conversion map[string][]string, molecule string) []string {
	answers := []string{}

	for k := range conversion {
		r := regexp.MustCompile(k)
		indice := r.FindAllStringIndex(molecule, -1)
		for _, i := range indice {
			for _, c := range conversion[k] {
				answer := strings.Join([]string{molecule[0:i[0]], c, molecule[i[1]:]}, "")
				answers = append(answers, answer)
			}
		}
	}

	return answers
}

func ParseInput(inp string) (map[string][]string, string) {
	main := strings.Split(inp, "\r\n\r\n")
	conv_map := map[string][]string{}
	conv, mol := main[0], main[1]
	conv_split := strings.Split(conv, "\r\n")
	for _, c := range conv_split {
		c_s := strings.Split(c, " => ")
		conv_map[c_s[0]] = append(conv_map[c_s[0]], c_s[1])
	}
	return conv_map, string(mol[0 : len(mol)-2])
}

func GetUniqueMolecules(mol []string) []string {
	u_mol := []string{}
	for _, i := range mol {
		if Includes(i, u_mol) {
			continue
		}
		u_mol = append(u_mol, i)
	}

	return u_mol
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	d, err := os.ReadFile("./input.txt")
	check(err)
	conv, mol := ParseInput(string(d))
	results := GenerateAllMolecules(conv, mol)
	fmt.Println("No. of distinct moelecules :", len(GetUniqueMolecules(results)))
	fmt.Println("No. of steps to reach the molecule :", CountSteps(mol))
}
