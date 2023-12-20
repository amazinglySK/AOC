import sys
from collections import defaultdict

f = sys.argv[1]

def get_neigh(c, m, prev_dir) : 
    dir_, n_dir = prev_dir
    valid = range(0, m)
    neigh = []
    for dr in [(1, 0), (-1, 0), (0, 1), (0, -1)] : 
        dx, dy = dr
        x, y = c
        xn, yn = x + dx, y + dy
        if dr == dir_ : n = n_dir + 1
        else : n = 1
        if xn not in valid or yn not in valid:
            continue
        neigh.append(((xn, yn), (dr, n)))
    return neigh

def backtrack(c, prev, m, grid) : 
    l = []
    while c : 
        l.append(c)
        if c not in prev : break
        c= prev[c]

    s = 0
    for j in range(m) : 
        for i in range(m) : 
            if (i, j) in l : 
                ch = grid[(i, j)]
                s += ch
                print(ch, end = "")
            else : print(".", end = "")
        print()

def dijkstra(grid, m) :
    open = [(0, 0)]
    closed = []
    cameFrom = {}

    gScore = defaultdict(lambda : 1e9)
    gScore[(0, 0)] = 0

    fScore = defaultdict(lambda : 1e9)
    fScore[(0, 0)] = 0

    prev_dirs = {}
    prev_dirs[(0, 0)] = ((0, 0), 0)

    def h(coord) : 
        x, y = coord
        return abs(m-1 - x) + abs(m-1 - y)

    while open != []  : 
        open.sort(key = lambda x : fScore[x])
        current = open[0]
        closed.append(current)

        if current == (m-1, m-1) : 
            backtrack(current, cameFrom, m, grid)
            return gScore[current]
        
        open.pop(0)
        direction = prev_dirs[current]

        for n, d in get_neigh(current, m, direction) : 
            if n in closed: continue
            temp = gScore[current] + grid[n]
            _, ndir_ = d
            if ndir_ >= 4 : ndir_ = 1e9
            temp_f = temp + ndir_ + h(n)
            if n in open : 
                if temp > gScore[n] : 
                    continue

            cameFrom[n] = current
            gScore[n] = temp
            fScore[n] = temp_f
            prev_dirs[n] = d
            if n not in open :
                open.append(n)
    return False

with open(f) as fp : 
    lines = fp.readlines()
    c = {}
    for j in range(len(lines)): 
        for i in range(len(lines[0].strip())) : 
            c[(i, j)] = int(lines[j][i])

    p = dijkstra(c, len(lines))
    print(p)
    