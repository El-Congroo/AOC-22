import re
import copy

#################
### read file ###
#################

def readData():
    with open('data/sample.txt') as f:
        content = [[b for b in a.replace(",", "").strip().split("to valv")] for a in f.readlines()]
        for line in content:
            line[0] = (line[0].split(" ")[1], int(re.findall(r'-?[0-9]+', line[0])[0]))
            line[1] = line[1].split(" ")[1:]
        
        return content

##############
### part 1 ###
##############

def getFollowUpTunnels(node, content):
    for line in content:
        if line[0][0] == node:
            return line[1]

def getPressure(node, content):
    for line in content:
        if line[0][0] == node:
            return line[0][1]


def setPressure(node, content, pressure):
    for line in content:
        if line[0][0] == node:
            line[0][1] = pressure



def getMaxPressure(node, content, minutesleft):
    
    if minutesleft <= 0:
        return 0

    if minutesleft == 1:
        return getPressure(node, content)


    maxRelease = 0

    # open and walk (and open)
    if minutesleft >= 3:
        thisPressure = getPressure(node, content)
        setPressure(node, content, 0)
        for next in getFollowUpTunnels(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesleft-2), maxRelease)
        maxRelease += thisPressure
        setPressure(node, content, thisPressure) 

    # just walk
    if minutesleft >= 2:
        for next in getFollowUpTunnels(node, content):
            maxRelease = max(getMaxPressure(next, content, minutesleft-1), maxRelease)
    
    return maxRelease





    

def part1(content):
    print(getMaxPressure(content[0][0], content, 30))



for i in readData():
    print(i)