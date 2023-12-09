def simulate(s) : 
    p = [[int(x) for x in s.split()]]
    while not all(x == 0 for x in p[-1]): 
        tmp = []
        for i in range(len(p[-1]) - 1) :
            tmp.append(p[-1][i+1] - p[-1][i])
        p.append(tmp)

    # Extrapolation
    n = b = 0
    for i in range(-1, -len(p)-1, -1) :
        n += p[i][-1]
        b = p[i][0] - b

    return n, b


f = input("File : ")
with open(f) as fp : 
    lines = fp.read().split("\n")
    s = s2 = 0
    for l in lines : 
        n, b = simulate(l)
        s += n
        s2 += b
    print(s)
    print(s2)