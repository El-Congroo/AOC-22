with open('2023/data/input08.txt') as f:
    content = [line.strip() for line in f.readlines()]

direction = [0 if x=="L" else 1 for x in content[0]]
route = {}
for line in content[2:]:
    key, values = line.split(" = ")
    x, y = values[1:-1].split(", ")
    route[key] = (x, y)

cur = "AAA"
steps = 0
while cur != "ZZZ":
    cur = route[cur][direction[steps%len(direction)]]
    steps += 1
print("Part One:", steps)


def getGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

def getLCM(x, y):
   lcm = (x*y)//getGCD(x,y)
   return lcm

starts = [x for x in list(route) if x[-1] == "A"]
retTwo = 1
for cur in starts:
    steps = 0
    while cur[-1] != "Z":
        cur = route[cur][direction[steps%len(direction)]]
        steps += 1
    retTwo = getLCM(retTwo, steps)

print("PartTwo", retTwo)