def calc_diff(l1, l2) : 
    t = 0
    for i, j in zip(l1, l2) : 
        if i != j : t += 1
    return t

def find_mirror_with_smudge(l) : 
    # Horizontal 
    for i in range(len(l) - 1) : 
        diff = calc_diff(l[i], l[i+1])
        smudge_done = False
        if diff == 1 : smudge_done = True
        if diff <= 1: 
            l1 = i + 2
            l2 = i + i + 1 - l1
            while 0 <= l2 and l1 < len(l): 
                diff = calc_diff(l[l1], l[l2])
                if diff > 1 or (diff == 1 and smudge_done): break
                elif diff == 1 : smudge_done = True
                l1 += 1
                l2 -= 1
            else : 
                if not smudge_done : continue
                return "row", i + 1
            
    # Vertical 
    for i in range(len(l[0]) - 1) : 
        col = [x[i] for x in l]
        col2 = [x[i+1] for x in l]
        diff = calc_diff(col, col2)
        smudge_done = False
        if diff == 1 : smudge_done = True
        if diff <= 1: 
            c1 = i + 2
            c2 = i + i + 1 - c1
            while 0 <= c2 and c1 < len(l[0]): 
                col = [x[c1] for x in l]
                col2 = [x[c2] for x in l]
                diff = calc_diff(col, col2)
                if diff > 1 or (diff == 1 and smudge_done): break
                elif diff == 1: smudge_done = True
                c1 += 1
                c2 -= 1
            else : 
                if not smudge_done : continue
                return "col", i + 1

def part2(patterns) : 

    s2 = 0
    for p in patterns : 
        lines = p.split('\n')
        t, n = find_mirror_with_smudge(lines)
        if t== "row" : s2 += n*100
        if t== "col" : s2 += n

    return s2