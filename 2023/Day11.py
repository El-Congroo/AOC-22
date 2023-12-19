with open('2023/data/input11.txt') as f:
    content = [line.strip() for line in f.readlines()]

def getDistSum(allGalaxies):
    galCnt, distsum = len(allGalaxies), 0
    for i in range(galCnt):
        for j in range(i+1, galCnt):
            distsum += sum(map(lambda a, b: abs(a-b), allGalaxies[i], allGalaxies[j]))
    return distsum

def getAllGalaxPos(dist):
    allGalaxies, allGala, disty, distx = {}, [], 0, 0
    l = range(len(content))

    for i in l:
        if '#' not in content[i]: disty += 1
        else: 
            for j in l: 
                if content[i][j] == '#':
                    if (i, j) not in allGalaxies: allGalaxies[(i, j)] = [0, 0]
                    allGalaxies[(i, j)][0] = disty

        line = [x[i] for x in content]
        if '#' not in line: distx += 1
        else:
            for j in l:
                if line[j] == '#':
                    if (j, i) not in allGalaxies: allGalaxies[(j, i)] = [0, 0]
                    allGalaxies[(j, i)][1] = distx

    for k in allGalaxies.keys():
        allGala.append(tuple(map(lambda a, b, d: a + (b * d), k, allGalaxies.get(k), [dist for _ in range(2)])))
    return allGala

print("Part one:", getDistSum(getAllGalaxPos(1)))
print("Part two:", getDistSum(getAllGalaxPos(1000000-1)))