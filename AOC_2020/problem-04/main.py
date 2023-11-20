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

class Passport :
    def __init__(self, passport_text) : 
        self.details = {}
        for i in passport_text.split() :
            j = i.split(":")
            self.details[j[0]] = j[1]

        self.validity = self.final_check()

    def final_check(self) :
        self.c = False 
        if self.check_valid_keys() :
            self.c = True
            # print(self.details) 
            return self.check_valid_values()
        
        return False

    def check_valid_keys(self) : 
        return all([x in self.details.keys() for x in fields])
    
    def check_valid_values(self) :
        # Birth year
        byr = self.details["byr"]
        if not (byr.isdigit() and 1920 <= int(byr) <= 2002) : 
            return False
        # Issue year
        iyr = self.details["iyr"]
        if not (iyr.isdigit() and 2010 <= int(iyr) <= 2020) : 
            return False
        # Expiry year
        eyr = self.details["eyr"]
        if not (eyr.isdigit() and 2020 <= int(eyr) <= 2030) : 
            return False
        
        # Height
        hgt = self.details["hgt"]
        exp = r"[0-9]+(in|cm)"
        if not bool(re.fullmatch(exp, hgt)) :
            return False
        else : 
            if bool(re.match(r"cm", hgt)) and not 150 <= int(hgt[:-2]) <= 193 : 
                return False
            elif bool(re.match(r"in", hgt)) and not 59 <= int(hgt[:-2]) <= 76 : 
                return False
            
        # Eye Colour 
        exp = r"amb|blu|brn|gry|grn|hzl|oth"
        if not bool(re.fullmatch(exp, self.details["ecl"])):
            return False
        
        # Passport Id
        exp = r"[0-9]{9}"
        if not bool(re.fullmatch(exp, self.details["pid"])): 
            return False
        
        # Hair colour
        pattern = r"#[a-f|1-9]{6}"
        if not bool(re.fullmatch(pattern, self.details["hcl"])):
           return False
        
        return True
        

with open('input.txt', 'r') as input_file:
    INPUT = input_file.read().strip().split('\n\n')
    part1= just_find_valids(INPUT)
    print(part1)


    # Part 2
    passes = []
    c = 0
    c1 = 0
    for p in INPUT:
        passp = Passport(p)
        if passp.c : c1+=1
        if passp.validity : 
            c+=1
    
    print(c)
    print(c1)
        
    # Part 2
    ValidPassports = 0
    for passport in INPUT:
        if (re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport) and re.search(r"eyr:202\d|eyr:2030", passport) and
                re.search(r"iyr:201\d|iyr:2020", passport) and re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", passport) and
        re.search(r"hcl:#[a-z0-9]{6}", passport) and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) and re.search(r"pid:\d{9}\b", passport)):
            ValidPassports += 1

    print(ValidPassports)