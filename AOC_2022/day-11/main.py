import math

class Monkey :

    def __init__(self, serial, items, op, condition, actions):
        self.serial = serial
        self.items = items
        self.orig_items = items
        self.op = op
        self.condition = condition
        self.actions = actions
        self.inspections = 0


    def inspect_items_in_hand(self, mod_constant, new) -> dict:
        passing = {x : [] for x in self.actions}
        # print(self.serial)
        # print(self.items)
        r = self.actions[::-1]
        for i in self.items:
            if new:
                i_dash = self.op(i) % mod_constant
            else:
                i_dash = self.op(i) // 3
            # print(i_dash)
            # i_dash//=3
            idx = int(self.condition(i_dash))
            monk = r[idx]
            passing[monk].append(i_dash)
        
        self.inspections += len(self.items)
        self.items = []
        return passing

    def add_items(self, items):
        self.items += items

    def reset(self):
        self.items = self.orig_items
        self.inspections = 0

def ParseMonkeys(ip) -> Monkey:
    sp = ip.split("\n")
    monkey_serial = sp[0].removesuffix(":").split(" ")[-1]
    monkey_items = [int(x) for x in sp[1].split(": ")[-1].split(", ")]
    monkey_op = lambda old : eval(sp[2].split(" = ")[-1])
    f = sp[3].split(' by ')[-1]
    monkey_condition = lambda x : eval(f"x % {f} == 0")
    monkey_actions = [int(sp[x].split(" monkey ")[-1]) for x in range(4, 6)]
    return Monkey(monkey_serial, monkey_items, monkey_op, monkey_condition, monkey_actions), int(f)

file = input("Enter the input file : ")

def simulate_rounds(monkeys : dict, mod_constant, rounds, new) : 
    for _ in range(rounds):
        for k in monkeys.keys():
            p = monkeys[k].inspect_items_in_hand(mod_constant, new)
            for i, v in p.items():
                monkeys[i].add_items(v)
                

with open(file, 'r') as inp_file:
    monkey_inputs = inp_file.read().strip().split("\n\n")
    monkeys = {}

    # THANKS REDDIT !!
    mod_constant = 1 # updated in the parse monkey function

    for idx, m in enumerate(monkey_inputs): 
        monk, f = ParseMonkeys(m)
        mod_constant*=f
        monkeys[idx] = monk

    simulate_rounds(monkeys, mod_constant, 20, False) # Keep this false for 1st part answer and true for second part answer
    scores = sorted([k.inspections for _, k in monkeys.items()], reverse=True)
    print("Part 1 :", scores[0] * scores[1])

    simulate_rounds(monkeys, mod_constant, 10000 - 20, True)
    scores = sorted([k.inspections for _, k in monkeys.items()], reverse=True)
    print("Part 2 :", scores[0] * scores[1])