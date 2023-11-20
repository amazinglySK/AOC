import re

# Part 1

def parse_input(string : str):
    regex = r"[-, :, \s]+"
    return re.split(regex, string)

class Password:

    def __init__(self, min, max, char, pwd):
        self.min = int(min)
        self.max = int(max)
        self.char = char
        self.pwd = pwd

    def check_validity(self) -> bool:
        return self.min <= self.pwd.count(self.char) <= self.max
    
    def check_toboggan_validity(self) -> bool:
        valids = [self.pwd[self.min - 1] == self.char,self.pwd[self.max - 1] == self.char]
        if valids.count(True) == 1:
            return True
        return False
        



with open("input.txt", 'r') as input_file:
    INPUT = [parse_input(x) for x in input_file.read().strip().split("\n")]
    passwords = [Password(x[0], x[1], x[2], x[3]) for x in INPUT]
    validities = [x.check_validity() for x in passwords]
    print(f"Part 1 : {validities.count(True)}")
    validities = [x.check_toboggan_validity() for x in passwords]
    print(f"Part 2 : {validities.count(True)}")
