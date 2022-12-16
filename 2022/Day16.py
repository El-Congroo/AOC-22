import re

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

for i in readData():
    print(i)