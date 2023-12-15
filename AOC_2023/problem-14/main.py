import sys

def transpose(grid) : 
    g = []
    for i in range(len(grid[0])) : 
        g.append("".join([x[i] for x in grid]))
    return g

def tilt(grid) : 
    g = transpose(grid)
    for idx, col in enumerate(g) : 
        sp = col.split("#")
        new_sp = []
        for i in sp : 
            c = i.count("O")
            a = c*"O" + "."*(len(i) - c)
            new_sp.append(a)
        g[idx] = "#".join(new_sp)
    g = transpose(g)
    return g

def cycle() : 
    pass

def calc_load(grid) : 
    s = 0
    for idx, l in enumerate(grid[::-1]) : 
        s += (idx + 1)*l.count("O")
    return s

f = sys.argv[1]
with open(f) as fp : 
    grid = fp.read().strip().split("\n")
    # print("=================")
    grid = tilt(grid)
    l = calc_load(grid)
    print(l)   
    