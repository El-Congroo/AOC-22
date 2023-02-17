import re
from z3 import *

def readData():
    with open('2022/data/input15.txt') as f:
        return [[int(b) for b in re.findall(r'-?[0-9]+', a)] for a in f.readlines()]


def getDistance(coords):
    return abs(coords[0]-coords[2])+abs(coords[1]-coords[3])

def getPossiblePos(coords):
    positions = set()
    x1, y1, x2, y2 = coords
    distance = getDistance(coords)
    for y in range(y1-distance, y1+distance+1):
        difference = max(y1 - y, y - y1)
        for x in range(x1-distance+difference, x1+distance-difference+1):
            positions.add(x + y * 1j)
    return positions

def getOuterEdgeElements(coords):
    positions = set()
    difOuterEdge = getDistance(coords) + 1
    for y in range(coords[1]-difOuterEdge, coords[1]+difOuterEdge+1):
        for x in [positions[0]-difOuterEdge, positions[0]+difOuterEdge]:
            if (x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000):
                positions.add(x + y * 1j)
    return positions

def getElementsInLine(coords, line):
    positions = set()
    size = getDistance(coords)
    difCenter2Line = abs(coords[1] - line)
    if size < difCenter2Line: 
        return set()
    difLine2Edge = size - difCenter2Line

    for x in range(coords[0]-difLine2Edge, coords[0]+difLine2Edge+1):
        positions.add(x + line * 1j)
    return positions



def getBeacons(data):
    positions = set()
    for coords in data:
        positions.add(coords[2]+ coords[3] * 1j)
    return positions

def getSetOfAllPos(data):
    allPositions = set()
    for coords in data:
        allPositions = allPositions.union(getPossiblePos(coords))
    return allPositions

def getAllElementsInLine(data, line):
    allPositions = set()
    for coords in data:
        allPositions = allPositions.union(getElementsInLine(coords, line))
    return allPositions

def removeBeacons(data, allPos):
    return allPos.difference(getBeacons(data))

def getNbrOfElementsInLine(set, line):
    return len([x for x in set if x.imag == line])


def getFreeXY(content, border):
    s = Solver()
    x, y = Ints('x y')
    s.add(x >= 0)
    s.add(y >= 0)
    s.add(x <= border)
    s.add(y <= border)
    
    for coords in content:
        distance = getDistance(coords)
        x1, y1, _, _ = coords
        s.add(Abs(x-x1) + Abs(y-y1) > distance)
    
    assert s.check() == sat, "unsat"
    result = s.model()

    return result[x].as_long(), result[y].as_long()

def getTuningFreq(x, y):
    return (x * 4_000_000) + y


def task1():

    lineNr = 2000000
    data = readData()
    elementsInLine = getAllElementsInLine(data, lineNr)
    blockedPos = removeBeacons(data, elementsInLine)
    nbr = getNbrOfElementsInLine(blockedPos, lineNr)
    print("in Line", lineNr, "are", nbr, "blocked positions")




def task2():
    border = 4_000_000
    data = readData()
    x, y = getFreeXY(data, border)
    print(f"The tuning frequency of the Beacon {x,y} is {getTuningFreq(x, y)}")




task1()
task2()