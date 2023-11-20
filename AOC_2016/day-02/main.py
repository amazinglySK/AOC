def gen_keypad() -> list[list[int]]: 
    prev = 1
    pad = []
    for _ in range(1, 4):
        n = prev + 2
        pad.append([x for x in range(prev, n + 1)])
        prev = n + 1

    return pad

def get_key_idx(key : str, pad: list[list[int]]) -> tuple : 
    for y, i in enumerate(pad):
        for x, j in enumerate(i):
            if str(j) == key:
                return x,y
    return (0, 0)

def next_key(x, y, k) -> tuple:

    if k == "U":
        y += 1

    elif k == "D":
        y -= 1

    elif k == "L":
        x -= 1

    elif k == "R":
        x += 1

    if x > 2:
        x = 2
    elif x < 0:
        x = 0
    elif y > 2:
        y = 2
    elif y < 0 :
        y = 0

    return x, y 


with open("sample-input.txt", 'r') as inp_file : 
    
    lines = inp_file.readlines()
    pad = gen_keypad()
    print(pad)

    keys = ["5"]

    for line in lines : 
        k = keys[-1]
        print(k)
        for d in line.strip() :
            x, y = get_key_idx(str(k), pad)
            x, y = next_key(x, y, d)
            k = str(pad[y][x])
            print(d, x, y, k)
        keys.append(str(k))

    print(int("".join(keys)))


