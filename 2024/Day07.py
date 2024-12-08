import math

with open('2024/data/input07.txt') as f:
    c = [[[int(z) for z in y.split(" ")] for y in x.strip().split(": ")] for x in f.readlines()]

def is_calculatable(result: int, cur: int, chain: list, concatable: bool):
    if len(chain) == 0 or result < cur: return result == cur
    return is_calculatable(result, cur + chain[0], chain[1:], concatable) or is_calculatable(result, cur * chain[0], chain[1:], concatable) or (concatable and is_calculatable(result, int(cur*10**(1+math.floor(math.log10(chain[0])))+chain[0]), chain[1:], concatable))

[print(x, sum([result[0] for result, chain in c if is_calculatable(result[0], chain[0], chain[1:], y)])) for x, y in [["Part 1:", False], ["Part 2:", True]]]