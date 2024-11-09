with open('2023/data/input14.txt') as f:
    content = [line.strip() for line in f.readlines()]

def countRow(column : str) -> int:
    if column == "": return 0

    if (split := column.find("#")) == -1:
        split = len(column)
    
    n, m = len(column), column.count("O", 0, split)
    
    return  int(m/2 * (2*n - (m-1))) + countRow(column[split+1:])
    
    
def countTiltedNorth(platform):
    result = 0
    for column in [''.join(a) for a in zip(*platform)]:
        cur = countRow(column)
        result += cur
    return result

print("Part 1:", countTiltedNorth(content))


def rotatePlatformOnce(platform):
    for _ in range(4): # directions
        newPlat = []
        for row in [list(x) for x in zip(*reversed(platform))]: # each row
            for i in range(len(row)): # n times
                changes = False
                for j in range(len(row)-1): # go over row
                    if row[j] == 'O' and row[j+1] == '.':
                        row[j] = '.'
                        row[j+1] = 'O'
                        changes = True
                if not changes:
                    break
            newPlat.append(row)
        platform = newPlat
    return platform
            

def rotatePlatformOften(platform):
    iter = 0
    d = {}
    ROTATECNT = 1000000000
    while iter < ROTATECNT:
        iter += 1
        platform = rotatePlatformOnce(platform)
        state = tuple(tuple(a) for a in platform)
        if state in d:
            rest = ROTATECNT - iter
            stepsize = iter - d[state]
            iter += (rest // stepsize) * stepsize
        else :
            d[state] = iter
    return platform
        

print("Part 2:", sum(weight * row.count('O') for weight, row in enumerate(rotatePlatformOften(content)[::-1], 1)))

