import sys

rules = {
    "/" : lambda dx, dy : [(-dy, -dx)],
    "\\" : lambda dx, dy : [(dy, dx)],
    "|" : lambda dx, dy : [(dx, dy)] if (dx, dy) in [(0, 1), (0, -1)] else [(dy, dx), (-dy, -dx)],
    "-" : lambda dx, dy : [(dx, dy)] if (dx, dy) in [(1, 0), (-1, 0)] else [(dy, dx), (-dy, -dx)]
}

seen = set()
visited = set()
def light(start, vec, g, l, first = False) : 
    if (start, vec) in seen : return
    seen.add((start, vec))

    dx, dy = vec
    x, y = start
    visited.add((x, y))

    if first : 
        if (x, y) in g : 
            ch = g[(x, y)]
            for i in rules[ch](dx, dy) : 
                light((x, y), i, g, l)
            return

    while True : 
        x += dx
        y += dy
        if not (x in range(0, l) and y in range(0, l)) : return
        visited.add((x, y))
        if (x, y) in g : break

    ch = g[(x, y)]
    for i in rules[ch](dx, dy) : light((x, y), i, g, l)
        
def parse_grid(lines) : 
    g = {}
    for j in range(len(lines)) : 
        for i in range(len(lines[j])) : 
            ch = lines[j][i]
            if ch == "." : continue
            else : g[(i, j)] = ch
    return g

f = sys.argv[1] 
with open(f) as fp : 
    lines = fp.read().strip().split("\n")
    grid = parse_grid(lines)
    light((0, 0), (1, 0), grid, len(lines), first = True)
    print(len(visited))
    visited.clear()
    seen.clear()


    # Part 2
    max = 0
    for (dx, dy) in [(1, 0), (0, 1)] :  # Left and top sides
        for j in range(len(lines)) : 
            coord = dy*j, dx*j
            light(coord, (dx, dy), grid, len(lines), first = True)
            if len(visited) > max : max = len(visited)
            visited.clear()
            seen.clear()

    for (dx, dy) in [(-1, 0), (0, -1)] : # Right and bottom sides
        for j in range(len(lines)) :
            coord = (len(lines)-1, j) if dx == -1 else (j, len(lines) - 1)
            light(coord, (dx, dy), grid, len(lines), first = True)
            if len(visited) > max : max = len(visited)
            visited.clear()
            seen.clear()

    print(max)
