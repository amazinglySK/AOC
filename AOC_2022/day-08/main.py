def mod_score_perspective(to_edges) : 
    r = to_edges
    r[0] = r[0][::-1]
    r[2] = r[2][::-1]

    return r

def calc_scenic_score(score, to_edges) :
    new_sc = mod_score_perspective(to_edges)
    ssc = 1
    for sc in new_sc:
        enc = 0
        for s in sc : 
            enc += 1
            if s >= score : # blocked
                break     
        ssc *= enc 

    return ssc


def check_visible(score, to_edges):
    visibility = []
    for line in to_edges:
        for s in line:
            if s >= score : 
                visibility.append(False)
                break 
        else:
            visibility.append(True)

    if any(visibility) :
        return True
    return False


n = input("Enter the file name : ")

with open(n, 'r') as inp_file:

    lines = inp_file.read().strip().split("\n")
    score_matrix = [[int(y) for y in x] for x in lines]
    visible = 4*(len(score_matrix) - 1)
    max_scenic_score = 0

    for y, line in enumerate(score_matrix[1:len(score_matrix)-1]):
        for x, score in enumerate(line):
            if x == 0 or x == len(line) - 1:
                continue
            horizontal_edges = [line[:x], line[x+1:]]
            vertical_edges = [[l[x] for l in score_matrix[:y+1]], [l[x] for l in score_matrix[y+2:]]]

            to_edges = horizontal_edges + vertical_edges
            if check_visible(score, to_edges) :
                visible += 1
            
            sc = calc_scenic_score(score, to_edges)
            if sc > max_scenic_score:
                max_scenic_score = sc

    print("Part 1 answer : ", visible)
    print("Part 2 answer : ", max_scenic_score)
