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
