import copy as cp

#################
### read data ###
#################

#read file
with open('data/input5.txt') as f:
    content = f.readlines()

#format towers
towers = []
for i in content:
    if(i[1] == '1'):
        break
    towers.append(i[1::4])

towers = list(zip(*towers[::-1]))

#delete all elements that are spaces from towers
for i in range(len(towers)):
    towers[i] = list(filter(lambda x: x != ' ', towers[i]))

#copy list towers
towers2 = cp.deepcopy(towers)


#format moves
idx= len(towers[0])+3
move = []
for i in range(idx, len(content)):
    move.append([x-1 for x in list(map(int, content[i].split()[1::2]))])


##########################
### algorithm part one ###
##########################

for i in move:
    for j in range(i[0]+1):
        towers[i[2]].append(towers[i[1]].pop(-1))


##########################
### algorithm part two ###
##########################

for i in move:
    copyFrom = len(towers2[i[1]])-i[0]-1
    towers2[i[2]].extend(towers2[i[1]][copyFrom:])
    towers2[i[1]] = towers2[i[1]][:copyFrom]
    


####################
### print result ###
####################

print("Part one: ")
for i in range(len(towers)):
    print(towers[i].pop(-1), end='')

print(" ")
print(" ")

print("Part two: ")
for i in range(len(towers2)):
    print(towers2[i].pop(-1), end='')

