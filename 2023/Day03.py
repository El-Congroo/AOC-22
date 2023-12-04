import re

with open('2023/data/input03.txt') as f:
    content = ["." + line.strip() + "." for line in f.readlines()]
    border = "."*len(content[0])
    content.insert(0, border)
    content.append(border)

def isAdjacent(i, start, end):
    for mov in range(-1,2):
        if re.search(r'[^.\d]', content[i+mov][start-1:end+1]):
            return True
    return False

def getPotGear(i, start, end):
    pot = []
    for mov in range(-1,2):
        for match in re.finditer(r'[*]', content[i+mov][start-1:end+1]):
            pot.append((start+match.start(), i+mov))
    return pot


sumOne = 0
sumTwo = 0
i = 1
potGears = {}
for line in content[1:-1]:
    for match in re.finditer(r'\d+', line):
        for position in getPotGear(i, match.start(), match.end()):
            if position in potGears:
                sumTwo += potGears[position] * int(match.group())
            else:
                potGears[position] = int(match.group())
        if isAdjacent(i, match.start(), match.end()):
            sumOne += int(match.group())
    i += 1

print("Part One:", sumOne)
print("Part Two:", sumTwo)