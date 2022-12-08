def check_inequality(side_set) :
    w_set = sorted([int(x) for x in side_set])
    return sum(w_set[0:2]) > w_set[2]


with open("input.txt", 'r') as inp_file:
    lines = inp_file.readlines()
    sides = [x.split() for x in lines]
    count = 0
    for side_set in sides :
            if check_inequality(side_set):
                count+=1

    print(count)


    count = 0 
    for i in range(3):
        tmp = []
        for j in sides:
            tmp.append(j[i])
            if len(tmp) == 3:
                if check_inequality(tmp):
                    count += 1
                tmp = []
            
            
    print(count)
