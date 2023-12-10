# Receiving and connecting vectors
pipe_type = {
    "|" : {(0, 1) : (0, 1), (0, -1) : (0, -1)},
    "-" : {(-1, 0) : (-1, 0), (1, 0) : (1, 0)},
    "L" : {(0, 1) : (1, 0), (-1, 0) : (0, -1)},
    "J" : {(0, 1) : (-1, 0), (1, 0) : (0, -1)},
    "7" : {(1, 0) : (0, 1), (0, -1) : (-1, 0)},
    "F" : {(0, -1) : (1, 0), (-1, 0) : (0, 1)},
}

def create_network(lines) : 
    l = [[ch for ch in l] for l in lines]
    for j in range(len(l)) : 
        for i in range(len(l[j])) : 
            ch = lines[j][i]
            if ch == "S" :
                return l, (i, j)
    return l, None

def check_compatibility(c, d) : # Takes the character and the direction vector
    if c == "." : 
        return False
    dirs = pipe_type[c]
    if d in dirs : 
        return dirs[d]
    return None

def find_valid_neighbours(coord, net) : 
    x, y = coord
    x_n = [-1, +1]
    y_n = [-1, +1]
    v = []
    for i in x_n : 
        ch = net[y][x + i]
        comp = check_compatibility(ch, (i, 0))
        if comp : 
            v.append(((x + i, y), (i, 0)))
    for i in y_n : 
        ch = net[y + i][x]
        if check_compatibility(ch, (0, i)) : 
            v.append(((x, y + i), (0, i)))
    return v

def traverse(coord, net, prev_vec, acc = []) :
    while True: 
        x, y = coord
        ch = net[y][x]
        if ch == "S" : break
        c = check_compatibility(ch, prev_vec)
        if not c : break 
        dx, dy = c
        acc.append(coord)
        coord = (x + dx, y + dy)
        prev_vec = dx, dy

    return acc

f = input('File name : ')
with open(f) as inp_file : 
    lines = inp_file.read().strip().split("\n")
    net, s= create_network(lines)
    neigh = find_valid_neighbours(s, net)

    m = 0
    for i, prev_vec in neigh : 
        t = traverse(i, net, prev_vec, acc = [])
        half_d = (len(t) + 1) // 2
        if half_d > m : 
            m = half_d

    print(m)
