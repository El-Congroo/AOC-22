with open('2024/data/input04.txt') as f:
    c = [l.strip() for l in f]

space = c + [''.join(x) for x in zip(*c)]
for x in range(w := len(c[0])):
    a, b = "", ""
    for y in range(h := len(c)):
        y = (y+x) % w
        a += c[y][y]
        b += c[y][h-y-1]
    space += [a[:-x], a[-x:], b[:-x], b[-x:]]

print("Part 1:", sum([l.count("XMAS") + l.count("SAMX") for l in space]))


d = {'X': 0, 'M': 1, 'A': 2 ,'S': 4}
e = lambda e: [[sum(d.get(c[y + z][x + z * e]) for z in range(-1, 2)) for x in range(1, w - 1)] for y in range(1, h - 1)]

print("Part 2:", sum([o == 'A' and p == q == 7 for l, m, n in zip(c[1:-1], e(1), e(-1)) for o, p, q in zip(l[1:-1], m, n)]))