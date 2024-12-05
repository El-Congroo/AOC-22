with open('2024/data/input05.txt') as f:
    [rules, orders] = [x.split("\n") for x in f.read().split("\n\n")]
    r = {}
    for rule in rules:
        [o, b] = map(int, rule.split("|"))
        r.setdefault(o, set()).add(b)

def isCorrectOrder(order : list) -> bool:
    for o in order: 
        if len(r.setdefault(o, set()) & set(order[:order.index(o)])) > 0: return False
    return True

def sort(order: list) -> list:
    i, redo = len(order), False
    while (i := i-1) > 0:
        for j in r.setdefault(order[i], []):
            if j in order[:i]:
                order.remove(j)
                order.insert(i, j)
                redo = True
        if redo: i, redo = i+1, False
    return order

pt1, pt2 = 0, 0
for order in orders[:-1]:
    order = list(map(int, order.split(",")))
    mid = len(order) // 2

    if isCorrectOrder(order):   pt1 += order[mid]
    else:                       pt2 += sort(order)[mid]

print("Part 1:", pt1)
print("Part 2:", pt2)