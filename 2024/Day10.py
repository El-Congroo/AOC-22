with open('2024/data/input10.txt') as f:
    c = [[int(x) for x in l.strip()] for l in f.readlines()]

get = lambda y, x : c[y][x] if 0 <= y < h and 0 <= x < w else None

def get_trailheads(y, x, val=0) -> list:
    l = [(y, x)] if get(y, x) == 9 else []
    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if get(y+dy, x+dx) == val + 1: 
            l += get_trailheads(y+dy, x+dx, val+1)
    return l

sum1 = sum2 = 0
for y in range(h := len(c)):
    for x in range(w := len(c[0])):
        if c[y][x] == 0:
            sum1 += len(set(t := get_trailheads(y, x)))
            sum2 += len(t)
            
print("part1:", sum1)
print("part2:", sum2)