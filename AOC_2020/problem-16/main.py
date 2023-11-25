import re 

def get_ranges(ranges): 
    all_vals = set()
    for l in ranges.split("\n") : 
        x = re.search(': ([0-9]|or|-| )+', l)
        s = ""
        if x : s = x.group()[2:]
        rg = s.split(" or ")
        for i in rg : 
            sp = i.split("-")
            st = set(range(int(sp[0]), int(sp[1]) + 1))
            all_vals = all_vals.union(st)
    return all_vals

def get_field_ranges(ranges) : 
    all_vals = {}
    for l in ranges.split("\n") : 

        f = re.search("([a-z]| )+:", l)
        key = ""
        if f : key = f.group()[:-1]
        all_vals[key] = set()

        x = re.search(': ([0-9]|or|-| )+', l)
        s = ""
        if x : s = x.group()[2:]
        rg = s.split(" or ")

        for i in rg : 
            sp = i.split("-")
            st = set(range(int(sp[0]), int(sp[1]) + 1))
            all_vals[key] = all_vals[key].union(st)

    return all_vals

f = input('File name :') 
with open(f) as inp_file : 
    chunks = inp_file.read().split('\n\n')
    ranges = chunks[0]
    range_set = get_ranges(ranges)
    all_seats = chunks[2].strip().split("\n")[1:]
    all_seats_copy = chunks[2].strip().split("\n")[1:]
    s = 0
    idx = 0
    flag = False
    for seat in all_seats : 
        nos = seat.split(",")
        for no in nos :
            if int(no) not in range_set : 
                s += int(no)
                break
        else : 
            idx += 1
            continue
        all_seats_copy.pop(idx)

    print(s)

    seat_ranges = get_field_ranges(ranges)
    s = [[int(x) for x in s.split(",")] for s in all_seats_copy]
    allocation = {}
    for i in range(len(seat_ranges)): 
        row = {j[i] for j in s}
        allocation[i] = set()
        for k in seat_ranges : 
            if seat_ranges[k].issuperset(row) : 
                allocation[i].add(k)
    
    final_allocation = {}
    allocation_list = sorted(list(allocation.items()), key = lambda x : len(x[1]))
    prev = set()
    for j, value in allocation_list : 
        s, prev = value - prev, value
        field = list(s)[0]
        final_allocation[j] = field
    
    cols = [i for i in final_allocation if final_allocation[i].startswith('departure')] 
    values = [int(x) for x in chunks[1].split("\n")[1].split(",")]
    mul = 1
    for col in cols : 
        mul *= values[col]
    print(mul)

    
        



