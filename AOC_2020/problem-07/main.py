def search_bags(bags, curr_bag, seen = 0) : 
    if "shiny gold" in [num[0] for num in bags[curr_bag]] : 
        return True
    for k in bags[curr_bag]: 
        if search_bags(bags, k[0], seen) :
            return True

    return False

def calculate_nesting(bags, curr_bag) : 
    if bags[curr_bag]  == [] : 
        return 0 
    sum = 0 
    for bag in bags[curr_bag]:
        sum += bag[1] + bag[1] * calculate_nesting(bags, bag[0])

    return sum


with open("input.txt", 'r') as inp_file: 
    bags = {}
    for lines in inp_file.readlines() : 
        l = lines.strip()
        sp = l.split(" contain ")
        key = sp[0].rstrip(' bags')
        bags[key] = []
        if sp[-1] == "no other bags.":
            continue
        else : 
            sp[-1] = sp[-1].rstrip(".")
            sub_bags = sp[-1].split(", ")
            for sub in sub_bags : 
                num = (sub[2:].rstrip(' bags'), int(sub[0]))
                bags[key].append(num)

    c = 0
    for bag in bags: 
        if search_bags(bags, bag) : 
            c += 1
    print(c)

    sum = calculate_nesting(bags, "shiny gold")
    print(sum)


