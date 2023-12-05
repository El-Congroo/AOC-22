import re

with open('2023/data/input05.txt') as f:
    content = [line.strip() for line in f.readlines()]

startranges = [int(x) for x in re.findall(r'\d+', content[0])]
startranges = [(x, x+y) for x, y in zip(startranges[::2], startranges[1::2])]

def intersect(r1, r2):
    if(r1[0] >= r2[1] or r1[1] <= r2[0]): return None
    return (max(r1[0],r2[0]), min(r1[1],r2[1]))

def difference(r1, r2):
    if(r1[0] >= r2[1] or r1[1] <= r2[0]):
        return [r1]
    ret = []
    if(r1[0] < r2[0]):
        ret.append((r1[0], r2[0]))
    if(r1[1] > r2[1]):
        ret.append((r2[1], r1[1]))
    return ret

def setOff(r, offset):
    return (r[0] + offset, r[1] + offset)

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
    convertRange = (src, src+off)
    offset = dest - src
    map.append((convertRange, offset))
maps.append(map)



curRanges = startranges
for map in maps:
    nextranges = []
    for convertRange, offset in map:
        for _ in range(len(curRanges)):
            cur = curRanges.pop(0)
            inters = intersect(cur, convertRange)
            if inters != None:
                curRanges += difference(cur, convertRange)
                nextranges.append(setOff(inters, offset))
            else:
                curRanges.append(cur)
    curRanges += nextranges

print("Part2:", min([x[0] for x in curRanges]))