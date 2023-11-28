def create_triplets(x, y, z)  : 
    t = []
    for i in x : 
        for j in y:
            for k in z : 
                t.append((i, j, k))
    return t

def simulate_round(blocks) : 
    x_c = [x[0] for x in blocks]
    y_c = [x[1] for x in blocks]
    z_c = [x[2] for x in blocks]

    new_blocks = set()

    for i in range(min(x_c) - 1, max(x_c) + 2) : 
        for j in range(min(y_c) - 1, max(y_c) + 2) : 
            for k in range(min(z_c) - 1, max(z_c) + 2) : 
                # neighbours
                coord = (i, j, k)
                x_combo = [i-1, i+1, i]
                y_combo = [j-1, j+1, j]
                z_combo = [k-1, k+1, k]
                
                trips = create_triplets(x_combo, y_combo, z_combo)
                
                c = 0
                for neigh in trips : 
                    if neigh == (i, j, k) : 
                        continue
                    if neigh not in blocks : 
                        continue
                    if neigh in blocks: 
                        c += 1

                if coord in blocks and c in [2, 3] : 
                    new_blocks.add(coord)
                elif coord not in blocks and c == 3 : 
                    new_blocks.add(coord) 
    
    return new_blocks

def create_quadruples(x, y, z, w) : 
    t = []
    for i in x : 
        for j in y:
            for k in z : 
                for l in w: 
                    t.append((i, j, k, l))
    return t

def simulate_4d(blocks): 
    x_c = [x[0] for x in blocks]
    y_c = [x[1] for x in blocks]
    z_c = [x[2] for x in blocks]
    w_c = [x[3] for x in blocks]

    new_blocks = set()

    for i in range(min(x_c) - 1, max(x_c) + 2) : 
        for j in range(min(y_c) - 1, max(y_c) + 2) : 
            for k in range(min(z_c) - 1, max(z_c) + 2) : 
                for l in range(min(w_c) - 1, max(w_c) + 2) : 
                # neighbours
                    coord = (i, j, k, l)
                    x_combo = [i-1, i+1, i]
                    y_combo = [j-1, j+1, j]
                    z_combo = [k-1, k+1, k]
                    w_combo = [l-1, l+1, l] 

                    quads = create_quadruples(x_combo, y_combo, z_combo, w_combo)
                    
                    c = 0
                    for neigh in quads: 
                        if neigh == (i, j, k, l) : 
                            continue
                        if neigh not in blocks : 
                            continue
                        if neigh in blocks: 
                            c += 1

                    if coord in blocks and c in [2, 3] : 
                        new_blocks.add(coord)
                    elif coord not in blocks and c == 3 : 
                        new_blocks.add(coord) 
    
    return new_blocks

f = input("File name : ")
with open(f) as inp_file : 
    l = inp_file.read().strip().split("\n")
    blocks = set()
    blocks_4d = set()
    z = 0
    for y in range(len(l)) : 
        for x in range(len(l[y])) :
            coord = (x, y, z)
            coord_4d = (x, y, z, 0)
            if l[y][x] == "#" : 
                blocks.add(coord)
                blocks_4d.add(coord_4d)
    
    for _ in range(6) : 
        blocks = simulate_round(blocks)
    
    print(len(blocks))

    for _ in range(6) : 
        blocks_4d = simulate_4d(blocks_4d)

    print(len(blocks_4d))
    
