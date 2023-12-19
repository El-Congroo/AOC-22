import re

with open('2023/data/input05.txt') as f:
    content = [line.strip() for line in f.readlines()]

seeds = [int(x) for x in re.findall(r'\d+', content[0])]
curRanges = [int(x) for x in re.findall(r'\d+', content.pop(0))]
curRanges = [(x, x+y) for x, y in zip(curRanges[::2], curRanges[1::2])] # save seeds

maps, map = [], []
for line in content:
    if len(line) == 0:
        maps.append(map)
        map = []
        continue
    if line[-1] == ":":
        continue

    dest, src, off = [int(x) for x in re.findall(r'\d+', line)]
    map.append(((src, src+off), dest - src)) # (range, offset) 
maps.append(map)

################
### part one ###
################

locations = []
for seed in seeds:
    for map in maps:
        for (start, stop), off in map:
            if seed in range(start, stop):
                seed += off
                break
    locations.append(seed)

print("Part one:", min(locations))

################
### Part two ###
################

def intersect(r1, r2): # r1 & r2
    if(r1[0] >= r2[1] or r1[1] <= r2[0]): return None
    return (max(r1[0],r2[0]), min(r1[1],r2[1]))

def difference(r1, r2): # r1 - r2
    ret = []
    if(r1[0] >= r2[1] or r1[1] <= r2[0]): return [r1]
    if(r1[0] < r2[0]): ret.append((r1[0], r2[0]))
    if(r1[1] > r2[1]): ret.append((r2[1], r1[1]))
    return ret

def setOff(r, offset):
    return tuple(x+offset for x in r)

for map in maps:                                            # iterate over all ...-to-... maps
    nextranges = []
    for convertRange, offset in map:                        # get stuff to one of the map ranges
        for _ in range(len(curRanges)):                     # try for every not moved range
            cur = curRanges.pop(0)                          # get one of our seed ranges
            inters = intersect(cur, convertRange)           # check if it should be moved
            if inters != None:
                curRanges += difference(cur, convertRange)  # numbers that aren't moved should be reconsidered
                nextranges.append(setOff(inters, offset))   # once they're offset they'll have to wait for the next ...-to-... map to be moved
            else:
                curRanges.append(cur)                       # if they don't overlap with the current map range. Maybe with the next one
    curRanges += nextranges                                 # when the next ...-to-... map comes, it's time to add the moved seeds

print("Part two:", min([x[0] for x in curRanges]))