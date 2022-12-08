
with open("input.txt") as inp_file : 
    split = inp_file.read().strip().split("\n\n")
    total = 0
    dict = {}
    
    for idx, set in enumerate(split): 
        s = sum([int(x) for x in set.split("\n") if x != " " or x != ""])
        dict[idx] = s

    # Part 1
    max_score = max(dict.values())
    print("Part 1 answer : ")
    print(max_score)


    # Part 2
    print("Part 2 answer : ")
    sum_score = sorted(dict.values(), reverse = True)
    print(sum(sum_score[:3]))



        
