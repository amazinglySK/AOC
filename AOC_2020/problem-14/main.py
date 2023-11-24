import re

chunks = {}
def parse_input(lines) : 
    curr_key = ""
    global chunks
    for l in lines : 
        l = l.strip()
        if l.startswith("mask = ") : 
            v = l.split(" = ")[1]
            curr_key = v
            chunks[curr_key] = {}
        elif l.startswith("mem") : 
            sp = l.split(" = ")
            x = re.search("\[[0-9]+\]", sp[0])
            s = ""
            if x : s = x.group()[1:-1]
            chunks[curr_key].update({s : "{0:036b}".format(int(sp[1]))})

def update_mem(chunks) : 
    global mem
    for mask in chunks : 
        for mem_add in chunks[mask] : 
            mem[mem_add] = masking(mask, chunks[mask][mem_add])

def update_mem_v2(chunks) : 
    global mem
    for mask in chunks : 
        for mem_add in chunks[mask] : 
            mem_bin = "{0:036b}".format(int(mem_add))
            mem_add_mask = masking_v2(mask, mem_bin)
            mem_add_combos = gen_combos(mem_add_mask)
            for i in mem_add_combos :
                mem[i] = chunks[mask][mem_add]

def masking(mask, val) : 
    final = ""
    idx = -1
    for ch in val[::-1] : 
        if mask[idx] == "X" : final = ch + final
        else : 
            final = mask[idx] + final
        idx -= 1
    return final

def masking_v2(mask, val) :
    final = ""
    idx = -1
    for ch in val[::-1] : 
        if mask[idx] == "0" : final = ch + final
        else : 
            final = mask[idx] + final
        idx -= 1
    return final 

def gen_combos(add) : 
    floating = [len(add) - i - 1 for i in range(len(add)) if add[i] == "X"]
    non_floating = sum([2**(len(add) - i - 1) for i in range(len(add)) if add[i] == "1"])
    combo = [0]
    for i in floating[::-1]: 
        p = 2**i
        combo.extend([p + m for m in combo])
    adds = [x + non_floating for x in combo]
    return adds
            
f = input("File name : ")
mem = {}
with open(f) as inp_file : 
    lines = inp_file.readlines()
    parse_input(lines)
    update_mem(chunks)
    s = sum([int(mem[k], 2) for k in mem])
    print(s)

    # Part 2
    mem = {}
    update_mem_v2(chunks)
    s = sum([int(mem[k], 2) for k in mem])
    print(s)

