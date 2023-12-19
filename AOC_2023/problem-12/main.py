# Huge thanks to @MattieShoes on Reddit for part 1
import sys

def check(s, b) : 
    x = [x for x in s.split(".") if x != ""]
    return x == ["#"*y for y in b]

def compute(s, b):
    if "?" not in s : 
        if check(s, b) : return 1
        else : return 0

    enc = False
    cb = []
    c = 0 
    for i in s : 
        if i == "#" : enc = True; c += 1
        elif i == "?" : break
        elif i == "." :
            if enc : 
                cb.append(c)
                c = 0
                enc = False
    if cb != b[:len(cb)] : return 0

    idx = s.index("?")
    a = s[:idx] + "#" + s[idx+1:]
    bs = s[:idx] + "." + s[idx+1:]
    return compute(a, b) + compute(bs, b)

f = sys.argv[1] 
with open(f) as fp: 
    lines = fp.read().strip().split("\n")
    sm = 0
    for i in lines : 
        s, b = tuple(i.split())
        b = [int(x) for x in b.split(",")]
        c = compute(s, b)
        sm += c
    print(sm)

