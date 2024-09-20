with open('2023/data/input14.txt') as f:
    content = [line.strip() for line in f.readlines()]

def countColumn(column : str) -> int:
    if column == "": return 0

    if (split := column.find("#")) == -1:
        split = len(column)
    
    n, m = len(column), column.count("O", 0, split)
    return  int(m/2 * (2*n -(m-1))) + countColumn(column[split+1:])
    
    
def countTiltedNorth(platform):
    result = 0
    for column in [''.join(a) for a in zip(*platform)]:
        cur = countColumn(column)
        result += cur
    return result

print(countTiltedNorth(content))
