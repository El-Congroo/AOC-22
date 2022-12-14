import numpy as np

######################
### set basic data ###
######################

with open('data/input14.txt') as f:
    content = [[[int(d) for d in c.split(',')] for c in b] for b in [a.strip().split('->') for a in f.readlines()]]


heightCave = 0
xSpan = [100000, 0]

for line in content:
    for x, y in line:
        xSpan = [min(x, xSpan[0]), max(x, xSpan[1])]
        heightCave = max(heightCave, y)

widthCave = xSpan[1] - xSpan[0] + 1
heightCave += 1

caveData = [widthCave, heightCave, xSpan[0]]
startPos = [0, 500-xSpan[0]]


################
### set cave ###
################

def setVoidCave(content):
    cave = [[0 for _ in range(widthCave)] for _ in range(heightCave)]

    for line in content:
        for i in range(1, len(line)):
            xStart = line[i-1][0] 
            yStart = line[i-1][1]
            widthDif = line[i][0] - xStart
            heightDif = line[i][1] - yStart
            xStart = xStart - caveData[2]
            
            
            for x in range(abs(widthDif) + 1):
                cave[yStart][xStart + x*np.sign(widthDif)] = 1

            for y in range(abs(heightDif) + 1):
                cave[yStart + y*np.sign(heightDif)][xStart] = 1
    return cave

def setGroundCave(content):
    cave = setVoidCave(content)

    xSpan[0] -= 2
    startPos[1] += 1

    for line in cave:
        line.insert(0, 0)
        line.append(0)
    
    for i in range(2):
        a = [i for _ in range(widthCave+2)]
        cave.append(a)
    
        
    return cave



######################
### cave functions ###
######################


def sand2Ground(cave, route, void):
    pos = startPos.copy()

    while True:
        newPos = canFall(cave, pos, void)
        if isinstance(newPos, list):
            pos = newPos
            if route:
                cave[pos[0]][pos[1]] = 3
        elif isinstance(newPos, int):
            if newPos == -1:
                return False
            if newPos == 0:
                cave[pos[0]][pos[1]] = 2
                return True


def canFall(cave, pos, void):
    if(void and (pos[1] == 0 or pos[1] == len(cave)-1 ) or pos[0] == len(cave)-1 or cave[pos[0]][pos[1]] == 2):
        return -1

    for i in [0, -1, 1]:
        xNew = pos[1]+i
        yNew = pos[0]+1
        try:
            if xNew >= 0 and xNew < len(cave[0]) and cave[yNew][xNew] == 0:
                return [yNew, xNew]
        except:
            return 1
    
    return 0
    

def draw(cave):
    for line in cave:
        for element in line:
            match element:
                case 0:
                    print('.', end='')
                case 1:
                    print('#', end='')
                case 2: 
                    print('+', end='')
                case 3:
                    print('~', end='')
        print('')

    print('')


def makeItRain(cave, void):
    while True:
        if not sand2Ground(cave, False, void):
            break

    sand2Ground(cave, True, void)
    draw(cave)


def countRestingSand(cave):
    restingSand = 0

    for line in cave:
        for element in line:
            if element == 2:
                restingSand += 1
    
    return restingSand

def countRestingSandGround(cave):
    a, b = 0, 0
    for i in range(len(cave)-2, 0, -1):
        if cave[i][0] == 0 and a == 0:
            a = len(cave) - i -2
        if cave[i][-1] == 0 and b == 0:
            b = len(cave) - i -2

    return countRestingSand(cave) + sum(range(a)) + sum(range(b))
    

##############
### Part 1 ###
##############

cave = setVoidCave(content)

makeItRain(cave, True)

print("there is so much sand:", countRestingSand(cave))


##############
### Part 2 ###
##############

cave = setGroundCave(content)

makeItRain(cave, False)

print("there is even more of so much sand:", countRestingSandGround(cave))