# AOC 2023 

## Day 1

Part 1 : Simple parsing. Parsed all the numbers in the string to a list, and took the last and first element to get the answer

Part 2 : Used sliding windows of lengths 3, 4 and 5 to parse the number string in order. Just like part 1 added them too to the list, and finally got the first and last number. (There was a slight oversight while optimizing. I hadn't noticed the overlapping digits)

## Day 2

Part 1 : If any number of cubes for a set in a game is greater than max value, then don't consider the game; else consider it.

Part 2 : Straight forward checking for the maximum value in a game. That would be the minimum number of cubes of each colour required. 

## Day 3

(Man, this took some time 😅)

Part 1 : Collected all nodes (i.e. numbers and special characters along with all the coordinates they're in). For each of the number node, checked if any of the neighbouring node was a special character. If it was, then we consider it in our sum. 

Part 2 : Went through all the star nodes and for each star node, fetched it's neighbours and if it had exactly 2 neighbouring part numbers, then we multiply those numbers to gear_ratio.

## Day 4

Part 1 : Simple parsing, and a for loops through the winning tickets to see the number of winning tickets. Stored this in a list for the second part. 

Part 2 : Kind of a memoized DFS using recursion. Kept "scratching" card until a card with 0 points is encountered (which will return 1). Then the previous functions in the stack will return 1 + [scratch sum of all the next n cards]

## Day 5

Part 1 : Started off with simple parsing. Picked up the destination, source and the length of the range. For a given number if it is between source and source + length - 1 (inclusive), then we may map it to the destination. Mapping formula used: n - source + destination

Part 2 : A bit of set theory. Found the intersection between the seed ranges and the source map range. If there's no intersection, then there's simply no mapping done. In the case that there's an intersection, the intersection part is mapped and the non-intersection set (ONLY SEEDS) is then mapped to itself. Mapping formula here, was

```
diff = so - dest
intersection.lower - diff, intersection.upper - diff
```

Interval operations were done using [portion](https://pypi.org/project/portion/)

## Day 6

Part 1 : Simple for loop and checking each hold, distance combination.

Part 2 : Reduced the size of the problem by 1/2. Didn't need an overkill solution to solve it since the input size was small this time (Unlike day 5)

## Day 7 

That was a lot of sorting! *Phew*

Part 1 : Generated the strengths of each hand according to the given condition (from 7..1). Seggregated it based on the score, and then sorted each segment using bubble sort. 

Part 2 : Simply changed the order of precedence and a few edits in the strength calculation. The J-count was now added to the card with maximum number of occurences. The essential sorting algorithm remained the same. 
