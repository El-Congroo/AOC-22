with open('2022/data/input20.txt') as f:
    content = [complex(a.strip()) for a in f.readlines()]

i = 0

while i < len(content):
    if content[i].imag != 0:
        i += 1
        continue

    print("i: ", i, "  content: ", [int(x.real) for x in content])

    # move 
    value = content[i].real
    newPos = int((i + value) % len(content))
    
    del content[i]
    content.insert(newPos, value + 1j)


    

print(content)

ret = 0

for i in range(1000, 3001, 1000):
    ret += content[(i+content.index(1j))%len(content)]

print(ret)