
with open("input.txt", 'r') as inp_file:
    lines = inp_file.readlines()
    sides = [x.split() for x in lines]
    count = 0
    for side_set in sides :
        w_set = sorted([int(x) for x in side_set])
        print(w_set)
        if sum(w_set[0:2]) > w_set[2]:
            print(sum(w_set[0:2]))
            count+=1

    print(count)

    for i in range(3):
        for j in sides:
            

