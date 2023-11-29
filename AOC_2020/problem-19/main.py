def parse_rules(rules) : 
    r = {}

    for l in rules : 
        sp = l.split(": ")
        if sp[1].startswith('\"') : 
            r[sp[0]] = sp[1][1:-1]
            continue
        rule_sets = sp[1].split(" | ")
        rule = tuple([x.split() for x in rule_sets])
        r[sp[0]] = rule

    return r

def create_combos(rules, rule) : 
    
    if type(rules[rule]) != tuple : 
        return rules[rule]

    combos = []

    for r in rules[rule]: # Each rule set
        temp_combo = [""]
        for i in r : # Each rule 
            combo= create_combos(rules, i)
            count = 0
            t = []
            for i in temp_combo : 
                count+=1
                t.extend([i + x for x in combo])
            temp_combo = t
        
        combos.extend(temp_combo)
    return combos
        

f = input("File name : ")
with open(f) as inp_file :
    chunks = inp_file.read().split("\n\n")
    rules = chunks[0].split("\n")
    r = parse_rules(rules)

    combos = create_combos(r, "0")
    c = 0
    for i in chunks[1].split("\n") : 
        if i in combos : 
            c += 1
    print(c)
