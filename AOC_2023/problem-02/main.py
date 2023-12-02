import re

f = input('File name : ')
with open(f) as inp_file : 
    lines = inp_file.readlines()
    valids = []
    sum_of_powers = 0
    for game in lines : 
        g = game[5:].strip().split(": ")
        g_id = int(g[0])
        # Part 1
        sets = re.split("; ", g[1])
        for i in sets :
            s = i.split(", ")
            for j in s : 
                p= j.split(" ")
                if p[1] == "red" and int(p[0]) > 12: break
                if p[1] == "green" and int(p[0]) > 13 : break
                if p[1] == "blue"  and int(p[0]) > 14: break
            else : 
                continue
            break
        else : 
            valids.append(g_id)

        # Part 2
        p = re.split(", |; ", g[1].strip())
        col = {"red" : [], "blue" : [], "green" : []}
        for i in p :
            sp = i.split(" ")
            col[sp[1]].append(int(sp[0]))
        
        power = 1
        for k in col : 
            power *= max(col[k])
        sum_of_powers += power
    
    print(sum(valids))
    print(sum_of_powers)
