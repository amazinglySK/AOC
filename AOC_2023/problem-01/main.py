
def part1(lines) : 
    s = 0
    for line in lines :
        nums = [x for x in line if x.isdigit() == True]
        s += int(nums[0] + nums[-1])
    return s

def part2(lines) : 
    l = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # minimum window of 3 maximum window of 5
    s = 0 
    for line in lines : 
        line = line.strip() # Removes the new line characters
        nums = []
        i = 0
        while i < len(line) : # Each character
            if line[i].isdigit() : 
                nums.append(line[i])
            else : 
                for j in range(3, 6) : 
                    r = line[i:i+j]
                    if r in l : # Checking the window substring
                        nums.append(str(l.index(r) + 1))
                        break
            i += 1
        s += int(nums[0] + nums[-1])
    return s

f = input('File name : ')
with open(f) as inp_file : 
    lines = inp_file.readlines()
    s = part1(lines)
    print(s)
    s = part2(lines)
    print(s)
