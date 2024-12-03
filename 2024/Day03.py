import re
with open('2024/data/input03.txt') as f:
    c = ''.join([l.strip() for l in f])

print("Part 1:", sum([int(a) * int(b) for a,b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", c)]))

do, pt2 = True, 0
for e, f, g in re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", c):
    if not g: do = e == "do()"
    elif do: pt2 += int(f) * int(g)

print("Part 2:", pt2)
