import numpy as np


with open('data/input9.txt') as f:
    content = f.readlines()

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

visited = set()
slungThere = set()


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

for line in content:
    line = line.strip().split(" ")
    for i in range(int(line[1])):
        posH += directions[line[0]]
        posT = next(posH, posT)
        visited.add(tuple(posT))


##############
### Part 2 ###
##############

for line in content:
    line = line.strip().split(" ")
    for i in range(int(line[1])):
        knots[0] += directions[line[0]]
        for j in range(1, 10):
            knots[j] = next(knots[j-1], knots[j])
        slungThere.add(tuple(knots[9]))



print("visited part 1: ", len(visited))
print("slung there part 2: ", len(slungThere))


