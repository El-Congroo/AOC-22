import copy as cp
import numpy as np
import matplotlib.pyplot as plt

#################
### read file ###
#################

with open('data/2022/input8.txt') as f:
    content = f.readlines()


######################
### set basic data ###
######################

content = [x.strip() for x in content]

rows = len(content)
columns = len(content[0])

visible = [[False for x in range(columns)] for y in range(rows)]

directions = [  [range(rows), range(columns)], 
                [range(rows), range(columns-1, -1, -1)], 
                [range(rows-1, -1, -1), range(columns)], 
                [range(rows), range(columns-1, -1, -1)]]


#####################
### Algotithm one ###
#####################
#    y  x
c = [0, 0]

for i in range(len(directions)):
    for c[i//2] in directions[i][0]:
        max = -1
        for c[(i//2+1)%2] in directions[i][1]:
            if(max < int(content[c[0]][c[1]])):
                max = int(content[c[0]][c[1]])
                visible[c[0]][c[1]] = True


#####################
### Algotithm two ###
#####################

estate_value = [[1 for x in range(columns)] for y in range(rows)]

content = [list(x) for x in content]

for i in range(4):
    for y in range(len(estate_value)):
        visibility = [1 for x in range(10)]
        for x in range(1, len(estate_value[y])):
            estate_value[y][x] *= (x+1) - visibility[int(content[y][x])]

            for j in range(int(content[y][x])+1):
                visibility[j] = x+1

    estate_value = np.rot90(estate_value)
    content = np.rot90(content)



####################
### print result ###
####################


count = 0
for row in visible:
    for column in row:
        if column:
            count += 1

print("Result task one: ", count)
print ("Result of the second tastk: ", np.max(estate_value))

estate_value = np.array(estate_value)



print(f"total number of visible trees: {count}\n highest scenic score: {np.max(estate_value)} [{100},{100}]")
plt.imshow(estate_value, cmap="viridis", interpolation="bilinear", norm="log")
plt.title("tree's scenic scores")
plt.show()
