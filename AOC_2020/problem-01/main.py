# Part 1

def find_nos(no, list, multiple = False):
    for i in list:
        diff = no - i
        if multiple == False:
            if diff in list:
                return [diff, i], diff*i
        else:
            nos, result = find_nos(diff, list)
            nos.append(i)
            if result != 0:
                return nos, i*result
    return [], 0
with open("input.txt", 'r') as input_file:
    INPUT = [int(x) for x in input_file.read().strip().split("\n")]
    expected_sum = 2020
    nos, result = find_nos(expected_sum, INPUT)
    print(f'Part 1 : {nos}\nanswer = {result}\n==========================================')
    nos, result = find_nos(expected_sum, INPUT, True)
    print(f'Part 2 : {nos}\nanswer = {result}\n==========================================')
        
        
    
    
