import re
import math

with open('2023/data/input02.txt') as f:
    content = [line for line in f.readlines()]

MAX_COLORS = [12, 13, 14]

col2idx = {
    "r": 0,
    "g": 1,
    "b": 2,
}

# OMG my first ever class in Python
class Game:
    def __init__(self, line):
        self.id = int(re.findall(r'\d+', line)[0])
        self.sets = []
        for round in line.split(";"):
            balls = re.findall(r'\d+ [r|g|b]', round)
            ballList = [0 for _ in range(3)]
            for ball in balls:
                ballList[col2idx[ball[-1]]] = int(ball[:-2])
            self.sets.append(Set(ballList))

    def isPossible(self):
        for set in self.sets:
            if not set.isPossible():
                return False
        return True
    
    def getAllSetMaxs(self):
        allValues = []
        for set in self.sets:
            allValues += set.cubes

        return [max(allValues[x::3]) for x in range(3)]
        
    def getPow(self):
        return math.prod(self.getAllSetMaxs())

class Set:
    def __init__(self, cubes):
        assert(len(cubes) == 3)
        self.cubes = cubes

    def isPossible(self):
        for (i,j) in zip(self.cubes, MAX_COLORS):
            if(i > j): return False
        return True

sumOne = 0
sumTwo = 0

for line in content:
    cur = Game(line)
    sumTwo += cur.getPow()
    if cur.isPossible():
        sumOne += cur.id
    
    

print("part one:", sumOne)
print("part two:", sumTwo)
