def create_graph(jolts) :
    graph = {} 
    r = range(1, 4)
    idx = 0
    for i in jolts : 
        s = jolts[idx + 1 : idx + 4]
        graph[i] = [x for x in s if x - i in r]
        idx += 1
    
    return graph

def traverse(graph, v, M = {}) : 
    # Memoizing according to @rune_kg on reddit
    if v in M : 
        return M[v]
    elif graph[v] : 
        M[v] = sum([traverse(graph, x, M) for x in graph[v]])
        return M[v]
    else : 
        return 1

file_name = input("Input file : ")
with open(file_name) as inp_file : 
    jolts = [int(l.strip()) for l in inp_file.readlines()]
    jolts.sort()
    jolts_diff = [0, 0]
    start = 0
    for i in jolts : 
        if i - start == 3: jolts_diff[0] += 1
        elif i - start == 1 : jolts_diff[1] += 1
        start = i
    jolts_diff[0] += 1
    print(jolts_diff[0] * jolts_diff[1])
    jolts.insert(0, 0)
    end = jolts[-1] + 3
    jolts.append(end)
    g = create_graph(jolts)
    s = traverse(g, 0)
    print(s)
