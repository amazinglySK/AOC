print("Hello World")


def calc_score(c : str) :
    if c.isupper() : 
        return ord(c) - 38
    else:
        return ord(c) - 96



def check_common(l) : 

    # Splitting
    f = l[0:len(l)//2]
    s = l[len(l)//2:]

    for i in f : 
        if i in s:
            return i

    return "a"

def find_badge(lines) : 
    
    for i in lines[0]:
        if i in lines[1] and i in lines[2]:
            return i
    return ""
    

with open("input.txt", 'r') as inp_file :
    lines = inp_file.readlines()
    score = 0
    alt_score = 0
    temp = []
    for line in lines : 
        c = check_common(line)
        score += calc_score(c)

        temp.append(line)
        if len(temp) == 3:
            b = find_badge(temp)
            alt_score += calc_score(b)
            temp = []

    print(score)

    print("--Part-2--")

    print(alt_score)
