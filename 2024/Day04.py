with open('2024/data/input04.txt') as f:
    c = [l.strip() for l in f]

space = c + [''.join(x) for x in zip(*c)]
for x in range(s := len(c)):
    a = [(c[y][i := (y+x) % s], c[y][s-i-1]) for y in range(s)]
    a, b = [''.join([b[x] for b in a]) for x in range(2)]
    space += [a[:-x], a[-x:], b[:-x], b[-x:]]

print("Part 1:", sum([l.count("XMAS") + l.count("SAMX") for l in space]))

d = {'X': 0, 'M': 1, 'A': 2 ,'S': 4}
e = lambda e: [sum(d.get(c[y+z][x+z*e]) for z in range(-1, 2)) for y in range(1, s-1) for x in range(1, s-1)]

print("Part 2:", sum([l=='A' and m==n==7 for l, m, n in zip([y for x in c[1:-1] for y in x[1:-1]], e(1), e(-1))]))