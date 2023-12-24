
import sys
import math
import numpy as np
from itertools import combinations
from vectors import reduce, cross, mag, diff, dot

# Shortest distance
def sd(a1, b1, a2, b2) : 
    if reduce(b1) == reduce(b2) :
        return False
    c = cross(b1, b2, d=2)
    if c == 0 : return False
    else : return True

def find_sols(a1, b1, a2, b2, d = 2) :
    x1, y1 = a1[:d]
    x2, y2 = a2[:d]
    dx1, dy1 = b1[:d]
    dx2, dy2 = b2[:d]
    A = np.array([[dx1, -dx2], [dy1, -dy2]])
    C = np.array([[x2 - x1], [y2-y1]])
    A_in = np.linalg.inv(A)
    B = np.dot(A_in, C) # Solutions
    for i in B : 
        if i < 0: return None
        else : continue
    return B.tolist()

def calc_position(l, b, a, m) : 
    ml, mh = m
    dx, dy = b[:2]
    x, y = a[:2]
    tx, ty = [x[0] for x in l]
    disx = x + dx*tx
    disy = y + dy*tx

    if ml <= disx <= mh and ml <= disy <= mh and not (ty < 0 or tx < 0): 
        return True, (disx, disy)
    return False, tuple()
    

f = sys.argv[1] 
with open(f) as fp:
    lines = fp.readlines()
    paths = []
    for l in lines : 
        l = l.strip()
        a, b = l.split(" @ ")
        a = tuple(int(x) for x in a.split(", "))
        b = tuple(int(x) for x in b.split(", "))
        paths.append((a, b))

    c = 0
    limits = (200000000000000, 400000000000000)
    for i in combinations(paths, 2):
        a1, b1 = i[0]
        a2, b2 = i[1]
        if sd(a1, b1, a2, b2) : 
            l = find_sols(a1, b1, a2, b2)
            if l == None : continue 
            con, pos = calc_position(l, b1, a1, limits)
            if con :
                c += 1
    print(c)
