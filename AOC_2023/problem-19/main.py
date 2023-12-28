import sys

f = sys.argv[1] 

def parse_instructions(instructions) :
    out = {}
    for line in instructions.split("\n") : 
        idx = line.index("{")
        workflow = line[:idx]
        v = line[idx:].strip("{}")
        splits = [tuple(i.split(":")) for i in v.split(",")]
        out[workflow] = splits
    return out
        
def run_workflow(splits, x, m, a, s) : 
    for condition, action in splits[:-1]: 
        if eval(condition) : return action
    return splits[-1][-1]

def simulate(w, x, m, a, s, inst) : 
    sm = 0
    while True :
        w = run_workflow(inst[w], x, m, a, s)
        if w in "AR" :
            if w == "A" : sm += x + m + a + s
            break
    return sm

def find_conditions(w, s, m, inst):
    if w == "R" : 
        return False
    elif w == "A": 
        return True
    
    final = []
    print(w, inst[w])
    for (conditions, action) in inst[w][:-1] :
        cond = find_conditions(action, s, m, inst)
        if cond : 
            final.extend(conditions)
    
    return final

with open(f) as fp : 
    instructions, data = fp.read().strip().split("\n\n")

    inst_set = parse_instructions(instructions)
    ans = 0
    for l in data.split("\n") : 
        x, m, a, s = [int(x.split("=")[1]) for x in l.strip("{}").split(",")]
        v = simulate("in", x, m, a, s, inst_set)
        ans += v
    print(ans)

    find_conditions("in", 1, 4000, inst_set)


