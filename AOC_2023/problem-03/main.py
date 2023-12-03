def create_nodes(lines) :  
    nodes = []
    lines = [l.strip() for l in lines]
    for i in range(len(lines)) : 
        num, coords = "", []
        for j in range(len(lines[i])) : 
            ch = lines[i][j]
            if ch.isdigit() : 
                num += ch
                coords.append((j, i))
                continue
            if not ch.isdigit() and num: 
                nodes.append((num, coords))
                num, coords = "", []
            if ch == "." : continue
            else : nodes.append((ch, (j,i)))
            
        if num : nodes.append((num, coords))

    return nodes

def create_combos(x, y, s) :  # Creates all the neighbours
    return [(i, j) for j in y for i in x if (i,j) != s]

f = input('File name : ')
with open(f) as inp_file : 
    lines = inp_file.readlines()
    part_nums = []
    nodes = create_nodes(lines)
    special_nodes = [x for x in nodes if x[0].isdigit()] # All the digits
    special_chars_coords = [x[1] for x in nodes if not x[0].isalnum()] # All the special characters
    for node, n in special_nodes : 
        for coords in n : 
            x, y = coords
            x_n = [x-1, x, x+1]
            y_n = [y-1, y, y+1]
            c = create_combos(x_n, y_n, (x,y))
            for i in c : 
                if i in special_chars_coords : 
                    part_nums.append(int(node))
                    break
            else : continue
            break
    print(sum(part_nums))

    gears = [x[1] for x in nodes if x[0] == "*"]
    gear_sum = 0 
    for g in gears : 
        x, y = g
        x_n = [x-1, x, x+1]
        y_n = [y-1, y, y+1]
        c = create_combos(x_n, y_n, (x,y))
        mul = 1
        vals = {}
        for i in c : 
            for j, coord in special_nodes : 
                if i in coord : 
                    if j in vals and vals[j] == coord[0] :
                        continue
                    vals[j] = coord[0]

        if len(vals) == 2 : 
            for k in vals : mul *= int(k)
            gear_sum += mul
            
    print(gear_sum)