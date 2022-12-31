
def app_val(cyc, x, val) :
    if cyc in [20, 60, 100, 140, 180, 220]:
        val.append(cyc*x)

def rectify_crt_img(img, vals) : 
    
    for idx, v in enumerate(vals) : 
        row = idx//40
        col = idx%40 - 1
        if v == 1:
            img[row][col] = "#"

    return img

def print_img(img) : 
    for i in img : 
        print("".join(i))

file = input("Enter the input file name : ")

with open(file, 'r') as inp_file : 
    lines = inp_file.readlines()
    
    x = 1
    cycle_no = 1
    adding = False
    values = []
    val = 0
    curr_line = 0

    crt = []

    while cycle_no <= 240 :
        # During cycle. The CRT line is printed here.
        app_val(cycle_no, x, values)
        
        crt.append(int(cycle_no%40 in range(x, x+3)))

        if adding : 
            x += val
            adding = False
            curr_line += 1
        elif lines[curr_line].split()[0] == "noop":
            curr_line += 1
        else:
            sp = lines[curr_line].split()
            adding = True
            val = int(sp[-1])

        # End of Cycle. The new sprite position if there's one is determined here
        cycle_no += 1
    
    crt_img = [["." for _ in range(40)] for _ in range(6)]
    f_img = rectify_crt_img(crt_img, crt)

    print("Part 1 :", sum(values))
    print("Part 2 : ")
    print_img(f_img)
