### prepare input ###
antennae_dict, antinodes, antinodess = {}, set(), set()

with open('2024/data/input08.txt') as f:
    content = [[y if y.isalnum() else None for y in x.strip()] for x in f.readlines()]

for y in range(h := len(content)):
    for x in range(w := len(content[y])):
        if k := content[y][x]:
            antennae_dict.setdefault(k, []).append(complex(x, y))

### determine antinodes ###
is_in_bounds = lambda x : 0 <= x.imag < h and 0 <= x.real < w

for antennea in antennae_dict.values():
    for i, a in enumerate(antennea):
        antinodess.add(a)
        
        for j, b in enumerate(antennea[i+1:]):
            d = (c := a) - b
            
            for (d, e) in [(-d, b), (d, c)]:
                if is_in_bounds(e := e + d): 
                    antinodes.add(e)
                    while is_in_bounds(e := e + d): antinodess.add(e)

### print count ###
print("Part 1:", len(antinodes))
print("Part 2:", len(antinodes | antinodess))
