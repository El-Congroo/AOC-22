with open('2024/data/input02.txt') as f:
    content = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

partOne = 0
partTwo = 0

getDiff = lambda line: [a - b for a,b in zip(line[:-1], line[1:])]
checkVal = lambda mi, ma: (ma <= 3 and mi > 0) or (mi >= -3 and ma < 0)
getMinMax = lambda diff: (min(diff), max(diff))
checkDiff = lambda diff: checkVal(*getMinMax(diff))
checkList = lambda list: checkDiff(getDiff(list))

for line in content:
    diff = getDiff(line)
    if checkDiff(diff):
        partOne += 1
        partTwo += 1
        continue
    
    mi, ma = getMinMax(diff)
    mini, maxa, moxo = line[:], line[:], line[:-1]
    
    mini.pop(diff.index(mi))
    maxa.pop(diff.index(ma))
    
    if checkList(maxa) or checkList(mini) or checkList(moxo):
        partTwo += 1

print("Part1:", partOne)
print("Part2:", partTwo)
