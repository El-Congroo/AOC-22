with open('2024/data/input01.txt') as f: 
    [left, right] = [sorted(l) for l in zip(*[list(map(int, line.split("   "))) for line in f])]

print("Part 1:", sum([abs(x-y) for x,y in zip(left, right)]))
print("Part 2:", sum(l * right.count(l) for l in set(left)))
