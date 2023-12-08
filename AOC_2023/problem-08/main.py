from math import lcm

def create_network(l) : 
    d = {}
    for i in l : 
        n = i.split(" = ")
        d[n[0]] = n[1].strip("()").split(", ")
    return d

def traverse(inst, n) : 
    i = 0
    curr = "AAA"
    while curr != "ZZZ" : 
        ch = inst[i%len(inst)]
        if ch == "L" : curr = n[curr][0]
        else : curr = n[curr][1]
        i += 1
    return i

def traverse_v2(inst, n) : 
    st = [x for x in n if x[-1] == "A"]
    p = []
    for dir in st :
        curr = dir
        i = 0
        while curr[-1] != "Z" : 
            ch = inst[i%len(inst)]
            if ch == "L" : 
                curr = n[curr][0] 
            else :
                curr = n[curr][1]
            i += 1
        p.append(i) 

    return lcm(*p)

f = input('File name : ')
with open(f) as inp_file : 
    l = inp_file.read().strip().split("\n\n")
    instructions = l[0]
    network = l[1].split("\n")

    fn, network = create_network(network)

    c = traverse(instructions, network)
    print(c)

    c = traverse_v2(instructions, network)
    print(c)
