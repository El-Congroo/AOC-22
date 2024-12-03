with open('2024/data/input02.txt') as f:
    c = [[int(x) for x in line.split(" ")] for line in f]

getDiff = lambda l: [a - b for a,b in zip(l[:-1], l[1:])]
rmIdx = lambda l, d, m: (lambda i: l[:i] + l[i+1:])(d.index(m(d)))
chkDiff = lambda d: (0 < min(d) <= max(d) <= 3) or (-3 <= min(d) <= max(d) < 0)

pt1 = pt2 = 0
for l in c:
    if chkDiff(d := getDiff(l)): pt1 += 1; pt2 += 1
    elif any(chkDiff(getDiff(i)) for i in [rmIdx(l, d, max), rmIdx(l, d, min), l[:-1]]): pt2 += 1

[print(sol) for sol in [f"Part 1: {pt1}", f"Part 2: {pt2}"]]
