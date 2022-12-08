print("Hello World")


def expand(rng) : 
    l, u = rng.split("-")
    return set(range(int(l), int(u) + 1))


with open("input.txt", 'r') as inp_file:
    lines = inp_file.readlines()
    total = len(lines)
    count = alt_count = 0
    for pair in lines:
        s = pair.split(",")
        a = expand(s[0])
        b = expand(s[1])
        if a.intersection(b) == a or a.intersection(b) == b :
            count += 1
        elif a.intersection(b) == set():
            alt_count += 1
    
    print(count)
    print("--Part-2--")
    print(total - alt_count)

