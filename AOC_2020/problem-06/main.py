with open('input.txt', 'r') as input_file:
    groups = [x for x in input_file.read().strip().split('\n\n')]
    groups = [[i for i in x if i != '\n'] for x in groups]
    counts = [set(group) for group in groups]
    sums = [len(group) for group in counts]
    print(sum(sums))
    

    input_file.seek(0)
    groups = [x for x in input_file.read().strip().split('\n\n')]
    groups_count = []
    for group in groups :
        people = group.split('\n')
        if len(people) == 1: 
            groups_count.append(len(people[0]))
            continue
        g_count = 0
        for i in people[0] : 
            if all([i in j for j in people[1:]]) : 
                g_count += 1

        groups_count.append(g_count)
    
    print(sum(groups_count))
