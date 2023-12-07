from collections import Counter, defaultdict

def get_score_hand(h, mod = False) : 
    # Scores: 7..1
    c = Counter(h)
    if mod :  # Modified for part 2
        if h == "J"*5 : return 7
        joker = c.pop("J", 0)
        vals = [v for v in c.values()] 
        m = max(vals)
        for i in c : 
            if c[i] == m : 
                c[i] += joker
                break
        
    vals = [v for v in c.values()] 
    if len(c) == 1 : return 7
    elif len(c) == 2 : 
        if 4 in vals: return 6
        else : return 5
    elif len(c) == 3 : 
        if 3 in vals : return 4
        else : return 3
    else : 
        if 2 in vals : return 2
        else : return 1

def swap_or_no(a, b, prec) : 
    for i in range(len(a)) : 
        p, q = a[i], b[i]
        if prec.index(q) < prec.index(p) :
            return True
        if prec.index(p) < prec.index(q) : 
            return False
    return False

def sort_same_scores(s, mod = False) : 
    prec = "AKQJT98765432"[::-1]
    if mod : 
        prec = "AKQT98765432J"[::-1]
    n = len(s) 
    for i in range(n) : # Bubble Sort
        swapped = False
        for j in range(0, n-i-1) :
            if swap_or_no(s[j][0], s[j+1][0], prec) : 
                s[j], s[j+1] = s[j+1], s[j]
                swapped = True
        if swapped == False : 
            break

    return s

f = input('File name : ')

with open(f) as inp_file : 
    lines = inp_file.readlines()
    hands = [tuple(x.strip().split()) for x in lines]

    score_dict = defaultdict(int)
    score_dict_v2 = defaultdict(int)

    for i in hands :
        score_dict[i] += get_score_hand(i[0])
        score_dict_v2[i] += get_score_hand(i[0], mod = True)
    
    # Part 1
    final = []
    for k in set(score_dict.values()) : 
        same_scores = [x for x in score_dict if score_dict[x] == k]
        s = sort_same_scores(same_scores)
        final += s

    ans = sum([int(x[1])*(i+1) for i, x in enumerate(final)])
    print(ans)

     
    # Part 2
    final = []
    for k in sorted(set(score_dict_v2.values())) : 
        same_scores = [x for x in score_dict_v2 if score_dict_v2[x] == k]
        s = sort_same_scores(same_scores, mod = True)
        final += s

    ans = sum([int(x[1])*(i+1) for i, x in enumerate(final)])
    print(ans)

