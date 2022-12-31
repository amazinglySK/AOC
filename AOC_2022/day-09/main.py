class Knot: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def check_in_vicinity(self, pos) -> bool:
        x, y = pos
        
        if x in range(self.x - 1, self.x + 2):
            if y in range(self.y - 1, self.y + 2):
                return True
        return False

    
    def move(self, pos):
        x, y = pos 
        self.x, self.y = x, y


dirs = {"R" : (1, 0) , "L" : (-1, 0), "U" : (0, 1), "D" : (0, -1)}

def execute_moves(inst, units, head, tail) -> list[tuple]:
    x_inc, y_inc= dirs[inst]
    vis = []
    for _ in range(units) :
        prev_x, prev_y = head.x, head.y
        head.move((prev_x + x_inc, prev_y + y_inc))
        if not tail.check_in_vicinity((head.x, head.y)):
            tail.move((prev_x, prev_y))
            vis.append((prev_x, prev_y))
    return vis

def execute_moves_rope(inst, units, rope : list[Knot]):
    x_inc, y_inc= dirs[inst]
    vis = []
    head = rope[0]
    tail = rope[:-1]
    for _ in range(units) :
        tmp_hd = head
        prev_x, prev_y = tmp_hd.x, tmp_hd.y
        tmp_hd.move((head.x + x_inc, head.y + y_inc))
        for i, k in enumerate(rope[1:]):
            if not k.check_in_vicinity((tmp_hd.x, tmp_hd.y)):
                p_x, p_y = k.x, k.y
                k.move((prev_x, prev_y))
                prev_x, prev_y = p_x, p_y
                if i == len(rope[1:]) - 1:
                    vis.append((prev_x, prev_y))
            tmp_hd = k
         
        print([(x.x, x.y) for x in rope])
    print(vis)
    return vis

file = input("Enter the input file name : ")

with open(file, 'r') as inp_file : 
    h = Knot(0, 0)
    t = Knot(0, 0)
    remaining_rope = [Knot(0, 0) for _ in range(8)]
    tail_visited = [(0,0)]
    lines = inp_file.readlines()

    for line in lines : 
        inst, units = line.split()
        vis = execute_moves(inst, int(units), h, t)
        tail_visited += vis 
    
    print(len(set(tail_visited)))

    h.x, h.y = 0, 0
    t.x, t.y = 0, 0
    rope = [h] + remaining_rope + [t]
    tail_visited = [(0, 0)]
    print([(x.x, x.y) for x in rope])
    for line in lines : 
        inst, units = line.split()
        vis = execute_moves_rope(inst, int(units), rope)
        tail_visited += vis
    print(len(set(tail_visited)))

