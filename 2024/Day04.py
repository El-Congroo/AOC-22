with open('2024/data/input04.txt') as f:
    c = [l.strip() for l in f]

space = c + [''.join(x) for x in zip(*c)]
for x in range(w := len(c[0])):
    a,b = "",""
    for y in range(h := len(c)):
        a += c[y][i := (y+x) % w]
        b += c[y][h-i-1]
    space += [a[:-x], a[-x:], b[:-x], b[-x:]]

print("Part 1:", sum([l.count("XMAS") + l.count("SAMX") for l in space]))


d = {'X': 0, 'M': 1, 'A': 2 ,'S': 4}
e = lambda e: f([[sum(d.get(c[y+z][x+z*e]) for z in range(-1, 2)) for x in range(1, w-1)] for y in range(1, h-1)])
f = lambda x: [z for y in x for z in y]

print("Part 2:", sum([l=='A' and m==n==7 for l, m, n in zip(f(x[1:-1] for x in c[1:-1]), e(1), e(-1))]))