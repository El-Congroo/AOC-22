from math import log10

with open('2024/data/input11.txt') as f:
    content = [int(x) for x in f.readlines()[0].split(" ")]

lookups = [{} for _ in range(75)]

def blink(numbers, blinks_left):
    if blinks_left == 0:
        return len(numbers)
    sum = 0
    for n in numbers:
        if n not in (lookup := lookups[blinks_left-1]):
            if n == 0:
                lookup[n] = blink([1], blinks_left-1)
            elif (b := (int(log10(n))+1)) % 2 == 0:
                c = 10**(b//2)
                lookup[n] = blink([n // c, n % c], blinks_left-1)
            else:
                lookup[n] = blink([n * 2024], blinks_left-1)
        sum += lookup[n]
    return sum


print("part 1:", sum1 := blink(content, 25))
print("part 2:", sum2 := blink(content, 75))
