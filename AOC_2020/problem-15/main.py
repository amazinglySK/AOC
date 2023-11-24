def run(l, max_l, turn_data, prev) : 
    for i in range(l + 1, max_l + 1) : 
        curr = turn_data[prev][1] - turn_data[prev][0]
        if curr not in turn_data : 
            turn_data[curr] = [i, i]
        else : 
            turn_data[curr][0] = turn_data[curr][1]
            turn_data[curr][1] = i
        prev = curr
    return prev

f = input("File name : ")
with open(f) as inp_file : 
    input = [int(i) for i in inp_file.read().strip().split(",")]
    turn_data = {input[i-1] : [i, i] for i in range(1, len(input)+1)}
    turn_data_copy = {input[i-1] : [i, i] for i in range(1, len(input)+1)}
    prev = input[-1]
    r = run(len(input), 2020, turn_data, prev)
    print(r) 
    r = run(len(input), 30000000, turn_data_copy, prev)
    print(r)
