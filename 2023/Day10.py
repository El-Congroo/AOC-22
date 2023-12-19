with open('2023/data/input10.txt') as f:
    content = [line for line in f.readlines()]

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)

allPipes = set()

pipesFrom = {
    n: ["|", "7", "F", "S"],
    e: ["-", "J", "7", "S"], 
    s: ["|", "L", "J", "S"],
    w: ["-", "L", "F", "S"]
}

possible = {
    "|": [n, s],
    "-": [e, w],
    "L": [n, e],
    "J": [n, w],
    "7": [s, w],
    "F": [e, s],
    "S": [n, e, s, w]
}



DY = len(content)
DX = len(content[0])

def getAnimalPos():
    for y in range(DY): 
        for x in range(DX):
            if content[y][x] == "S": 
                return (y,x)

def getTile(pos):
    y, x = pos
    return content[y][x]

def getNextPosition(pos, last):
    for d in possible.get(getTile(pos)):
        nextPos = tuple(map(lambda i, j: i + j, pos, d))
        tile = getTile(nextPos)
        if tile in pipesFrom.get(d) and nextPos != last:
            allPipes.add(nextPos)
            return nextPos

def countLoopLength(pos = getAnimalPos()):
    last, pos, count = pos, getNextPosition(pos, pos), 0
    while getTile(pos) != "S":
        pos, last = getNextPosition(pos, last), pos
        count += 1
    return count

def getInnerTilesCnt():
    cnt = 0
    for y in range(DY):
        for x in range(DX):
            if (y, x) in allPipes: continue
            inner = False
            for x1 in range(x+1, DX):
                inner ^= ((y, x1) in allPipes and getTile((y, x1)) in pipesFrom.get(n))
            cnt += 1 if inner else 0 
    return cnt

print("Part one:", int(countLoopLength()/2+0.5))
print("Part two:", getInnerTilesCnt())