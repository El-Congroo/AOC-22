def readData():
    with open('data/2021/input02.txt') as f:
        return [complex(eval(x.replace("forward ", "").replace("down", "1j *").replace("up", "-1j *").strip())) for x in f.readlines()]

def part1():
    pos = sum(readData())
    return int(pos.real * pos.imag)

def part2():
    pos, aim = 0, 0
    for i in readData():
        aim += i.imag
        pos += i.real + aim * 1j * i.real

    return int(pos.real * pos.imag)

print("Part1: ", part1())
print("Part2: ", part2())
