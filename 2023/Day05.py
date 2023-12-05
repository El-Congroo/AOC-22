import re

with open('2023/data/input05.txt') as f:
    content = [line for line in f.readlines()]

seeds = [int(x) for x in re.findall(r'\d+', content[0])]

# get all maps
maps = []
cur = []
for line in content[3:]:

    if line == '\n':
        maps.append(cur)
        cur = []
        continue
    
    if line[-2:-1] == ':':
        continue

    numbers = [int(x) for x in re.findall(r'\d+', line)]
    start = range(numbers[1], numbers[1]+numbers[2])
    offset = numbers[0] - numbers[1]
    cur.append((start, offset))
maps.append(cur)

locations = []
for seed in seeds:
    for map in maps:
        for convert in map:
            if seed in convert[0]:
                seed += convert[1]
                break
    locations.append(seed)

print(min(locations))

            