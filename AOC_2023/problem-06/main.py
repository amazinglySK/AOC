f = input('File name : ')
with open(f) as inp_file :
    # Part 1
    lines = inp_file.readlines()
    times = [int(x) for x in lines[0].lstrip("Time:").split()]
    distance = [int(x) for x in lines[1].lstrip("Distance:").split()]

    mul = 1
    for t, d in zip(times, distance): 
        c = 0
        for j in range(1, t+1) : 
            p = t - j
            if j*p > d : 
                c += 1
        mul *= c
    print(mul) 
    
    # Part 2
    time = int("".join([x for x in lines[0] if x.isdigit()]))
    dist = int("".join([x for x in lines[1] if x.isdigit()]))
    c = 0
    for i in range(1, time//2) : 
        if (time-i)*i > dist: 
            c += 1
    print(c*2 + 1) 
