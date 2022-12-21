import re
import numpy as np

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
nodesBigger0 = []


def getNextNodes(node, content):
    for line in content:
        if line[0][0] == node:
            return line[1]


def getPressure(node, content):
    for line in content:
        if line[0][0] == node:
            return line[0][1]


def setListOfNodesRateBigger0(content):
    ret = []
    for line in content:
        if line[0][1] > 0:
            ret += [line[0][0]]
    global nodesBigger0
    nodesBigger0 = ret


def getState(content):
    key = 0
    for node in nodesBigger0:
        key *= 2
        if getPressure(node, content) > 0:
            key += 1
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
        for next in getNextNodes(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesLeft - 2), maxRelease)

        maxRelease += thisPressure * (minutesLeft - 1)
        setPressure(node, content, thisPressure)

    # just walk
    for next in getNextNodes(node, content):
        maxRelease = max(getMaxPressure(next, content, minutesLeft - 1), maxRelease)

    """
    setPressure(node, content, 0)
    for next in getNextNodes(node, content):
        maxRelease = max(getMaxPressure(next, content, minutesLeft -1 -np.sign(thisPressure)), maxRelease)
    maxRelease += thisPressure * (minutesLeft-1)
    setPressure(node, content, thisPressure)
    """
    
    setDyn(content, minutesLeft, node, maxRelease)
    return getDyn(content, minutesLeft, node)


def part1(content):
    minutes = 30
    setListOfNodesRateBigger0(content)
    val = getMaxPressure(content[0][0][0], content, minutes)
    return val


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        print("maxPressure is", part1(readData()))

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename='needs_profiling.prof')


if __name__ == "__main__":
    main()
