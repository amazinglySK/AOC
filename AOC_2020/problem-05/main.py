def division(start, end, code, limit, chars, current_iter = 0) -> tuple | int:
    if current_iter == limit:
        return start
    if code[current_iter] == chars[0]:
        end = (start + end - 1)//2
    elif code[current_iter] == chars[1]:
        start = (start + end + 1)//2 
    return division(start, end, code, limit, chars, current_iter+ 1)

def create_id(row,col) -> int:
    return row*8 + col

with open('input.txt', 'r') as input_file:
    codes = input_file.read().strip().split('\n')
    ids = []
    seats = []
    for code in codes:
        row = division(0, 127, code[0:7], 7, ('F', 'B'))
        col = division(0, 7, code[7:10], 3, ('L', 'R'))
        ids.append(create_id(row, col))
        seats.append((row, col)) 
    
    # Analyze the missing seats
    for j in range(0, 7) : 
        for i in range(1, 127) : 
            if (i, j) not in seats: 
                # print(i, j)
                pass
    
    # Checked for the isolated seat
    print("Part 1")
    print(max(ids))
    print("Part 2")
    print(create_id(84, 6))
