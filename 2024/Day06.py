import time

time_start = time.time()

obst_by, visited = [{}, {}], set()
directions = [
    [0, True,  lambda y: (y[0], y[1], 0,    y[1]),  1, lambda x,y: x<y], # up
    [1, False, lambda y: (y[0], y[1], y[0], w-1),  -1, lambda x,y: x>y], # right
    [0, False, lambda y: (y[0], y[1], h-1,  y[1]), -1, lambda x,y: x>y], # down
    [1, True,  lambda y: (y[0], y[1], y[0], 0),     1, lambda x,y: x<y], # left
]

####################
### prepare data ###
####################

with open('2024/data/input06.txt') as f:
    c = [x.strip() for x in f.readlines()]


for y in range(h := len(c)):
    for x in range(w := len(c[0])):
        if (i := c[y][x]) == "#": 
            # obstacles sorted by Y and X coords
            obst_by[0].setdefault(y, []).append(x) 
            obst_by[1].setdefault(x, []).append(y)
        if i == "^": 
            GUARD_START = (guard := (y, x))

for obst in obst_by:
    for key, l in obst.items(): obst[key] = tuple(sorted(l))

# reorders vars for ranges and increases end to include stop
def min_max(x,y):
    return [x, y+1] if x < y else [y, x+1]

def add_positions(yStart, xStart, yEnd, xEnd):
    for y in range(*min_max(yStart, yEnd)):
        for x in range(*min_max(xStart, xEnd)):
            visited.add((y, x))

# reads next obstacle from sorted tuple
def get_next_obst(guard, dir) -> list | None: 
    [i, j, _, _, l] = directions[dir]
    obstacles = obst_by[1-i].setdefault(guard[1-i], ())
    if j: obstacles = reversed(obstacles)
    for k in obstacles:
        if l(k, guard[i]):
            ret = [k]
            ret.insert(1-i, guard[1-i])
            return ret
    return None


##############
### Part 1 ###
##############

pt1, i = 0, -1
while True:
    [d, r, border, e, l] = directions[i := (i+1) % len(directions)]
    
    next_guard = get_next_obst(guard, i)
    if not next_guard: # guard left
        add_positions(*border(guard))
        break

    next_guard[d] += e # set guard one before obst
    add_positions(*guard, *next_guard)
    
    guard = next_guard

time_mid = time.time()

##############
### Part 2 ###
##############

sum2 = 0
for j in visited: # guard can collide with each pos on original route
    for k in range(2): # add j to obstacles
        cur = list(obst_by[k].setdefault(j[k], ()))
        cur.append(j[1-k])
        cur.sort()
        obst_by[k][j[k]] = cur

    # reset position of guard, positions guard hit obstacle and counter
    guard, hit, i = GUARD_START, {}, -1
    
    while True:
        [d, r, border, e, l] = directions[i := (i+1) % len(directions)]
        
        next_guard = get_next_obst(guard, i)
        if not next_guard: # guard left 
            break

        next_guard[d] += e # set guard one before obst
        guard = tuple(next_guard)

        # checks if guard at same pos with same orientation
        if i in hit.setdefault(guard, []):
            sum2 += 1
            break
        else: 
            hit.setdefault(guard, []).append(i)
    
    for k in range(2): # remove j from obstacles
        cur = list(obst_by[k][j[k]])
        cur.remove(j[1-k])
        obst_by[k][j[k]] = tuple(cur)
    

time_end = time.time()

print("pt1", len(visited), "duration", time_mid - time_start)
print("pt2", sum2, "duration", time_end - time_mid)
        