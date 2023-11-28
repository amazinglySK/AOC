def get_index_of_closing(expr, open_idx) : 
    stk = []
    stop = -len(expr) + open_idx
    pair = "()"
    for idx in range(-1, stop, -1) :
        if expr[idx] == pair[-1] :  
            stk.append(idx)
        if expr[idx] == pair[0] :
            stk.pop()
    return stk[0]

def give_postfix(exp) : 
    post = ""
    op = ""
    idx = 0
    pair = "()"
    while idx < len(exp) : 
        ch = exp[idx]
        if ch == pair[0] : 
            c_idx = get_index_of_closing(exp[idx:], 0)
            post += give_postfix(exp[idx+1:c_idx])
            idx = len(exp) + c_idx + 1
            continue
        elif ch in "*+"  : 
            post+=op
            op = ch
        else : 
            post += ch
        idx += 1
        
    return post + op


def give_postfix_v2(exp) : 
    post = ""
    op = []
    idx = 0
    pair = "()"
    prec = "*+"
    while idx < len(exp) : 
        ch = exp[idx]
        if ch == pair[0] : 
            c_idx = get_index_of_closing(exp[idx:], 0)
            post += give_postfix_v2(exp[idx+1:c_idx])
            idx = len(exp) + c_idx + 1
            continue
        elif ch in "*+"  : 
            if op == [] : 
                op.append(ch)
                idx += 1
                continue
            prev = op[-1]
            if prec.index(prev) < prec.index(ch) : # previous precedence is lower
                op.append(ch)
                idx += 1
                continue
            p = op.pop()
            post += p
            op.append(ch)
        else : 
            post += ch
        idx += 1
    
    while op != [] : 
        post += op.pop()

    return post

def evaluate_postfix(exp) : 
    stk = []
    for i in exp : 
        if i in "*+" : 
            a = stk.pop()
            b = stk.pop() 
            ans = str(eval(a + i + b))
            stk.append(ans)
        else : 
            stk.append(i)
    return int(stk[0])

f = input("File name : ")

with open(f) as inp_file : 
    expr = inp_file.readlines()
    s = 0
    s1 = 0
    for exp in expr : 
        p_fix = give_postfix(exp.strip())
        v = evaluate_postfix(p_fix)
        s += v

        p_fix_new = give_postfix_v2(exp.strip()) 
        v = evaluate_postfix(p_fix_new)
        s1 += v

    print(s)
    print(s1)
