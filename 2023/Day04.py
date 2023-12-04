import re

with open('2023/data/input04.txt') as f:
    content = [line.split(":")[1] for line in f.readlines()]

i = 0 
sumOne = 0
size = len(content)
instances = [1 for _ in range(size)]

for line in content:
    winning = re.findall(r'\d+', line.split("|")[0])
    numbers = re.findall(r'\d+', line.split("|")[1])
    matches = len(set(winning) & set(numbers))
    if matches > 0:
        for j in range(i+1, i+matches+1):
            if j >= size: break
            instances[j] += instances[i]
        sumOne += 2**(matches-1)
    i += 1


print("Part One", sumOne)
print("Part Two", sum(instances))

