#read file

find = 2020
numbers = set()

with open('2020/data/input01.txt') as f:
    content = [int(x) for x in f.readlines()]

for i in content:
    numbers.add(i)

for i in numbers:
    if find - i in numbers:
       print(f"Pair: ({i}, {find - i}) adds up to {find}. Multiplied the result is {(find - i) * i}") 


for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == find:
                print(i*j*k)
                exit(1)