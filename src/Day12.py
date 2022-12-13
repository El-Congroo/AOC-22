with open('data/input12.txt') as f:
    grid = [[ord(c)-97 for c in line.strip()] for line in f.readlines()]

distance = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
directions = [(0,1),(0,-1),(1,0),(-1,0)]
queue = []


# find position of start node
setStart, setEnd = False, False
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == -14:
            start = (y, x)
            setStart = True
        if grid[y][x] == -28:
            end = (y, x)
            setEnd = True
        if setStart and setEnd:
            break
        


queue.append(start)
distance[start[0]][start[1]] = 0

while queue:
    y, x = queue.pop(0)

    for dy,dx in directions:
        if min(y+dy, x+dx) >= 0 and y+dy < len(grid) and x+dx < len(grid[0]) and distance[y+dy][x+dx] == -1 and grid[y][x] +1 >= grid[y+dy][x+dx]:
            distance[y+dy][x+dx] = distance[y][x] + 1
            queue.append(tuple((y+dy,x+dx)))

print(distance[end[0]][end[1]])