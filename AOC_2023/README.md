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

That was a lot of sorting! _Phew_

Part 1 : Generated the strengths of each hand according to the given condition (from 7..1). Seggregated it based on the score, and then sorted each segment using bubble sort.

Part 2 : Simply changed the order of precedence and a few edits in the strength calculation. The J-count was now added to the card with maximum number of occurences. The essential sorting algorithm remained the same.

## Day 8

Part 1: Loop until you hit the target. Simple parsing and executing

Part 2: Required a bit of reddit's contribution. The said pattern repeated after a point, so lcm of the number of steps for each of those starting points gives the final value for at which they all turn "Z". To be frank, this shouldn't be a general solution and this repeating behaviour is something peculiar to the input data only. There are probably many other inputs where this solution broke.

## Day 9

Part 1: Pretty straightforward problem. I think it was my fastest AOC solve. Simply iterated through the initial row and finally just extrapolated as instructed.

Part 2: Reapplying the same concept to the left side. Had to just tweak a few arithmetic operators and that's it!

## Day 10

Part 1: Pretty hacky solution. Basically followed the pipe from the starting point until it reached back to it. Had to check a few edge cases and direct the loop according to the type of pipe. After finding the length of the pipes, divide it by 2 and that's your farthest from the start. Find the maximum for all outbound pipes and you've got your solution. 

Part 2: Seems like a floodfill algorithm. But the weird edge case of water being able to flow between the pipes is a roadblock. DNF

## Day 11

Part 1: Started with simple list manipulation and duplication; duplicating every row after a match.

Part 2: Modified the algorithm to do some math instead of intense memory calculation. Basic check conditions. Nothing fancy on this day. 

The distance they were looking for was the [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry). That was probably the only noticeable gotcha on this day. 

## Day 12

Part 1: Nothing to explain by myself - [this reddit comment](https://www.reddit.com/r/adventofcode/comments/18hauj1/comment/kd93yog/?utm_source=share&utm_medium=web2x&context=3) saves the day.

Part 2: DNF. Huge scaling issue. 

## Day 13

Part 1: The mirror was between the first consecutive pair of rows which have the same sequence of character. Two pointers, one from the start and the end traverses through the 2D Array.

Part 2: The smudge could be between two mirrors who has exactly one difference in their sequence. Nothing else changed. 

...

## Day 14

(Noting this solution before any else because of the peculiarity)

Part 1: Took the column wise strings and split them by "#". Now for the tilt, just bring the rocks to one end and the dots to the other side

```
c = chunk.count("O")
"O"*c + "."*(length of chunk - c)
```

Part 2 : Used a modified version of the tilt function. Depending on the direction transposed/didn't transpose and changed/didn't change the order of chunk after tilt as mentioned above.

Upon close study of the input data, it was seen that the pattern was recurring after a point. From then on with a bit of modulus and tweaking with the variables we arrive at the solution I found out.

_(Pretty proud of my solution for this day)_

## Day 15

This was probably a redemption day. For the medley of hard problems this cooled down the situation a bit. Direct parsing and processing.

## Day 16

Kind of a day 10 problem. Had to save the direction vectors once again for each of the mirror types. Then it was just processing the path of light through the maze.

Part 2 was just applying the same algorithm through each row and column.

## Day 18

Direct application of [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) and [Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula). Had to look it up on reddit, but hey it was something new that I learned. 

The task was to find the sum of interior and exterior blocks of the closed polygon.

```
Pick's theorem
    A = i + b/2 - 1

With the shoelace formula : 
    A = sum(x_i*y_(i+1) - x_(i+1)*yi)

Since we need i + b
    
    A + 1 = i + b/2
So, i + b = A + b/2 + 1

A -> Calculated using the Shoelace formula
b -> Calculated while looping through the input coordinates
```
