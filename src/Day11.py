import math

monkeys = []

class Monkey:

    inspect = 0

    def __init__(self, items, operation, divisibleBy, throwsTo):
        self.items = items
        self.operation = operation
        self.divisibleBy = divisibleBy
        self.throwsTo = throwsTo

    def numberItems(self):
        return len(self.items)

    def operate(self):
        old = self.items[0]
        self.items[0] = eval(self.operation)
        self.inspect += 1

    def bored(self):
        self.items[0] //= 3

    def getActive(self):
        return self.inspect

    def test(self):
        self.items[0] %= kgv
        return self.items[0] % self.divisibleBy == 0

    def throw(self):
        i = 1
        if self.test():
            i = 0
        return (self.throwsTo[i], self.items.pop(0))

    def catch(self, item):
        self.items.append(item)



with open('data/input11.txt') as f:
    content = [line.strip().replace(' ', '') for line in f.readlines()]


# create monkeys
for i in range(content.count('')+1):
    line = i*7
    items = list(map(int,content[line+1].split("items:")[1].split(',')))
    operation = content[line+2].split("Operation:new=")[1]
    divisibleBy = int(content[line+3].split("divisibleby")[1])
    throwsTo = [int(content[line+4].split("monkey")[1]),
                int(content[line+5].split("monkey")[1])]
    
    monkeys.append(Monkey(items, operation, divisibleBy, throwsTo))


# run monkeys
round = 10000

kgv = 1
# find kgv
for monkey in monkeys:
    kgv = math.lcm(kgv, monkey.divisibleBy)

print("kgv", kgv)



for i in range(round):
    for monkey in monkeys:
        for j in range(monkey.numberItems()):
            monkey.operate()
            # monkey.bored()
            catcher, item = monkey.throw()
            monkeys[catcher].catch(item)


activity = []
for monkey in monkeys:
    activity.append(monkey.getActive())


print(f"== After round {round} ==")
for i in range(len(activity)):
    print(f"Monkey {i} inspected items {activity[i]} times")

prod = 1
for _ in range(2):
    highest = max(activity)
    prod *= highest
    activity.remove(highest)


print(prod)