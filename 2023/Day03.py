import re

with open('2023/data/input03.txt') as f:
    content = ["." + line.strip() + "." for line in f.readlines()]
    border = "."*len(content[0])
    content.insert(0, border)
    content.append(border)

def isAdjacent(i, start, end):
    if content[i][start-1] != "." or content[i][end] != ".":
        return True
    for mov in range(-1,2,2):
        if re.search(r'[^.\d]', content[i+mov][start-1:end+1]):
            return True
    return False
        

sumOne = 0
i = 1
for line in content[1:-1]:
    print(line)
    for match in re.finditer(r'\d+', line):
        if isAdjacent(i, match.start(), match.end()):
            sumOne += int(match.group())
    i += 1

print(sumOne)