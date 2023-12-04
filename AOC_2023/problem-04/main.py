
def scratch_cards(card_no, lines, M) : 
    c = lines[card_no]

    if card_no in M : 
        return M[card_no]

    if c == 0 : return 1
    else : 
        count = 0
        for i in range(card_no + 1, card_no + c + 1):
            count += scratch_cards(i, lines, M)
        M[card_no] = count + 1
        return M[card_no]


f = input('File name : ')
with open(f) as inp_file : 
    lines = inp_file.readlines()
    w = 0
    card_record = []
    for l in lines : 
        l = l.strip()
        sp = l.split(":")[1]
        s = sp.split(" | ")
        winning = s[0].split(" ")
        nums = s[1].split(" ")
        c = 0
        for i in winning : 
            if i == "" : continue
            if i in nums : 
                c += 1

        card_record.append(c)
        if c : w += 2**(c-1)
    
    print(w)

    card_count = 0
    memo = {}
    for i in range(len(lines)):
        card_count += scratch_cards(i, card_record, memo)

    print(card_count)
