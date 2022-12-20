rocks = [{0, 1, 2, 3},
         {1 + 2j, 1j, 1 + 1j, 2 + 1j, 1},
         {0, 1, 2, 2 + 1j, 2 + 2j},
         {0, 1j, 2j, 3j},
         {0, 1, 1j, 1 + 1j}]
rocksDim = [4 + 1j, 3 + 3j, 3 + 3j, 1 + 4j, 2 + 2j]

width = 7
nrUnitsTat = 1000000000000
nrUnits = nrUnitsTat
sigSize = 40
file = "input17"
# del_every = 300


def draw(title, tower, movedRock, height):
    print(title, ":")
    for y in range(height+5, max(-1, height-5), -1):
        for x in range(width):
            if x + y * 1j in tower:
                print("#", end="")
            elif x + y * 1j in movedRock:
                print("@", end="")
            else:
                print(".", end="")
        print("")
    print("")


def onGround(movedRock):
    return movedRock.imag == 0


def fall(rockPos):
    return rockPos - 1j


def setHeight(rockPos, i):
    return rockPos.real + i*1j


def moveBy(rockPos, rockId, i):
    if -i > rockPos.real:
        return rockPos.imag * 1j

    if rockPos.real + rocksDim[rockId].real + i > width:
        return (width-rocksDim[rockId].real) + rockPos.imag * 1j

    return i + rockPos.real + rockPos.imag * 1j


def move(content, rockPos, rockId, j):
    i = content[j]

    if rockPos.real + i < 0 or rockPos.real + rocksDim[rockId].real + i > width:
        return rockPos

    return rockPos + i


def maxHeight(height, rockPos):
    return max(height, int(rockPos.imag))


def readData():
    with open(f'2022/data/{file}.txt') as f:
        return [[int(y.replace("<", "-1").replace(">", "1")) for y in x.strip()] for x in f.readlines()][0]


def isOverlapping(rockPos, rockId, tower):
    for i in getRockSet(rockPos, rockId):
        if i in tower:
            return True
    return False
    # return not isNotOverlapping(rockPos, rockId, tower)


def isNotOverlapping(rockPos, rockId, tower):
    return not isOverlapping(rockPos, rockId, tower)
    # return set(getRockSet(rockPos, rockId)).isdisjoint(tower)


def getRockList(rockPos, rockId):
    return [x + rockPos for x in rocks[rockId]]


def getRockSet(rockPos, rockId):
    a = set()
    for i in rocks[rockId]:
        a.add(i + rockPos)
    return a


def getSignature(tower, height):
    return frozenset([height*1j - x for x in tower if height - x.imag <= sigSize])


def partOne():
    content = readData()
    tower, beforeBlock = set(), set()
    height, added, i, ptr = 0, 0, 0, 0
    seen = {}

    while i < nrUnits:
        rockId = i % len(rocks)
        offsetStartPos = 0

        for k in range(3):
            offsetStartPos += content[ptr]
            ptr = (ptr+1) % len(content)

        rockPos = moveBy(height * 1j + 2, rockId, offsetStartPos)

        while isNotOverlapping(rockPos, rockId, tower):
            movedRockPos = move(content, rockPos, rockId, ptr)
            ptr = (ptr+1) % len(content)

            if isOverlapping(movedRockPos, rockId, tower):
                movedRockPos = rockPos

            if onGround(movedRockPos):
                break
            
            rockPos = fall(movedRockPos)
            draw(f"Stein {i} fell", tower, getRockSet(movedRockPos, rockId), int(movedRockPos.imag))

        tower = tower.union(getRockSet(movedRockPos, rockId))
        height = maxHeight(height, movedRockPos + rocksDim[rockId])

        signature = getSignature(tower, height)
        sr = (ptr, rockId, signature)

        if sr in seen and i > 2022:
            oldi, oldHeight = seen[sr]
            dy = height-oldHeight
            di = i-oldi
            amt = (nrUnits - i) // di
            added += amt*dy
            i += amt*di
            assert i <= nrUnits

        seen[sr] = (i, height)

#       Attempt to boost performance
#       if i % del_every == 0:
#           tower = tower - beforeBlock
#           beforeBlock = tower

        i += 1

    print("Height: ", height, "added: ", added)
    return height + added


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        print(partOne())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='needs_profiling.prof')

if __name__ == "__main__":
    main()
