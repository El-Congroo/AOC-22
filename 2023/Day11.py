with open('2023/data/input11.txt') as f:
    content = [line.strip() for line in f.readlines()]

def doubleEmpty(galaxy):
    i = 0
    while i < len(galaxy):
        if '#' not in galaxy[i]:
            galaxy.insert(i, "."*len(galaxy[i]))
            i += 1
        i += 1

doubleEmpty(content)
content = [''.join(row) for row in zip(*reversed(content))]
doubleEmpty(content)

print(len(content), len(content[0]))