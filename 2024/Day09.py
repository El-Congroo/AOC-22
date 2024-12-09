# with open('2024/data/example.txt') as f:
with open('2024/data/input09.txt') as f:
    content = [int(y) for x in f for y in x.strip()]

cur_front_id = 0
cur_back_id = (len(content) - 1) // 2 + 1
fill_in = content[::-2]
free_cnt = sum(content[1::2])
all_cnt = sum(content)

sum1 = 0
i = 0
free = False
finished = False
cur_back_cnt = 0

for x in content:
    for j in range(x):
        if not free:
            sum1 += cur_front_id * i
        else:
            if cur_back_cnt == 0:
                cur_back_cnt = fill_in.pop(0)
                cur_back_id -= 1
            sum1 += cur_back_id * i
            cur_back_cnt -= 1
        i += 1
        if i == (all_cnt - free_cnt): finished = True; break
    if finished: break
    if not (free := not free): cur_front_id += 1

# 6330095022244
print("Part 1:", sum1)

def draw(c):
    for i, cnt in c:
        print((str(i) if i != None else ".") * cnt, end="")
    print()

enumerated_content = [(i//2, x) if i % 2 == 0 else (None, x) for i, x in enumerate(content) if x > 0]

reverse_enum_blocks = [x for x in enumerated_content[::-1] if x[0] != None]

def merge(index):
    mergeStorage = space = 0
    while enumerated_content[index][0] == None:
        mergeStorage += (space := enumerated_content[index][1])
        del enumerated_content[index]
        if index > len(enumerated_content) - 1: break
    if mergeStorage > 0:
        enumerated_content.insert(index, (None, mergeStorage))
    return (mergeStorage > space)

# go through all possibly movable blocks
for b in reverse_enum_blocks: 
    # print(b, end=": ")
    # draw(enumerated_content)
    
    # go over (free) blocks
    for i in range(len(enumerated_content)):
        
        # stop if there is no free space before cur element
        if enumerated_content[i] == b: break 
        
        # check if free and enough space
        if (None == enumerated_content[i][0]) and ((free_space := enumerated_content[i][1]) >= b[1]):
            
            # delete element being moved
            j = enumerated_content.index(b) 
            del enumerated_content[j]
            enumerated_content.insert(j, (None, occupied_space := b[1]))
            
            # merges free block
            merge(j-1)
            
            # delete empty space
            del enumerated_content[i]
            
            # insert free block and merge
            if (free_space := free_space - occupied_space) > 0:
                enumerated_content.insert(i, (None, free_space))
                if(merge(i - 1)): print("merged!")
            
            # insert blocked block
            enumerated_content.insert(i, b)
            break

sum2, i = 0, 0
for x, j in enumerated_content:
    if x == None:
        i += j
        continue
    for _ in range(j):
        sum2 += x * i
        i += 1

print("Part 2:", sum2) # != 6359444896937
