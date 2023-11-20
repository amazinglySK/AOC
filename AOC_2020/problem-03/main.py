def create_matrix() : 
    lst = []

    with open('./input.txt', 'r') as file:
        lines = file.readlines()
        for l in lines : 
            lst.append([True if x == "#" else False for x in l.strip()])
    
    return lst

# Part 1
'''
def main() :
    
    mat = create_matrix()
    pos = [0, 0]
    trees = 0

    while pos[1] < len(mat):
        x, y = pos[0], pos[1]
        if x >= len(mat[0]) : x = x%len(mat[0])
        if mat[y][x] : trees += 1
        pos[0] += 3
        pos[1] += 1

    print(trees)
'''
 
# Part 2
def main() : 
    mat = create_matrix()
    slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
    ans = 1

    for dx, dy in slopes:
        pos = [0, 0]
        trees = 0
        while pos[1] < len(mat):
            x, y = pos[0], pos[1]
            if x >= len(mat[0]) : x = x%len(mat[0])
            if y >= len(mat) : y = y%len(mat)
            if mat[y][x] : trees += 1
            pos[0] += dx
            pos[1] += dy
        ans *= trees

    print(ans)

if __name__ == "__main__" : 
    main()

        