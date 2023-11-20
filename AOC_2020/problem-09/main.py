def sliders(sub, target)  : 
    start = 0
    end = len(sub) - 1

    for i in range(start, end) : 
        for j in range(i + 1, end + 1) : 
            r = sub[i:j+1]
            if sum(r) == target:
                return max(r) + min(r)
    return 0

with open("input.txt") as inp_file : 
    lines = inp_file.readlines()
    preamble_len = 25
    codes = [int(l.strip()) for l in lines]
    fail = 0
    fail_idx = 0
    for i in range(preamble_len, len(codes)) : 
        curr = codes[i]
        s = sorted(codes[i-preamble_len : i], reverse=True)
        for j in range(len(s)) :
            if curr - s[j] in s and curr != 2*s[j]: 
                break
        else : 
            fail = curr 
            fail_idx = i
            break
    print(fail)
    sub = codes[:fail_idx]
    print(sliders(sub, fail))

