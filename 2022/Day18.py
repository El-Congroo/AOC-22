
with open('2022/data/input18.txt') as f:
    content = [[int(y)-1 for y in x.strip().split(",")] for x in f.readlines()]

size = 21

lava = [[[0 for z in range(size)] for y in range(size)] for x in range(size)]

for x, y, z in content:
    lava[x][y][z] = 1

# des ist schon hart hässlich. kann man das iwie in eine Schleife klatschen?

cmp = 0
count = 0
for x in range(size):
    for y in range(size):
        for z in range(size):
            count += cmp != lava[x][y][z]
            cmp = lava[x][y][z]
        if cmp:
            cmp = 0
            count += 1

for z in range(size):
    for x in range(size):
        for y in range(size):
            count += cmp != lava[x][y][z]
            cmp = lava[x][y][z]
        if cmp:
            cmp = 0
            count += 1

for y in range(size):
    for z in range(size):
        for x in range(size):
            count += cmp != lava[x][y][z]
            cmp = lava[x][y][z]
        if cmp:
            cmp = 0
            count += 1

print("Part One:", count)

for i in lava:
    for j in i:
        print(j)
    print("")

