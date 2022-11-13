import math

dirs = ["N", "W", "S", "E"]


def get_dir_on_rot(dir : str, curr : int) -> int :
    i = 0
    if dir == "L" :
        i = curr + 1
        if i > len(dirs) - 1:
            i = 0
    elif dir == "R" :
        i = curr - 1
        if i < 0:
            i = len(dirs)-1

    return i

def update(x : int, y : int, curr : int, val : int) -> tuple : 
    
    curr_str = dirs[curr]

    if curr_str == "N":
        y += val
    elif curr_str == "W":
        x -= val
    elif curr_str == "S":
        y -= val
    elif curr_str == "E":
        x += val
    else : 
        print("An error occured", curr_str)


    return (x, y)

with open("input.txt", "r") as inp_file : 
    lines = inp_file.read().strip().split(", ")
    instructions = [tuple([x[0], str(x[1:])]) for x in lines]
    curr = 0
    x = 0
    y = 0
    visited = [(0, 0)]
    for i in instructions:
        ins, v = i
        curr = get_dir_on_rot(ins, curr)
        x, y = update(x, y, curr, int(v)) 
        if tuple([x, y]) in visited:
            break
        visited.append((x, y))

    print(x, y)

    t = math.fabs(x) + math.fabs(y)

    print(int(t))

