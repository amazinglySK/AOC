import sys
from part1 import part1
from part2 import part2


f = sys.argv[1]
with open(f) as fp : 
    patterns = fp.read().strip().split("\n\n")
    s = part1(patterns)
    s2 = part2(patterns)        
    print(s)
    print(s2)