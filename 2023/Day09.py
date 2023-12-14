with open('2023/data/input09.txt') as f:
    content = [[int(x) for x in line.split(" ")] for line in f.readlines()]

def nn(n): # get next number
    return n[0] if len(set(n) )== 1 else n[-1] + nn([y - x for x, y in zip(n[:-1], n[1:])])

sumOne, sumTwo  = 0, 0
for numbers in content:
    sumOne += nn(numbers)
    sumTwo += nn(numbers[::-1])

print("part one:", sumOne)
print("part two:", sumTwo)
