with open('2023/data/input12.txt') as f:
    content = [line.strip().split() for line in f.readlines()]

cache = {}

def getArrCnt(key):
    condition, numbers = key
    if numbers == (): return 1 if "#" not in condition else 0
    if condition == "": return 0

    ret, n = 0, numbers[0]
    for i in range(len(condition) - n + 1):
        if (i != 0 and condition[i-1] == "#"): break
        if "." not in condition[i:i+n] and (i+n == len(condition) or condition[i+n] != "#"):
            key = (condition[i+n+1:], numbers[1:])
            if key not in cache: 
                cache[key] = getArrCnt(key)
            ret += cache[key]
    return ret


print("Part one:", sum(getArrCnt((condition, tuple(map(int, numbers.split(","))))) for condition, numbers in content))
print("Part two:", sum(getArrCnt(("?".join([condition]*5), tuple(map(int, numbers.split(",")))*5)) for condition, numbers in content))