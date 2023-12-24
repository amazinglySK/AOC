import math
# Vector maths

def cross(a, b, d = 3) :
    if d == 2 : 
        x1, y1 = a[:2]
        x2, y2 = b[:2]
        return (x1*y2 - x2*y1)

    x1, y1, z1 = a
    x2, y2, z2 = b
    x, y, z = (y1*z2 - y2*z1, -x1*z2 + x2*z1, x1*y2 - x2*y1)
    return (x, y, z)

def mag(a) : 
    m = 0
    for i in a : 
        m += i**2
    return math.sqrt(m)

def dot(a, b) :
    d = 0
    for i, j in zip(a, b) : 
        d += i*j
    return d

def diff(a, b) :
    r = tuple()
    for i, j in zip(a, b) : 
        r += (i - j,)
    return r

def reduce(a) :
    d=  math.gcd(*a)
    f = tuple()
    for i in a :
        f += (i//d,)
    return f
