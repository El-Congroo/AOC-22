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

dict = {}

def getFollowUpTunnels(node, content):
    for line in content:
        if line[0][0] == node:
            return line[1]


def getValvesWithRate(content):
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


def setCalced(content, minutesLeft, pos, i):
    dict[(minutesLeft, getState(content), pos)] = i


def getCalced(content, minutesLeft, pos):
    if (minutesLeft, getState(content), pos) in dict:
        return dict[(minutesLeft, getState(content), pos)]
    else: 
        return -1
    

def getMaxPressure(node, content, minutesLeft, calced):

    if minutesLeft <= 0:
        return 0

    ret = getCalced(content, minutesLeft, node)
    if ret >= 0:
        return ret

    thisPressure = getPressure(node, content)

    if minutesLeft == 1:
        setCalced(content, minutesLeft, node, thisPressure)
        return thisPressure


    maxRelease = 0

    # open and walk (and open)
    if thisPressure > 0 and minutesLeft >= 3:
        setPressure(node, content, 0)
        for next in getFollowUpTunnels(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesLeft-2, calced), maxRelease)
        maxRelease += thisPressure
        setPressure(node, content, thisPressure) 

    # just walk (and open)
    if minutesLeft >= 2:
        for next in getFollowUpTunnels(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesLeft-1, calced), maxRelease)
    
    print("in", node, "time left:", minutesLeft, "maxRelease:", maxRelease)


    setCalced(content, minutesLeft, node, maxRelease)
    return maxRelease



def part1(content):
    minutes = 30
    valWRate = getValvesWithRate(content)
    # min        combinatoins
    calced = [[-1 for _ in range(valWRate*valWRate)] for _ in range(minutes)]
    # print(calced)
    print("maxPressure:", getMaxPressure(content[0][0][0], content, minutes, calced))


part1(readData())