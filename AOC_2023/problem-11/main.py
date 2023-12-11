import sys

def find_empty_rcs(grid) :
    # Find the empty rows and columns 
    # Horizontal 
    rows = [idx for idx in range(len(grid)) if set(grid[idx]) == {"."}]
    # Vertical 
    cols = [idx for idx in range(len(grid)) if set([x[idx] for x in grid]) == {"."}]
    return rows, cols

def expand_grid(grid, galaxies, inflation = 2) : 
    rows, cols = find_empty_rcs(grid)
    for idx, coord in enumerate(galaxies) : 
        x, y = coord
        x1, y1 = x, y
        for r in rows : 
            if y > r : y1 += inflation - 1
        for c in cols : 
            if x > c : x1 += inflation - 1
        galaxies[idx] = (x1, y1)
    
    return galaxies

def find_galaxies(grid) : 
    # Readability? What's that?
    coords = [(i, j) for i in range(len(grid[0])) for j in range(len(grid)) if grid[j][i] == "#"]
    return coords

def calc_distance(a, b) : 
    x1, y1 = a
    x2, y2 = b
    return abs(x2-x1) + abs(y2-y1)

def solve(part) : 
    if part == 1 : inflation = 2
    else : inflation = 1000000
    galaxies = find_galaxies(grid)

    coords = expand_grid(grid, galaxies, inflation)
    combos = []
    for i in range(len(coords) - 1) : 
        c = [(coords[i], x) for x in coords[i+1:]]
        combos.extend(c)

    d = 0
    for a, b in combos : 
        dist = calc_distance(a, b)
        d += dist

    return d

with open(sys.argv[1]) as fp : 
    grid = [[ch for ch in l] for l in fp.read().strip().split("\n")]
    print(solve(1))
    print(solve(2))
