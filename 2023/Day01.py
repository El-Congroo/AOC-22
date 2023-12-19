import re

with open('2023/data/input01.txt') as f:
    content = [line for line in f.readlines()]

sumOne = 0
for line in content:
    numbers = [int(i) for i in re.findall(r'\d', line)]
    sum += numbers[0] * 10 + numbers[-1]


sumTwo = 0 
numberDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4, 
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def parseToInt(n):
    if n in numberDict:
        return numberDict[n]
    return(int(n))

for line in content:
    numbers = [match.group(1) for match in re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)]
    sum += parseToInt(numbers[0]) * 10 + parseToInt(numbers[-1])

print("Part one:", sumOne)
print("Part two:", sumTwo)