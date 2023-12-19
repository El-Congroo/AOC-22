with open('2023/data/input11.txt') as f:
    content = [line.strip() for line in f.readlines()]



x, y = 0, 0
for i in range(len(content)):
    if '#' not in content[i]: y +=1
    if '#' not in ''.strip([x[i] for x in content]): x += 1

    x += 1
    y += 1