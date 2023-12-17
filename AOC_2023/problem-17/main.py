
import sys

f = sys.argv[1] 

def find_min(starting, ending, grid, max) : 
    vecs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    open = [grid[starting]]
    closed = []
    grid[starting]["g"]  = 0
    grid[starting]["f"]  = 0
    grid[starting]["h"]  = 0
        
    while open != []: 

        curr_node = [x for x in open if x["f"] == min([y["f"] for y in open])]
        if curr_node[0]["coord"] == ending : 
            print("Found")

        children = []





with open(f) as fp :
    lines = fp.read().strip().split("\n")
    map = {}
    for j, l in enumerate(lines) : 
        for i, ch in enumerate(l) : 
            map[(i, j)] = {"coord" : (i, j), "v" : int(ch), "g" : None, "f" : None, "h" : None}
    
    ans = find_min((0, 0), (len(lines) - 1, len(lines) - 1), map, len(lines))
    print(ans)

