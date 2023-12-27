with open('2023/data/input12.txt') as f:
    content = [line.strip().split() for line in f.readlines()]

cache = {}

def getArrCnt(condition, numbers):
    if len(numbers) == 0: return 1 if "#" not in condition else 0
    if len(condition) == 0: return 0

    if key := (condition, numbers) in cache: return cache[key]

    ret, n = 0, numbers[0]

    if condition[0] in ".?":
        ret += getArrCnt(condition[1:], numbers)
        
    if condition[0] in "#?":
        if n <= len(condition) and "." not in condition[:n] and (n == len(condition) or condition[n] != "#"):
            ret += getArrCnt(condition[n+1:], numbers[1:])
        
    cache[key] = ret
    return ret


print("Part one:", sum(getArrCnt(condition, tuple(map(int, numbers.split(",")))) for condition, numbers in content))
print("Part two:", sum(getArrCnt("?".join([condition]*5), tuple(map(int, numbers.split(",")))*5) for condition, numbers in content))