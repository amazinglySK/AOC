import numpy as np 
from math import cos, radians, sin, fabs
f = input("File name : ")
with open(f) as inp_file : 
    instructions = [x.strip() for x in inp_file.readlines()]
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)] # ESWN
    x, y = 0, 0
    idx = 0
    for inst in instructions : 
        v = int(inst[1:])
        if inst[0] == "L" :
            idx = (idx + (-v//90)) % 4
        elif inst[0] == "R" : 
            idx = (idx + (v//90)) % 4

        elif inst[0] == "F" : 
            dx, dy = vectors[idx]
            x += dx*v
            y += dy*v
        elif inst[0] == "N" : y -= v
        elif inst[0] == "S" : y += v
        elif inst[0] == "W" : x -= v
        elif inst[0] == "E" : x += v

    print(int(fabs(x) + fabs(y)))

    x, y = 0, 0
    wx, wy = 10, 1
    for inst in instructions : 
        v = int(inst[1:])
        if inst[0] in "LR" :
            d = 0
            if inst[0] == "L" : 
                d = radians(v)
            else:
                d = -radians(v)
            s, c = int(sin(d)), int(cos(d))
            rot = np.array([[c, s], [-s, c]])
            vec = np.array([wx, wy])
            prod = vec.dot(rot)
            wx, wy = prod[0], prod[1]

        if inst[0] == "F" : 
            x += wx * v
            y += wy * v

        elif inst[0] == "N" : wy += v
        elif inst[0] == "S" : wy -= v
        elif inst[0] == "W" : wx -= v
        elif inst[0] == "E" : wx += v

    print(int(fabs(x) + fabs(y)))

