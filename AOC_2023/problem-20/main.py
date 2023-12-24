import sys
import time

f = sys.argv[1] 


def update(a, signal, fr) : # n = {type, state}, signal = True/False
    if a["type"] == "%" :
        if signal : return
        # Low pulse from here on
        a["state"][1] = not a["state"][1]

    elif a["type"] == "&" : 
        a["state"] = {**a["state"], fr : signal}
        

def decide(a, signal) :
    if a["type"] == "%" : 
        if signal : return signal
        else : 
            return a["state"][1]
    elif a["type"] == "&" : 
        return not all(a["state"].values())

        
def simulate(signals) : 
    
    h = l = 0
    idx = 0
    curr_pending = {(False, "broadcaster")}
    while not (idx != 0 and all(not all(signals[k]["state"].values()) for k in signals if k != "broadcaster")): 
        curr_nodes = {x[1] for x in curr_pending}
        temp = set()
        if idx == 0 : idx += 1
        for sig, i in curr_pending : 
            curr = i 
            curr_states = signals[curr]

            to = curr_states
            if curr != "broadcaster" : 
                sig = decide(curr_states, sig)
                to = curr_states["to"]

            for i in to : 
                if sig: h += 1
                else : l += 1
                if i not in signals : continue
                update(signals[i], sig, curr)
                if i in curr_nodes : continue
                temp.add((sig, i))
            print(curr, "---", sig, "--->", "".join(to), h, l)

        curr_pending = temp
        time.sleep(2)
    
    print(curr_pending)
    for sig, i in curr_pending :
        sig = decide(signals[i], sig)
        if sig : h += 1
        else : l += 1
    return h, l + 1
        
with open(f) as fp : 
    lines = fp.readlines()
    signals = {}
    for l in lines : 
        l = l.strip()
        a, b = tuple(l.split(" -> "))
        b = b.split(", ")
        if a == "broadcaster" : 
            signals[a] = b
            continue
        op = a[0]
        a = a[1:]
        if op == "%" : state = {1 : False}
        else : state = {}
        signals[a] = {"type" : op, "to" : b, "state" : state}

    
    print(signals)
    h, l = simulate(signals)
    print(h, l)

