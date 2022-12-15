def readData():
    with open('data/2021/input01.txt') as f:
        return [int(x) for x in f.readlines()]

def aufgabe1(content):
    return sum(list(map(lambda x,y: 1 if x < y else 0, content[:-1], content[1:])))

def aufgabe2(content):
    return aufgabe1(list(map(lambda x,y,z: x+y+z, content[:-2], content[1:-1], content[2:])))

content = readData()
print("ret1:", aufgabe1(content))
print("ret2:", aufgabe2(content))