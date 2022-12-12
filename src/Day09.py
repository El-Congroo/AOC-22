import numpy as np


with open('data/input9.txt') as f:
    content = [line.strip().split(" ") for line in f.readlines()]


directions = {
    'L' : np.array([-1,  0]),
    'R' : np.array([ 1,  0]),
    'U' : np.array([ 0,  1]),
    'D' : np.array([ 0, -1])
}

posH = np.array([0, 0])
posT = np.array([0, 0])

knots = []
for i in range(10):
    knots.append(np.array([0, 0]))

visited, slungThere = set(), set()


##############
### Part 1 ###
##############

def next(posH, posT):
    match np.sum(np.abs(posH-posT)):
        case 2:
            # es ist Nacht und ich will schlafen. Deswegen komm jetzt sowas hier
            if(np.sum(np.abs(np.sign(posH-posT))) == 1): posT += np.sign(posH-posT)
            return posT
        case 3 | 4: 
            return posT + np.sign(posH-posT)
    return posT

for direction, steps in content:
    for _ in range(int(steps)):
        posH += directions[direction]
        posT = next(posH, posT)
        visited.add(tuple(posT))
    

##############
### Part 2 ###
##############

for direction, steps in content:
    for _ in range(int(steps)):
        knots[0] += directions[direction]
        for j in range(len(knots) - 1):
            knots[j+1] = next(knots[j], knots[j+1])
        slungThere.add(tuple(knots[9]))



print("visited part 1: ", len(visited))
print("slung there part 2: ", len(slungThere))


