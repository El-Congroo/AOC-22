import re
import copy

#################
### read file ###
#################

def readData():
    with open('2022/data/sample.txt') as f:
        content = [[b for b in a.replace(",", "").strip().split("to valv")] for a in f.readlines()]
        for line in content:
            line[0] = [line[0].split(" ")[1], int(re.findall(r'-?[0-9]+', line[0])[0])]
            line[1] = line[1].split(" ")[1:]
        return content

##############
### part 1 ###
##############

dynamic = {}


def getNextTunnels(node, content):
    for line in content:
        if line[0][0] == node:
            return line[1]


def countValvesWithRate(content):
    count = 0
    for line in content:
        if line[0][1] > 0:
            count += 1
    
    return count


def getPressure(node, content):
    for line in content:
        if line[0][0] == node:
            return line[0][1]


def getState(content):
    key = 0
    for line in content:
        key += line[0][1]
    return key


def setPressure(node, content, pressure):
    for line in content:
        if line[0][0] == node:
            line[0][1] = pressure


def setDyn(content, minutesLeft, pos, i):
    dynamic[(minutesLeft, getState(content), pos)] = i


def getDyn(content, minutesLeft, pos):
    if (minutesLeft, getState(content), pos) in dynamic:
        return dynamic[(minutesLeft, getState(content), pos)]
    else: 
        return -1


def getMaxPressure(node, content, minutesLeft):
    if minutesLeft <= 0:
        return 0

    ret = getDyn(content, minutesLeft, node)
    if ret >= 0:
        return ret

    thisPressure = getPressure(node, content)

    if minutesLeft == 1:
        setDyn(content, minutesLeft, node, thisPressure)
        return getDyn(content, minutesLeft, node)

    maxRelease = 0

    # open and walk
    if thisPressure > 0:
        setPressure(node, content, 0)
        thisPressure *= minutesLeft-1
        for next in getNextTunnels(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesLeft-2), maxRelease)

        maxRelease += thisPressure * (minutesLeft -1)
        setPressure(node, content, thisPressure)

    # just walk
    for next in getNextTunnels(node, content):
        maxRelease = max(getMaxPressure(next, content, minutesLeft-1), maxRelease)

    setDyn(content, minutesLeft, node, maxRelease)
    return getDyn(content, minutesLeft, node)



def part1(content):
    minutes = 30
    val = getMaxPressure(content[0][0][0], content, minutes)
    print("maxPressure:", val)


part1(readData())