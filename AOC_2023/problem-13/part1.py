def find_mirror(l) : 
    # Horizontal
    for i in range(len(l) - 1) : 
        if l[i] == l[i+1] : 
            l1 = i + 2
            l2 = 2*i + 1 - l1
            while 0 <= l2 and l1 < len(l): 
                if l[l1] != l[l2] : break
                l1 += 1
                l2 -= 1
            else : 
                return "row", i + 1

    # Vertical 
    for i in range(len(l[0]) - 1) : 
        col = [x[i] for x in l]
        col2 = [x[i+1] for x in l]
        if col == col2 : 
            c1 = i + 2
            c2 = i + i + 1 - c1
            while 0 <= c2 and c1 < len(l[0]): 
                col = [x[c1] for x in l]
                col2 = [x[c2] for x in l]
                if col != col2: break
                c1 += 1
                c2 -= 1
            else : 
                return "col", i + 1
            
def part1(patterns) : 
    s = 0
    for p in patterns : 
        lines = p.split('\n')
        t, n = find_mirror(lines)
        if t == "row" : s += n*100
        if t == "col" : s += n
    return s
    
