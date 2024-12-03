with open('2024/data/input02.txt') as f:
    c = [[int(i) for i in l.split(" ")] for l in f]

dif = lambda l: [a-b for a, b in zip(l[:-1], l[1:])]
chk = lambda d: (0<min(d)<=max(d)<=3) or (-3<=min(d)<=max(d)<0)
rmv = lambda l, d, m: (lambda i: l[:i] + l[i+1:])(d.index(m(d)))

pt1 = pt2 = 0
for l in c:
    if chk(d := dif(l)): pt1 += 1; pt2 += 1
    elif any(chk(dif(i)) for i in [rmv(l, d, max), rmv(l, d, min), l[:-1]]): pt2 += 1

[print(s) for s in [f"Part 1: {pt1}", f"Part 2: {pt2}"]]
