def crt(r_mod_pairs):
    # 0mod7 = (7, 0)
    LCM = r_mod_pairs[0][0]
    prev = r_mod_pairs[0][1]
    for i in range(len(r_mod_pairs[:-1])) : 
        mod, r = r_mod_pairs[i+1]
        lcm = LCM%mod
        p = prev%mod
        r_set = [(p + lcm*i) % mod for i in range(mod)]
        for idx in range(len(r_set)) : 
            i = r_set[idx]
            if i == r % mod:
                prev += LCM*idx
                LCM  = get_lcm(LCM, mod)
                break
        else:
            break
    
    return LCM - prev

def get_lcm(a, b) :
    l = a
    while l % b != 0 : 
        l += a
    return l

def create_mod_pairs(data) : 
    lines = data[1].strip().split(",")
    pairs = []
    idx = 0
    for i in lines : 
        if i != "x" : pairs.append((int(i), idx))
        idx += 1
    return pairs


f = input("File name :")
with open(f) as inp_file : 
    lines = inp_file.readlines()
    minutes = int(lines[0].strip())
    l = [int(x) for x in lines[1].strip().split(",") if x.isdigit()]
    waiting = [x - minutes % x for x in l]
    min_waiting = min(waiting)
    idx = waiting.index(min_waiting)
    print(l[idx] * min_waiting)
    pairs = create_mod_pairs(lines)
    c = crt(pairs)
    print(c)

