import re

with open('2023/data/input06.txt') as f:
    content = [re.findall(r'\d+', line) for line in f.readlines()]

numbers = [(int(x),int(y)) for x, y in zip(content[0], content[1])]
number = [int(''.join(x)) for x in content]

def bbcnt(msWhole, bestDistace): # bigger best count
    x1 =  int(-((msWhole**2 - 4 * bestDistace)**(1/2) - msWhole) / 2) + 1
    return msWhole-x1*2+1
    
prod1 = 1
for time, bestD in numbers:
    prod1 *= bbcnt(time, bestD) 

time, bestD = number

print("Part one", prod1)
print("Part two", bbcnt(time, bestD))
