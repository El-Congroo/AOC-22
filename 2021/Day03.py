import numpy as np
import math

###################
###  read data  ###
###################

def getContent():
    with open('data/2021/input03.txt') as f:
        return [[int(a) for a in b.strip()] for b in f.readlines()]


####################
###    part 1    ###
####################

def part1():
    gamma, epsilon = "", ""
    for line in np.rot90(np.array(getContent())):
        mostCommmon = 1 if sum(line) > len(line)/2 else 0
        gamma = str(mostCommmon) + gamma
        epsilon = str(1- mostCommmon) + epsilon
    return int(epsilon, 2) * int(gamma, 2)


####################
###    part 2    ###
####################

def mostCommon(content, i):
    ret = 0
    for number in content:
        ret += -1 if number[i] == 0 else 1
    return 0 if ret < 0 else 1

def leastCommon(content, i):
    return 1 - mostCommon(content, i)

def binListList2Dec(binList):
    return int("".join([str(a) for a in binList[0]]), 2)

def getOxy():
    oxy = getContent()
    i = 0
    while len(oxy) > 1:
        oxy = [a for a in oxy if a[i] == mostCommon(oxy, i)]
        i += 1
    return binListList2Dec(oxy)

def getCo2():
    co2 = getContent()
    i = 0
    while len(co2) > 1:
        co2 = [a for a in co2 if a[i] == leastCommon(co2, i)]
        i += 1
    return binListList2Dec(co2)

def part2():
    return getOxy() * getCo2()





####################
### print answer ###
####################

print("part1:", part1())
print("part2:", part2())
