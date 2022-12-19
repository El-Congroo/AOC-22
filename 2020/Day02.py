with open('2020/data/input02.txt') as f:
    content = [[y for y in x.replace(":", "").strip().split(" ")] for x in f.readlines()]

validPasswords = 0
newPolicies = 0

for line in content:
    min, max = line[0].split("-")
    min, max = int(min), int(max)
    
    count = line[2].count(line[1])

    if count >= min and count <= max:
        validPasswords += 1

    min -= 1
    max -= 1
    minCor, maxCor = False, False

    if min >= 0 and min < len(line[2]):
        minCor = line[2][min] == line[1]

    if max >= 0 and max < len(line[2]):
        maxCor = line[2][max] == line[1]

    if (minCor != maxCor):
        newPolicies += 1

print(validPasswords)
print(newPolicies)