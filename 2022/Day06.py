with open('data/input6.txt') as f:
    content = f.readlines()

data = content[0]
distinctNumbers = 14

for i in range(distinctNumbers-1, len(data)):
    pointer = True
    
    for j in range(0, distinctNumbers):
        for k in range(j+1, distinctNumbers):
            pointer = pointer & (data[i-j] != data[i-k])

    if(pointer) :
        print(i+1)
        break
