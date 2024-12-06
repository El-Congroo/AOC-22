import time

time_start = time.time()

with open('2024/data/input06.txt') as f:
    c = [x.strip() for x in f.readlines()]

min_max = lambda x,y : [x, y+1] if x < y else [y, x+1]

obstructions = set()
visited = set()


for y in range(h := len(c)):
    for x in range(w := len(c[0])):
        if (i := c[y][x]) == "#": obstructions.add((y, x))
        if i == "^": startGuard = (guard := (y, x))

def addPositions(yStart, xStart, yEnd, xEnd):
    for y in range(*min_max(yStart, yEnd)):
        for x in range(*min_max(xStart, xEnd)):
            visited.add((y, x))

dirs = [
    [0, True,  lambda y: (y[0], y[1], 0,    y[1]),  1, lambda x,y: x<y], #up
    [1, False,  lambda y: (y[0], y[1], y[0], w-1),  -1, lambda x,y: x>y], #right
    [0, False, lambda y: (y[0], y[1], h-1,  y[1]), -1, lambda x,y: x>y], #down
    [1, True, lambda y: (y[0], y[1], y[0], 0),     1, lambda x,y: x<y], #left
]

pt1, i = 0, -1
while True:
    [d, r, border, e, l] = dirs[i := (i+1) % len(dirs)]
    obstacles = [o for o in obstructions if o[1-d] == guard[1-d] and l(o[d], guard[d])]
    if len(obstacles) == 0:
        addPositions(*border(guard))
        break
    obstacles.sort(key=lambda x: x[d], reverse=r)
    
    nextGuard = list(obstacles[0])
    nextGuard[d] += e
    addPositions(*guard, *nextGuard)
    
    guard = nextGuard

time_mid = time.time()

sum2 = 0
for j in visited:
    obstructions.add(j)
    guard, hit, i = startGuard, {}, -1
    
    while True:
        [d, r, border, e, l] = dirs[i := (i+1) % len(dirs)]
        
        obstacles = [o for o in obstructions if o[1-d] == guard[1-d] and l(o[d], guard[d])]
        if len(obstacles) == 0: break
        obstacle = sorted(obstacles, key=lambda x: x[d], reverse=r)[0]
        
        nextGuard = (obstacle[0] + (1-d) * e, obstacle[1] + d * e)

        if i in (k := hit.setdefault(nextGuard, [])):
            sum2 += 1
            break
        else: 
            k.append(i)
        
        guard = nextGuard

    obstructions.remove(j)
    

time_end = time.time()

print("pt1", len(visited), "duration", time_mid - time_start)
print("pt2", sum2, "duration", time_end - time_mid)
        