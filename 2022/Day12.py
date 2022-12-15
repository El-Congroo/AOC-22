# open test data
with open('data/input12.txt') as f:
    grid = [[ord(c)-97 for c in line.strip()] for line in f.readlines()]

#################
### Algorithm ###
#################

def dijkstra(queue, grid, end):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    distance = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    distance[queue[0][0]][queue[0][1]] = 0
    grid[queue[0][0]][queue[0][1]] = 0

    while queue:
        y, x = queue.pop(0)
        for dy,dx in directions:
            if min(y+dy, x+dx) >= 0 and y+dy < len(grid) and x+dx < len(grid[0]) and distance[y+dy][x+dx] == -1 and grid[y][x] +1 >= grid[y+dy][x+dx]:
                distance[y+dy][x+dx] = distance[y][x] + 1
                queue.append(tuple((y+dy,x+dx)))

    return distance[end[0]][end[1]]



##############
### Part 1 ###
##############


# get start and end point
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == -14:
            start = (y, x)
        if grid[y][x] == -28:
            end = (y, x)

# set up queue
queue = []
queue.append(start)

# run algorithm
minimum = dijkstra(queue, grid, end)

print("Distance from start to End: ", minimum)



##############
### Part 2 ###
##############


##### IT IS WORKING, SO ITS GOOD #####


# get all possible starting points
starts = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 0:
            starts.append(tuple((y, x)))


# test minimum distance for each starting point
for start in starts:
    queue = []
    queue.append(start)
    steps = dijkstra(queue, grid, end)    

    if(steps > -1):
        minimum = min(steps, minimum)

print("Minimum distance from any a to the End: ", minimum)