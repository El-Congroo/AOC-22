with open('2023/data/input09.txt') as f:
    content = [[int(x) for x in line.split(" ")] for line in f.readlines()]

def getNextNumber(numbers):
    return numbers[-1] if len(set(numbers)) == 1 else numbers[-1] + getNextNumber([y - x for x, y in zip(numbers[:-1], numbers[1:])])

sumOne, sumTwo  = 0, 0
for numbers in content:
    sumOne += getNextNumber(numbers)
    sumTwo += getNextNumber(numbers[::-1])

print("part one:", sumOne)
print("part two:", sumTwo)
