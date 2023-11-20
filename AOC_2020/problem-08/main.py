def simulate_part2(visited, instructions, acc) : 
    idx = visited.pop()
    acc_copy = acc
    instructions_copy = instructions.copy()
    inst = instructions[idx][:3]

    if inst == "acc" : 
        acc -= int(instructions[idx][3:])
        return simulate_part2(visited, instructions, acc)
    
    visited_copy = visited.copy()
    if inst == "jmp" : 
        inst = "nop"
    elif inst == "nop" : 
        inst = "jmp"
    instructions[idx] = inst + instructions[idx][3:]

    while idx < len(instructions):
        sp = instructions[idx].split()
        i, v = sp[0], int(sp[1])
        if idx in visited : 
            break
        visited.append(idx)
        if i == "jmp" : 
            idx += v
            continue
        elif i == "nop" : pass
        elif i == "acc" : acc += v
        idx += 1
    else : 
        return acc

    return simulate_part2(visited_copy, instructions_copy, acc_copy)

    

with open("input.txt", 'r') as inp_file : 
    lines = inp_file.readlines()
    acc = 0
    instructions = [l.strip() for l in lines]
    visited = []
    idx = 0
    while True:
        sp = instructions[idx].split()
        i, v = sp[0], int(sp[1])
        if idx in visited : 
            break
        visited.append(idx)
        if i == "jmp" : 
            idx += v
            continue
        elif i == "nop" : pass
        elif i == "acc" : acc += v
        idx += 1
    print(acc)
    print(simulate_part2(visited, instructions, acc))


