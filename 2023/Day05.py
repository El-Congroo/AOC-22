import re

with open('2023/data/example.txt') as f:
    content = [line.strip() for line in f.readlines()]

# print(content)

startranges = [int(x) for x in re.findall(r'\d+', content[0])]
startranges = [range(x, x+y) for x, y in zip(startranges[::2], startranges[1::2])]

def intersect(r1, r2):
    return range(max(r1.start,r2.start), min(r1.stop,r2.stop)) or None

def difference(r1, r2):
    return range(r1.start, r2.start), range(r1.stop, r2.stop)

def setOff(r, offset):
    return range(r.start + offset, r.stop + offset)

# get all maps
maps = []
map = []
for line in content[3:]:

    if len(line) == 0:
        maps.append(map)
        map = []
        continue
    if line[-1] == ":":
        continue

    dest, src, off = [int(x) for x in re.findall(r'\d+', line)]
    convertrange = range(src, src+off)
    offset = dest - src
    map.append((convertrange, offset))
maps.append(map)



seedranges = startranges
for map in maps:
    nextranges = []
    while len(seedranges) > 0:
        seedrange = seedranges.pop(0)
        for convertrange, offset in map:
            inters = intersect(seedrange, convertrange)
            if inters != None:
                seedranges += difference(seedrange, convertrange)
                nextranges.append(setOff(inters, offset))
                break
    # merge nextranges
    seedranges = nextranges

print("min:", min([x.start for x in seedranges]))