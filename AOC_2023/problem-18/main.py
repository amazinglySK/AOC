import sys

# Thanks to Reddit - r/adventofcode
# Shoelace formula : https://en.wikipedia.org/wiki/Shoelace_formula
# Pick's theorem : https://en.wikipedia.org/wiki/Pick%27s_theorem
'''
Pick's theorem:
    A = i + b/2 - 1
 => A - b/2 + 1 = i
 => A + b/2 + 1 = (i + b) --> Which is required
'''
def shoelace(points) : 
    a = 0
    for i in range(len(points) - 1) : 
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        a += x1*y2 - x2*y1
    return a//2

def solve(lines, part2=False) : 
    x = y = 0
    P = 0
    coords = []
    dv = "RDLU"
    for l in lines : 
        l = l.strip()
        if part2:
            l = l.strip()
            _, _, v= tuple(l.split())
            v = v.strip("#()")
            v, d = int(v[:5], 16), int(v[5])
            d = dv[d]
        else : 
            d, v, _ = tuple(l.split())
            v = int(v)
        if d == "R" : x += int(v)
        if d == "U" : y -= int(v)
        if d == "D" : y += int(v)
        if d == "L" : x -= int(v)
        P += int(v)
        coords.append((x, y))

    A = shoelace(coords)
    ans = A + P//2 + 1
    return ans

f = sys.argv[1]
with open(f) as fp : 
    lines = fp.readlines()
    print(solve(lines))
    print(solve(lines, True))