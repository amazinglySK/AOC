import re


class Stack : 
    
    def __init__(self, l : list): 
        self.containers = l[::-1]
    
    def pop(self, n):
        elements = []
        for _ in range(n):
            e = self.containers.pop()
            elements.append(e)
        return elements

    def add(self, l: list) : 
        self.containers += l

    def get_top(self):
        return self.containers[-1]

def parse_raw(lines):
    s = lines.split("\n\n")
    curr, inst = s[1], s[2].split("\n")

    curr = curr.split("\n") 

    # Parsing the initial structure
    struct = {}
    alt_struct = {}
    for idx, i in enumerate(curr) : 
        s = i.split(", ")
        struct[idx + 1] = Stack(s)
        alt_struct[idx + 1] = Stack(s)

    # Parsing the instructions
    p = re.compile(r"^move (\d+) from (\d+) to (\d+)$")    
    results = []
    for i in inst : 
        i = i.strip()
        res = p.findall(i)[0]
        res = tuple([int(x) for x in res])
        results.append(res)

    return struct, alt_struct, results
    

inp = input("Enter the name of the input file : ")
with open(inp, 'r') as inp_file:
    raw = inp_file.read().strip()
    res, alt_res, inst = parse_raw(raw)

    for i in inst : 
        n, orig, dest = i
        items = res[orig].pop(n)
        res[dest].add(items)

        items = alt_res[orig].pop(n)
        alt_res[dest].add(items[::-1])
    
    values = []
    alt_values = []
    for value in res.values():
        values += value.get_top()

    for v in alt_res.values():
        alt_values += v.get_top()

    print("".join(values))
    print("".join(alt_values))
