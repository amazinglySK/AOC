
import sys

f = sys.argv[1]

def neighbours(c, occ, mx) : 
    valid = range(0, mx)
    neigh = set()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
        x, y = c
        nx, ny = x + dx, y + dy
        if nx not in valid or ny not in valid : continue
        if (nx, ny) in occ : continue
        neigh.add((nx, ny))
    return neigh

def simulate(s, occupied, n, mx) : 
    t = {s}
    while n != 0 : 
        tmp = set()
        for i in t :
            tmp = tmp.union(neighbours(i, occupied, mx))
        t = tmp
        n -= 1
    return len(t)

with open(f) as fp : 
    lines = fp.readlines()
    occupied = set()
    start = tuple()
    for j in range(len(lines)) : 
        for i in range(len(lines[0].strip())) : 
            ch = lines[j][i]
            c = (i, j)
            if ch == "#" : occupied.add(c)
            if ch == "S" : start = c

    s = simulate(start, occupied, 64, len(lines))
    print(s)

