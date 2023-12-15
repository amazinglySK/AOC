import sys
from collections import defaultdict

def evaluate_expr(s) : 
    v = 0
    for ch in s : 
        v += ord(ch)
        v = v*17%256
    return v

f = sys.argv[1]
with open(f) as fp : 
    s = fp.read().strip()
    sum = 0

    # Part 1
    for i in s.split(",") : 
        sum += evaluate_expr(i)
    print(sum)

    # Part 2
    boxes = defaultdict(list)
    for i in s.split(",") : 
        if i.endswith("-") : 
            l, o = i[:-1], "-"
        else : 
            l, o = i.split("=")[0], "="

        b_no = evaluate_expr(l)
        labels = [x[0] for x in boxes[b_no]]
        if o == "-" : 
            if l in labels: 
                idx = labels.index(l)
                boxes[b_no].pop(idx)
        if o == "=":
            v = int(i[-1])
            if l in labels: 
                idx = labels.index(l)
                boxes[b_no][idx] = (l, v)
            else : 
                boxes[b_no].append((l, v))

    sum = 0
    for k in boxes : 
        for idx, l in enumerate(boxes[k]) : 
            sum += (k+1)*(idx+1)*l[1]
    print(sum)
