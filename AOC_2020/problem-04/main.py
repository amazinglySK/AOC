import re

cid = "cid"
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
def just_find_valids(inp) -> int:
    pattern = r"[\n, :, \s]+"
    field_sep = [re.split(pattern, x) for x in inp]
    valids = []
    for i in field_sep:
        validity = [x in i for x in fields]
        valids.append(all(validity))
    return valids.count(True)

class Passport:
    def __init__(self, dets : dict):
        self.details = dets
    
    def is_valid(self):
        keys = self.details.keys()
        if all([x in keys for x in fields]):
            for k, v in self.details:
                pass
        return False
    
    def check_condition(self, k, v:str):
        if k == 'byr':
            return len(v) == 4 and v.isnumeric() and 1920 <= int(v) <= 2002
        elif k == 'iyr':
            return len(v) == 4 and v.isnumeric() and 2010 <= int(v) <= 2020
        elif k == 'eyr':
            return len(v) == 4 and v.isnumeric() and 2020 <= int(v) <= 2030
        elif k == 'hgt':
            v = v[-1 : ]
            return len(v) == 4 and v.isnumeric() and 2020 <= int(v) <= 2030




with open('input.txt', 'r') as input_file:
    INPUT = input_file.read().strip().split('\n\n')
    part1= just_find_valids(INPUT)
        

