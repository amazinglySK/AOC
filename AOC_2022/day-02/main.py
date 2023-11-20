'''
A -> Rock -> 1
B -> Paper -> 2
C -> Scissors -> 3

X -> Rock
Y -> Paper
Z -> Scissors

---

X -> Lose
Y -> Draw
Z -> Win
'''

scores = {"X" : 1, "Y" : 2, "Z" : 3}

def check_status(curr, opp) : 
    losing = [("A", "Z"), ("B", "X"), ("C", "Y")]
    winning = [("A", "Y"), ("B", "Z"), ("C", "X")]

    if (curr, opp) in winning : 
        return True
    
    if (curr, opp) in losing :
        return False

    return "Draw"

def return_move_score(curr, stat) : 
    losing = {"A": 3, "B" : 1, "C": 2}
    winning = {"A" : 2, "B" : 3, "C" : 1}
    draw = {"A" : 1, "B" : 2, "C" : 3}

    if stat == True:
        return winning[curr] + 6
    elif stat == "Draw":
        return draw[curr] + 3
    elif stat == False:
        return losing[curr]

    return 0


def translate(curr):
    d = {"X" : False, "Y" : "Draw", "Z" : True}
    if curr not in d.keys():
        return ""
    return d[curr]

with open("input.txt") as inp_file : 
    lines = inp_file.read().strip().split("\n")
    score = 0
    alt_score = 0

    for match in lines : 
        split = match.split(" ")
        stat = check_status(split[0], split[1])

        if stat == False : 
            score += scores[split[1]]
        elif stat == True: # Win
            score += scores[split[1]] + 6
        elif stat == "Draw": # Draw
            score += scores[split[1]] + 3
        
        t = translate(split[1])
        s = return_move_score(split[0], t)
        alt_score += s


    print("--Part-1--")

    print(score)

    print("--Part-2--")

    print(alt_score)


