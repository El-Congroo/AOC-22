with open('2023/data/input11.txt') as f:
    content = [line.strip() for line in f.readlines()]

def doubleEmpty(galaxy):
    i = 0
    while i < len(galaxy):
        if '#' not in galaxy[i]:
            galaxy.insert(i, "."*len(galaxy[i]))
            i += 1
        i += 1

doubleEmpty(content)
content = [''.join(row) for row in zip(*reversed(content))]
doubleEmpty(content)

allGalaxies = []

for y in range(len(content)):
    for x in range(len(content[0])):
        if content[y][x] == '#':
            allGalaxies.append((y, x))

galCnt = len(allGalaxies)

distsum = 0 
for i in range(galCnt):
    for j in range(i+1, galCnt):
        distsum += sum(map(lambda a, b: abs(a-b), allGalaxies[i], allGalaxies[j]))

print("Part one:", distsum)