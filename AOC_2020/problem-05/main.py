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
    rows = []
    cols = []
    ids = []
    for code in codes:
        row = division(0, 127, code[0:7], 7, ('F', 'B'))
        col = division(0, 7, code[7:10], 3, ('L', 'R'))
        rows.append(row)
        cols.append(col)
        ids.append(create_id(row, col))

    for i in range(min(rows), max(rows) + 1):
        if i not in rows:
            our_row = i
    for i in range(min(cols), max(cols) + 1):
        if i not in cols:
            our_col = i

    print(create_id(our_row, our_col))
    print(max(ids))