
import sys

def compute(s, b):
    if b == []  : 
        if "#" in s : return 0
        else : return 1

    cb = b.pop()
    enc = False

    for idx, i in enumerate(s) : 
        if i == "." : 
            if cb == 0 and enc : 
                if b == [] : continue
                else : cb = b.pop()
            elif enc and cb : return 0
            enc = False
        if i == "?" :
            if cb : 
                b += [cb]
                a = compute("#" + s[idx+1:], b.copy())
            else : a = 0
            bs = compute("." + s[idx+1:], b.copy())
            return a + bs
        if i == "#" : 
            cb -= 1
            enc = True
            if cb < 0 : return 0 
    

    if b != [] : return 0

    return 1
    

f = sys.argv[1] 
with open(f) as fp: 
    lines = fp.read().strip().split("\n")
    for i in lines : 
        s, b = tuple(i.split())
        b = [int(x) for x in b.split(",")]
        c = compute(s, b[::-1])
        print(c)

