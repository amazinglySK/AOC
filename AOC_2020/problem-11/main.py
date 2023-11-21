

f = input("File name : ")
with open(f) as inp_file : 
    lines = inp_file.readlines()
    seats = [[x for x in l.strip()] for l in lines]
    prev = []
    while prev != seats :
        new = [[x for x in y] for y in seats] 
        for j in range(len(seats)) : 
            for i in range(len(seats[0])) : 
                curr = seats[j][i]
                if curr == "." : continue
                x_c = [i, i+1, i-1]
                y_c = [j, j+1, j-1]
                
                x_c = [x for x in x_c if 0 <= x < len(seats[0])]
                y_c = [y for y in y_c if 0 <= y < len(seats)]

                lit = 0
                for x in x_c : 
                    for y in y_c : 
                        if x == i and y == j : continue
                        if seats[y][x] == "#" : 
                            lit += 1

                if lit == 0 and curr == "L" : 
                    new[j][i] = "#"
                
                elif lit >= 4 and curr == "#" : 
                    new[j][i] = "L"
        prev = [[x for x in y] for y in seats]
        seats = new
#        print("\n".join(["".join(x) for x in seats]))


    c = 0
    for j in range(len(seats)) : 
        for i in range(len(seats[0])) : 
            if seats[j][i] == "#" : c += 1
    
    print(c)

    seats = [[x for x in l.strip()] for l in lines]
    while prev != seats : 
        new = [[x for x in y] for y in seats] 
        for j in range(len(seats)) : 
            for i in range(len(seats[0])) : 
                curr = seats[j][i]
                vecs = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (1,0), (0, -1), (0, 1)]
                lit = 0
                for vec in vecs: 
                   dx, dy = vec
                   x, y = i + dx, j + dy
                   while 0 <= x < len(seats[0]) and 0 <= y < len(seats) : 
                        i_curr = seats[y][x]
                        if i_curr == "#" : 
                            lit += 1
                        
                        if i_curr != "." : break
                        x += dx
                        y += dy

                if lit == 0 and curr == "L" : 
                    new[j][i] = "#"
                
                elif lit >= 5 and curr == "#" : 
                    new[j][i] = "L"
        prev = [[x for x in y] for y in seats]
        seats = new


   # print("\n".join(["".join(x) for x in seats]))
    c = 0
    for j in range(len(seats)) : 
        for i in range(len(seats[0])) : 
            if seats[j][i] == "#" : c += 1
    print(c)
