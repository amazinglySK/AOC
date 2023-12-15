import sys

def transpose(grid) : 
    g = []
    for i in range(len(grid[0])) : 
        g.append("".join([x[i] for x in grid]))
    return g

def tilt(grid, d = "v", vec = 1) : 
    g = transpose(grid) if d == "v" else grid.copy()
    for idx, col in enumerate(g) : 
        sp = col.split("#")
        new_sp = []
        for i in sp : 
            c = i.count("O")
            a = c*"O" + "."*(len(i) - c) if vec == 1 else "."*(len(i) - c) + c*"O"
            new_sp.append(a)
        g[idx] = "#".join(new_sp)
    g = transpose(g) if d == "v" else g
    return g

def cycle(grid) : 
    grid = tilt(grid)
    grid = tilt(grid, d = "h")
    grid = tilt(grid, vec = -1)
    grid = tilt(grid, d= "h", vec = -1)
    return grid

def calc_load(grid) : 
    s = 0
    if type(grid) == str : grid = grid.split("\n")
    for idx, l in enumerate(grid[::-1]) : 
        s += (idx + 1)*l.count("O")
    return s

f = sys.argv[1]
with open(f) as fp :
    # Part 1 
    grid = fp.read().strip().split("\n")
    grid = tilt(grid)
    l = calc_load(grid)
    print(l)   

    # Part 2
    fp.seek(0)
    grid = fp.read().strip().split("\n")
    grid_hist =  []
    n = 1000000000
    last = 0
    for i in range(n) : 
        grid = cycle(grid)
        g = "\n".join(grid)
        if g in grid_hist : 
            last_idx = grid_hist.index(g)
            break
        grid_hist.append(g)
    idx = last_idx + (n-1-i) % (i - last_idx)
    print(calc_load(grid_hist[idx]))
    