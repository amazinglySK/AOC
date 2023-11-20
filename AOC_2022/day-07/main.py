class File:
    def __init__(self, size, name):
        self.name = name
        self.size = size


class Directory : 

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = {}

    def add_file(self, f: File):
        self.files.append(f)

    def get_parent(self):
        if self.parent == None:
            return self
        else:
            return self.parent

    def add_folder(self, d): 
        self.folders[d.name] = d

    def change_dir(self, name):
        return self.folders[name]

    def calc_score(self):
        score = 0
        for i in self.files:
            score += i.size

        for i in self.folders.values():
            score += i.calc_score()
        return score

class FileSystem:

    def __init__(self):
        start_dir = Directory("/", None)
        self.sd = start_dir
        self.t_size = 70000000
        self.min_req = 30000000
        self.curr = start_dir
    
    def parse_cmds(self, lines) : 
        for line in lines :
            if line.startswith("$"):
                # Command
                s = line.removeprefix("$ ").split(" ")
                cmd, dir = s[0], s[-1]
                if cmd == "cd":
                    if dir == "..":
                        parent = self.curr.get_parent()
                        self.curr = parent
                    elif dir == "/":
                        sd = self.sd
                        self.curr = sd
                    else:
                        self.curr = self.curr.change_dir(dir)
                elif cmd == "ls":
                    continue
            else:
                if line.startswith("dir"):
                    s = line.removeprefix("dir ")
                    new_folder = Directory(s, self.curr)
                    self.curr.add_folder(new_folder)
                else:
                    s = line.split(" ")
                    size, name = int(s[0]), s[1]
                    new_file = File(size, name)
                    self.curr.add_file(new_file)

    def get_final_score(self, dirs : list[Directory], scores : list) : 
        if dirs == []:
            return scores
        r_sc = [x.calc_score() for x in dirs]
        sc = [x for x in r_sc if x <= 100000]
        nxt = []
        for i in dirs:
            nxt += i.folders.values()
        return self.get_final_score(nxt, scores + sc)
    
    def get_del_score(self, sd_sc : int, dirs : list[Directory], scores : list[int]):
        if dirs == []:
            return scores
        r_sc = [x.calc_score() for x in dirs]
        sc = [x for x in r_sc if (self.t_size - sd_sc + x) >= self.min_req]
        nxt = []
        for i in dirs:
            nxt += i.folders.values()
        return self.get_del_score(sd_sc, nxt, scores + sc)

file = input("Enter the file name : ")

with open(file, 'r') as inp_file : 
    lines = inp_file.read().strip().split("\n")
    fs = FileSystem()
    fs.parse_cmds(lines)

    scores = fs.get_final_score([fs.sd], [])

    print("\nPart 1")
    print("Filtered scores :", scores)
    print("Final answer :", sum(scores))
    
    sd_sc = fs.sd.calc_score()
    scores = fs.get_del_score(sd_sc, [fs.sd], [])

    print("\nPart 2")
    print("Filtered scores :", scores)
    print("Final answer :", min(scores))
