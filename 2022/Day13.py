import ast

#################
### read file ###
#################


with open('data/input13.txt') as f:
    lists = [line.strip() for line in f.readlines()]

while '' in lists:
    lists.remove('')

for i in range(len(lists)):
    lists[i] = ast.literal_eval(lists[i])

#################
### algorithm ###
#################

def difference(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            try:
                dif = difference(a[i], b[i])
            except: 
                return len(b) - len(a)
            
            if(dif != 0 and dif != None):
                return dif

    elif isinstance(a, int) and isinstance(b, int):
        return b - a
    elif isinstance(a, list) and isinstance(b, int):
        return difference(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return difference([a], b)

################
### part one ###
################

points = 0
element = 1
nbrElements = len(lists)//2

for pairs in [lists[i*2:i*2+2] for i in range(nbrElements)]:

    if difference(pairs[0], pairs[1]) > 0:
        points += element
    element +=1

print("The answer to live and everything is" , points)


################
### part two ###
################

key_elements = [[[2]], [[6]]]

lists.extend(key_elements)

for i in range(len(lists)):
    for j in range(1, len(lists)-i):
        if(difference(lists[j-1], lists[j]) < 0):
            tmp = lists[j]
            lists[j] = lists[j-1]
            lists[j-1] = tmp

score = 1
for i in key_elements:
    score *= lists.index(i) + 1

print("The answer to live and everything and part two is", score)