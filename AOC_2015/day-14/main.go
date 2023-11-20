package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Reindeer struct {
	name      string
	speed     int
	moving    int
	is_moving bool
	resting   int
	dist      int
	elapsed   int
	score     int
}

func ParseReindeers(input []string) []*Reindeer {
	reindeers := []*Reindeer{}

	for _, line := range input {
		split := strings.Split(line, " ")
		if len(split) <= 1 {
			continue
		}
		name, s, m, r := split[0], split[3], split[6], split[13]
		sInt, _ := strconv.Atoi(s)
		mInt, _ := strconv.Atoi(m)
		rInt, _ := strconv.Atoi(r)
		reindeers = append(reindeers, &Reindeer{name, sInt, mInt, true, rInt, 0, 0, 0})

	}

	return reindeers
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func GetWinningDistance(reindeers []*Reindeer, duration int) int {
	max := 0
	for _, reindeer := range reindeers {
		cumulus := (reindeer.moving + reindeer.resting)
		reindeer.dist += (duration / cumulus) * reindeer.speed * reindeer.moving
		if duration%cumulus > reindeer.moving {
			reindeer.dist += reindeer.moving * reindeer.speed
		}
		if reindeer.dist > max {
			max = reindeer.dist
		}
	}
	return max
}

func GetWinningPoints(reindeers []*Reindeer, duration int) int {
	max_score := 0
	for _, reindeer := range reindeers {
		reindeer.dist = 0
	}
	for sec := 0; sec < duration; sec++ {
		curr_high_dist := 0
		tied := []*Reindeer{}
		for _, reindeer := range reindeers {
			reindeer.elapsed += 1
			if reindeer.elapsed == reindeer.moving && reindeer.is_moving {
				reindeer.elapsed = 0
				reindeer.is_moving = false
				reindeer.dist += reindeer.speed
			}

			if reindeer.is_moving {
				reindeer.dist += reindeer.speed
			} else {
				if reindeer.elapsed == reindeer.resting {
					reindeer.is_moving = true
					reindeer.elapsed = 0
				}
			}
			if curr_high_dist < reindeer.dist {
				tied = []*Reindeer{reindeer}
				curr_high_dist = reindeer.dist
				continue
			}
			if curr_high_dist == reindeer.dist {
				tied = append(tied, reindeer)
			}
		}

		for _, r := range tied {
			r.score += 1
		}

	}

	for _, reindeer := range reindeers {
		fmt.Println(reindeer)
		if max_score < reindeer.score {
			max_score = reindeer.score
		}
	}
	return max_score
}

func main() {
	fmt.Println("Hello, World !")
	d, err := os.ReadFile("./input.txt")
	check(err)
	duration := 2503
	reindeers := ParseReindeers(strings.Split(string(d), ".\r\n"))
	fmt.Println(reindeers)
	max := GetWinningDistance(reindeers, duration)
	fmt.Println(max)
	max_points := GetWinningPoints(reindeers, duration)
	fmt.Println(max_points)

}
