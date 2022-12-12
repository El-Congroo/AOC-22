with open('data/input10.txt') as f:
    content = [line.strip().split(" ") for line in f.readlines()]

sum = 0
value = 1
cycle = 0

for line in content:

    for i in range(len(line)):
        cycle += 1

        # draw numbers
        if abs(value+1-(cycle)%40) < 2 :
            print('#', end='')
        else:
            print('.', end='')

        if (cycle) % 40 == 0:
            print('')


        # sum signal strength
        if (cycle % 40) - 20 == 0:
            sum += value * cycle


        # addx number
        if i == 1:
            value += int(line[1])


    

        
        






print(sum)


