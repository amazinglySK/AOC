import portion as P

f = input('File name : ')
with open(f) as inp_file : 
    chunks = inp_file.read().split("\n\n")
    
    seeds = {int(x): [int(x)] for x in chunks[0].split(": ")[1].split(" ")}
    # All the map chunks
    for chunk in chunks[1:] : 
        chunk = chunk.strip()
        mapped = []
        for i in chunk.split("\n")[1:] : 
            i = i.strip()
            dest, so, ln = (int(x) for x in i.split(" "))
            not_mapped = [x for x in seeds if x not in mapped]
            for s in not_mapped : 
                diff = seeds[s][-1] - so
                if 0 <= diff < ln : 
                    seeds[s].append(dest + diff) 
                    mapped.append(s)
        
        not_mapped = [x for x in seeds if x not in mapped]
        for nm in not_mapped : 
            seeds[nm].append(seeds[nm][-1])

    m = min([seeds[s][-1] for s in seeds])
    print(m)

    
    seeds = []
    seeds_string = chunks[0].split(": ")[1].split(" ")
    i = 0

    # Parsing them into ranges
    while i < len(seeds_string) - 1 : 
        start = int(seeds_string[i])
        end = int(seeds_string[i+1]) - 1 + start
        seeds.append(P.closed(start, end))
        i += 2

    for chunk in chunks[1:] : 
        chunk = chunk.strip()
        new = []
        for i in chunk.split("\n")[1:] : 
            i = i.strip()
            dest, so, ln = (int(x) for x in i.split(" "))
            diff = so - dest # The diff which will be later subtracted to get mapped value
            mapped_idx = []
            for idx, i in enumerate(seeds) : 
                intersection = P.closed(so, so + ln -1) & i
                if not intersection.empty : 
                    st, sp = intersection.lower, intersection.upper
                    c = P.closed(st - diff, sp - diff) # Mapped values
                    new.append(c)
                    for k in i - P.open(so-1, so + ln) : # Non intersectiing values
                        new.append(k) # Non mapped values, but won't be there in any other chunk range

                    mapped_idx.append(idx)
            not_mapped = [seeds[idx] for idx in range(len(seeds)) if idx not in mapped_idx]
            seeds = not_mapped
        
        seeds.extend(new)
    
    m = min([s.lower for s in seeds])

    print(m)
